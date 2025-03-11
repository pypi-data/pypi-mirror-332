"""`MazeDatasetConfig` is where you decide what your dataset should look like, then pass it to `MazeDataset.from_config` to generate or load the dataset.

see [demo_dataset notebook](../../notebooks/demo_dataset)

"""

import copy
import functools
import json
import multiprocessing
import typing
import warnings
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Literal, Optional, cast, overload

import numpy as np
import tqdm
from jaxtyping import Float, Int
from muutils.json_serialize import (
	json_serialize,
	serializable_dataclass,
	serializable_field,
)
from muutils.json_serialize.util import (
	_FORMAT_KEY,
	JSONdict,
	safe_getsource,
	string_as_lines,
)
from muutils.misc import sanitize_fname, shorten_numerical_to_str, stable_hash
from zanj import ZANJ
from zanj.loading import LoaderHandler, load_item_recursive, register_loader_handler

from maze_dataset.constants import Coord, CoordArray, CoordTup
from maze_dataset.dataset.dataset import (
	DatasetFilterProtocol,
	GPTDataset,
	GPTDatasetConfig,
	register_dataset_filter,
	register_filter_namespace_for_dataset,
)
from maze_dataset.dataset.success_predict_math import cfg_success_predict_fn
from maze_dataset.generation.generators import _GENERATORS_PERCOLATED, GENERATORS_MAP
from maze_dataset.maze import LatticeMaze, SolvedMaze

# If `n_mazes>=SERIALIZE_MINIMAL_THRESHOLD`, then the MazeDataset will use `serialize_minimal`.
# Setting to None means that `serialize_minimal` will never be used.
# Set to -1 to make calls to `read` use `MazeDataset._load_legacy`. Used for profiling only.
SERIALIZE_MINIMAL_THRESHOLD: int | None = 100


_PercolationSuccessArray = Float[
	np.ndarray,
	"p/grid_n/deadends/endpoints_not_equal/generator_func=5",
]


class NoPercolationInConfigError(ValueError):
	"""raised when trying to predict the success fraction of a config that doesn't have percolation"""

	pass


class SuccessChanceTooSmallError(ValueError):
	"""raised when the success fraction is below the threshold in `MazeDatasetConfig.success_fraction_compensate`"""

	pass


def set_serialize_minimal_threshold(threshold: int | None) -> None:
	"get the global SERIALIZE_MINIMAL_THRESHOLD"
	global SERIALIZE_MINIMAL_THRESHOLD  # noqa: PLW0603
	SERIALIZE_MINIMAL_THRESHOLD = threshold


def _load_maze_ctor(maze_ctor_serialized: str | dict) -> Callable:
	"get the maze constructor from `GENERATORS_MAP`"
	if isinstance(maze_ctor_serialized, dict):
		# this is both the new and old version of the serialization
		return GENERATORS_MAP[maze_ctor_serialized["__name__"]]
	elif isinstance(maze_ctor_serialized, str):
		# this is a version I switched to for a while but now we are switching back
		warnings.warn(
			"you are loading an old model/config in `_load_maze_ctor()`!!! this should not be happening, please report: "
			"https://github.com/understanding-search/maze-dataset/issues/new",
		)
		return GENERATORS_MAP[maze_ctor_serialized]
	else:
		err_msg: str = f"maze_ctor_serialized is of type {type(maze_ctor_serialized) = }, expected str or dict\n{maze_ctor_serialized = }"
		raise TypeError(err_msg)


EndpointKwargsType = dict[
	typing.Literal[
		"allowed_start",
		"allowed_end",
		"deadend_start",
		"deadend_end",
		"endpoints_not_equal",
		"except_on_no_valid_endpoint",
	],
	bool | None | list[tuple[int, int]],
]
"type hint for `MazeDatasetConfig.endpoint_kwargs`"


def _load_endpoint_kwargs(data: dict) -> EndpointKwargsType:
	if data.get("endpoint_kwargs") is None:
		return dict()

	else:
		return {
			k: (
				# bools and Nones are fine
				v
				if (isinstance(v, bool) or v is None)
				# assume its a CoordList
				else [tuple(x) for x in v]  # muutils/zanj saves tuples as lists
			)
			for k, v in data["endpoint_kwargs"].items()
		}


MAZEDATASETCONFIG_FNAME_HASH_LENGTH: int = 5


@serializable_dataclass(kw_only=True, properties_to_serialize=["grid_shape"])
class MazeDatasetConfig(GPTDatasetConfig):
	"""config object which is passed to `MazeDataset.from_config` to generate or load a dataset"""

	grid_n: int = serializable_field()

	# not comparing n_mazes is done primarily to avoid conflicts which happen during `from_config` when we have applied filters
	n_mazes: int = serializable_field(compare=False)

	maze_ctor: Callable = serializable_field(
		default=GENERATORS_MAP["gen_dfs"],
		serialization_fn=lambda gen_func: {
			"__name__": gen_func.__name__,
			"__module__": gen_func.__module__,
			"__doc__": string_as_lines(gen_func.__doc__),
			"source_code": safe_getsource(gen_func),
		},
		loading_fn=lambda data: _load_maze_ctor(data["maze_ctor"]),
		assert_type=False,  # TODO: check the type here once muutils supports checking Callable signatures
	)

	maze_ctor_kwargs: dict = serializable_field(
		default_factory=dict,
		serialization_fn=lambda kwargs: kwargs,
		loading_fn=lambda data: (
			dict()
			if data.get("maze_ctor_kwargs", None)
			is None  # this should handle the backwards compatibility
			else data["maze_ctor_kwargs"]
		),
	)

	endpoint_kwargs: EndpointKwargsType = serializable_field(
		default_factory=dict,
		serialization_fn=lambda kwargs: kwargs,
		loading_fn=_load_endpoint_kwargs,
		assert_type=False,
	)

	@property
	def grid_shape(self) -> CoordTup:
		"""return the shape of the grid as a tuple"""
		return (self.grid_n, self.grid_n)

	@property
	def grid_shape_np(self) -> Coord:
		"""return the shape of the grid as a numpy array"""
		return np.array(self.grid_shape)

	@property
	def max_grid_n(self) -> int:
		"""return the maximum of the grid shape"""
		return max(self.grid_shape)

	def stable_hash_cfg(self) -> int:
		"""return a stable hash of the config"""
		return stable_hash(
			json.dumps(
				self.serialize(),
				sort_keys=True,
				indent=None,
			),
		)

	# TODO: include fname in serialized form, but exclude it when hashing so we dont infinitely loop?
	def to_fname(self) -> str:
		"""return a unique identifier (valid as a filename) for this config"""
		n_mazes_str: str = shorten_numerical_to_str(self.n_mazes)
		maze_ctor_name: str = self.maze_ctor.__name__.removeprefix("gen_")
		hash_id: int = self.stable_hash_cfg() % 10**MAZEDATASETCONFIG_FNAME_HASH_LENGTH
		return sanitize_fname(
			f"{self.name}-g{self.grid_n}-n{n_mazes_str}-a_{maze_ctor_name}-h{hash_id}",
		)

	def summary(self) -> dict:
		"""return a summary of the config"""
		# do we run this to make sure it doesn't error?
		super_summary: dict = super().summary()
		assert super_summary
		self_ser: dict = self.serialize()
		return dict(
			name=self.name,
			fname=self.to_fname(),
			sdc_hash=self.stable_hash_cfg(),
			seed=self.seed,
			seq_len_min=self.seq_len_min,
			seq_len_max=self.seq_len_max,
			applied_filters=self.applied_filters,
			grid_n=self_ser["grid_n"],
			n_mazes=self_ser["n_mazes"],
			maze_ctor_name=self_ser["maze_ctor"]["__name__"],
			maze_ctor_kwargs=self_ser["maze_ctor_kwargs"],
			endpoint_kwargs=self_ser["endpoint_kwargs"],
		)

	def _to_ps_array(self) -> _PercolationSuccessArray:
		"""Convert this config to a [p, grid_n, deadends, endpoints_not_equal, generator_func] vector.

		used in predicting the success rate
		"""
		try:
			assert self.maze_ctor.__name__ in _GENERATORS_PERCOLATED, (
				f"generator not supported, must be a percolation generator\n{self.maze_ctor.__name__ = }, {_GENERATORS_PERCOLATED = }"
			)
			assert "p" in self.maze_ctor_kwargs, (
				f"maze_ctor_kwargs must have a 'p' (percolation value) key: {self.maze_ctor_kwargs = }"
			)
			assert not self.endpoint_kwargs.get("except_on_no_valid_endpoint", True), (
				f"except_on_no_valid_endpoint must be False, or else if any maze fails to generate, the whole dataset will fail: {self.endpoint_kwargs = }"
			)
		except AssertionError as e:
			err_msg: str = f"invalid config for percolation success prediction: {self.summary() = }"
			raise NoPercolationInConfigError(
				err_msg,
			) from e

		endpoints_unique_flag: int = int(
			self.endpoint_kwargs.get("endpoints_not_equal", True),
		)

		# adjustment for bknutson0
		if not (
			self.endpoint_kwargs.get("deadend_start", False)
			and self.endpoint_kwargs.get("deadend_end", False)
		):
			# we didnt train on this, but if either endpoint is not required to be in a dead end
			# then  requiring the endpoints to be unique does not really affect the success rate
			# (except for very small percolation values, pure percolation generation)
			endpoints_unique_flag: int = 0

		return np.array(
			[
				float(self.maze_ctor_kwargs["p"]),
				float(self.grid_n),
				float(
					int(
						self.endpoint_kwargs.get("deadend_start", False)
						or self.endpoint_kwargs.get("deadend_end", False),
					),
				),
				float(endpoints_unique_flag),
				float(_GENERATORS_PERCOLATED.index(self.maze_ctor.__name__)),
			],
			dtype=np.float64,
		)

	@classmethod
	def _from_ps_array(
		cls,
		arr: _PercolationSuccessArray,
		name: str = "predict",
		n_mazes: int = 100,
		**kwargs,
	) -> "MazeDatasetConfig":
		"""Reconstruct a config from an array [p, grid_n, deadends, endpoints_not_equal, generator_func] and other config parameters.

		# Returns:
		- `MazeDatasetConfig`
			Config corresponding to `arr`
		"""
		return cls(
			name=name,
			grid_n=int(arr[1]),
			n_mazes=n_mazes,
			maze_ctor=_GENERATORS_PERCOLATED[int(arr[4])],
			maze_ctor_kwargs={"p": float(arr[0])},
			endpoint_kwargs=dict(
				deadend_start=bool(arr[2]),
				deadend_end=bool(arr[2]),
				endpoints_not_equal=bool(arr[3]),
				except_on_no_valid_endpoint=False,
			),
			**kwargs,
		)

	def success_fraction_estimate(
		self,
		except_if_all_success_expected: bool = False,
	) -> float:
		"""Estimate the success fraction of this config.

		only valid when the generator is a percolation generator,
		and endpoints are enforced to be dead ends

		this estimate comes from `estimate_dataset_fractions.ipynb` and `maze_dataset.benchmarks.sweep_fit`

		# Parameters:
		- `except_if_all_success_expected : bool`
			if `True`, don't raise an error if the success fraction is below the threshold.
			will always return `1.0` if the config is not expected to fail

		# Returns:
		- `float`
			estimated success fraction

		# Raises:
		- `NoPercolationInConfigError` : if the config is not expected to fail, and `except_if_all_success_expected` is `False`
		"""
		try:
			return cfg_success_predict_fn(self)

		except NoPercolationInConfigError as e:
			if except_if_all_success_expected:
				return 1.0
			else:
				raise e  # noqa: TRY201

	def success_fraction_compensate(
		self,
		safety_margin: float = 1.2,
		except_if_all_success_expected: bool = False,
		epsilon: float = 1e-2,
	) -> "MazeDatasetConfig":
		"""return a new `MazeDatasetConfig` like this one with `n_mazes` adjusted to compensate for the success fraction

		# Parameters:
		- `safety_margin : float`
			safety margin to apply to the success fraction estimate
			(defaults to `1.2`, or 20% more mazes than estimated)
		- `except_if_all_success_expected : bool`
			if `True`, don't raise an error if the success fraction is below the threshold.
			this is passed to `MazeDatasetConfig.success_fraction_estimate`.
			if your config isn't expected to fail, passing this might mean you generate more mazes than needed
			since `safety_margin` is still applied.
			(defaults to `False`)
		- `epsilon : float`
			raise `SuccessChanceTooSmallError` if the success fraction is below this threshold
			(defaults to `1e-2`)

		# Returns:
		- `MazeDatasetConfig`
			new config with adjusted `n_mazes`

		# Raises:
		- `SuccessChanceTooSmallError` : if the computed success fraction is below `epsilon`
		"""
		# compute and check the success fraction
		success_fraction: float = self.success_fraction_estimate(
			except_if_all_success_expected=except_if_all_success_expected,
		)
		if success_fraction < epsilon:
			err_msg: str = (
				f"{success_fraction = } is below the threshold of {epsilon = }"
			)
			raise SuccessChanceTooSmallError(
				err_msg,
			)

		# compute the new number of mazes
		n_mazes: int = self.n_mazes
		new_n_mazes: int = int((n_mazes * safety_margin) / success_fraction) + 1

		# put it in a new config and return
		cfg_dict: dict = self.serialize()
		cfg_dict["n_mazes"] = new_n_mazes
		return MazeDatasetConfig.load(cfg_dict)


def _generate_maze_helper(index: int) -> Optional[SolvedMaze]:  # noqa: ARG001
	"""Helper function for generating mazes in parallel.

	> [!CAUTION]
	> don't use this unless generating in parallel!
	"""
	# TODO: don't use this unless generating in parallel!
	maze: LatticeMaze = _GLOBAL_WORKER_CONFIG.maze_ctor(
		grid_shape=_GLOBAL_WORKER_CONFIG.grid_shape_np,
		**_GLOBAL_WORKER_CONFIG.maze_ctor_kwargs,
	)

	endpoint_kwargs: EndpointKwargsType = _GLOBAL_WORKER_CONFIG.endpoint_kwargs.copy()

	# Generate the solution
	solution: Optional[CoordArray] = maze.generate_random_path(**endpoint_kwargs)

	# Validate the solution
	if (
		solution is None
		or len(solution) == 0
		or not isinstance(solution, np.ndarray)
		# magic value is fine here
		or len(solution.shape) != 2  # noqa: PLR2004
	):
		return None  # Return None if the solution is invalid

	return SolvedMaze.from_lattice_maze(
		lattice_maze=maze,
		solution=solution,
	)


def _maze_gen_init_worker(config: MazeDatasetConfig) -> None:
	"""special worker helper

	> [!CAUTION]
	> this makes the generation depend both on whether parallelism is used, and on the number of processes. this is bad!

	"""
	# TODO: dont use globals here!
	global _GLOBAL_WORKER_CONFIG  # noqa: PLW0603
	_GLOBAL_WORKER_CONFIG = config

	process_id: tuple[int] = multiprocessing.current_process()._identity
	if len(process_id) == 0:
		# no multiprocessing, seed was already set
		pass
	elif len(process_id) == 1:
		# multiprocessing, adjust seed based on process id
		# only set numpy seed, since we do not use other random gens
		np.random.seed(_GLOBAL_WORKER_CONFIG.seed + process_id[0])
	else:
		err_msg = (
			f"unexpected process id: {process_id = }\n{multiprocessing.Process() = }"
		)
		raise ValueError(
			err_msg,
		)


class MazeDataset(GPTDataset):
	"""a maze dataset class. This is a collection of solved mazes, and should be initialized via `MazeDataset.from_config`"""

	def __init__(
		self,
		cfg: MazeDatasetConfig,
		mazes: typing.Sequence[SolvedMaze],
		generation_metadata_collected: dict | None = None,
	) -> None:
		"""initialize a maze dataset from a config and a list of solved mazes"""
		super().__init__()
		self.cfg: MazeDatasetConfig = cfg
		self.mazes: list[SolvedMaze] = list(mazes)
		self.generation_metadata_collected: dict | None = generation_metadata_collected

	@classmethod
	def from_config(
		cls,
		cfg: MazeDatasetConfig,
		do_generate: bool = True,
		load_local: bool = True,
		save_local: bool = True,
		zanj: ZANJ | None = None,
		do_download: bool = True,
		local_base_path: Path = Path("data/maze_dataset"),
		except_on_config_mismatch: bool = True,
		allow_generation_metadata_filter_mismatch: bool = True,
		verbose: bool = False,
		**kwargs,
	) -> "MazeDataset":
		"""create a maze dataset from a config

		priority of loading:
		1. load from local
		2. download
		3. generate

		"""
		return cast(
			MazeDataset,
			super().from_config(
				cfg=cfg,
				do_generate=do_generate,
				load_local=load_local,
				save_local=save_local,
				zanj=zanj,
				do_download=do_download,
				local_base_path=local_base_path,
				except_on_config_mismatch=except_on_config_mismatch,
				allow_generation_metadata_filter_mismatch=allow_generation_metadata_filter_mismatch,
				verbose=verbose,
				**kwargs,
			),
		)

	def data_hash(self) -> int:
		"""return a hash of the data"""
		return stable_hash(str(tuple([x.serialize() for x in self.mazes])))

	def __getitem__(self, i: int) -> SolvedMaze:
		"""get a maze by index"""
		return self.mazes[i]

	def __deepcopy__(self, memo) -> "MazeDataset":  # noqa: ANN001
		"""deepcopy the dataset

		FIX: this isnt actually a deepcopy I think?
		"""
		return MazeDataset.load(self._serialize_full())

	# TYPING: get type hints on the tokenizer here
	@overload
	def as_tokens(
		self,
		maze_tokenizer,  # noqa: ANN001
		limit: int | None = None,
		join_tokens_individual_maze: Literal[False] = False,
	) -> list[list[str]]: ...
	@overload
	def as_tokens(
		self,
		maze_tokenizer,  # noqa: ANN001
		limit: int | None = None,
		join_tokens_individual_maze: Literal[True] = True,
	) -> list[str]: ...
	def as_tokens(
		self,
		maze_tokenizer,  # TODO: MazeTokenizer
		limit: int | None = None,
		join_tokens_individual_maze: bool = False,
	) -> list[list[str]] | list[str]:
		"""return the dataset as tokens according to the passed `maze_tokenizer`

		the `maze_tokenizer` should be either a `MazeTokenizer` or a `MazeTokenizerModular`

		if `join_tokens_individual_maze` is True, then the tokens of each maze are
		joined with a space, and the result is a list of strings.
		i.e.:

			>>> dataset.as_tokens(join_tokens_individual_maze=False)
			[["a", "b", "c"], ["d", "e", "f"]]
			>>> dataset.as_tokens(join_tokens_individual_maze=True)
			["a b c", "d e f"]
		"""
		output: list[list[str]] = [
			maze.as_tokens(maze_tokenizer) for maze in self.mazes[:limit]
		]
		if join_tokens_individual_maze:
			return [" ".join(tokens) for tokens in output]
		else:
			return output

	def __len__(self) -> int:
		"""return the number of mazes in the dataset"""
		return len(self.mazes)

	def __eq__(self, other: object) -> bool:
		"""compare two datasets"""
		if not isinstance(other, MazeDataset):
			raise NotImplementedError(
				"can only compare with other MazeDataset objects",
			)
		# TODO: compare hashes of data instead of the data itself?
		return self.cfg == other.cfg and self.mazes == other.mazes

	@classmethod
	def generate(
		cls,
		cfg: MazeDatasetConfig,
		gen_parallel: bool = False,
		pool_kwargs: dict | None = None,
		verbose: bool = False,
	) -> "MazeDataset":
		"""Generate a maze dataset given a config and some generation parameters"""
		# Copy the config to avoid modifying the original
		cfg_cpy: MazeDatasetConfig = MazeDatasetConfig.load(
			json.loads(json.dumps(cfg.serialize())),
		)

		if pool_kwargs is None:
			pool_kwargs = dict()
		maze_indexes: Int[np.ndarray, " maze_index"] = np.arange(cfg_cpy.n_mazes)  # type: ignore[assignment]

		solved_mazes: list[SolvedMaze | None]
		# Configure tqdm for progress bar
		tqdm_kwargs: dict = dict(
			total=cfg_cpy.n_mazes,
			unit="maze",
			desc="generating & solving mazes",
			disable=not verbose,
		)
		# TODO: don't use the global unless generating in parallel!
		if gen_parallel:
			with multiprocessing.Pool(
				**pool_kwargs,
				initializer=_maze_gen_init_worker,
				initargs=(cfg_cpy,),
			) as pool:
				solved_mazes = list(
					tqdm.tqdm(
						pool.imap(_generate_maze_helper, maze_indexes),
						**tqdm_kwargs,
					),
				)

		else:
			_maze_gen_init_worker(cfg_cpy)
			solved_mazes = list(
				tqdm.tqdm(
					map(
						_generate_maze_helper,
						maze_indexes.tolist(),
					),
					**tqdm_kwargs,
				),
			)

		# Filter out None values explicitly after ensuring all results are collected
		solved_mazes_: list[SolvedMaze] = [
			maze for maze in solved_mazes if maze is not None
		]
		# solved_mazes_ = list(filter(lambda x: x is not None, solved_mazes))

		# Update the config with the actual number of mazes
		cfg_cpy.n_mazes = len(solved_mazes_)

		dataset: MazeDataset = cls(
			cfg=cfg_cpy,
			mazes=solved_mazes_,
		)

		dataset.update_self_config()  # Call `update_self_config()` to ensure the dataset's config reflects changes

		np.random.seed(cfg_cpy.seed)  # Reset the seed to the value in the config copy

		return dataset

	@classmethod
	def download(cls, cfg: MazeDatasetConfig, **kwargs) -> "MazeDataset":
		"(not implemented yet!) download a maze dataset from the internet"
		raise NotImplementedError("not implemented yet")

	@classmethod
	def load(cls, data: JSONdict) -> "MazeDataset":
		"""load from zanj/json"""
		if data[_FORMAT_KEY] == "MazeDataset:minimal":
			return cls._load_minimal(data)
		elif data[_FORMAT_KEY] == "MazeDataset:minimal_soln_cat":
			return cls._load_minimal_soln_cat(data)
		elif data[_FORMAT_KEY] == "MazeDataset":
			if (
				SERIALIZE_MINIMAL_THRESHOLD == -1
			):  # Allow access to `_load_legacy` for profiling
				return cls._load_legacy(data)
			return cls._load_full(data)
		else:
			err_msg: str = f"`_FORMAT_KEY` string {data[_FORMAT_KEY] = } is not a recognized `MazeDataset` format. ({_FORMAT_KEY = })"
			raise KeyError(
				err_msg,
			)

	@classmethod
	def _load_full(cls, data: JSONdict) -> "MazeDataset":
		assert data[_FORMAT_KEY] == "MazeDataset"
		return cls(
			cfg=MazeDatasetConfig.load(data["cfg"]),  # type: ignore[arg-type]
			mazes=load_item_recursive(data["mazes"], tuple()),
			generation_metadata_collected=data["generation_metadata_collected"],  # type: ignore[arg-type]
		)

	@classmethod
	def _load_minimal(cls, data: JSONdict) -> "MazeDataset":
		assert data[_FORMAT_KEY] == "MazeDataset:minimal"
		return cls(
			cfg=MazeDatasetConfig.load(data["cfg"]),  # type: ignore[arg-type]
			generation_metadata_collected=data["generation_metadata_collected"],  # type: ignore[arg-type]
			mazes=[
				SolvedMaze(
					clist,
					soln[:slen, ...],
				)
				for clist, slen, soln in zip(
					load_item_recursive(data["maze_connection_lists"], tuple()),
					load_item_recursive(data["maze_solution_lengths"], tuple()),
					load_item_recursive(data["maze_solutions"], tuple()),
					strict=False,
					# load_item_recursive(data["maze_endpoints"], tuple()),
				)
			],
		)

	@classmethod
	def _load_minimal_soln_cat(cls, data: JSONdict) -> "MazeDataset":
		assert data[_FORMAT_KEY] == "MazeDataset:minimal_soln_cat"

		maze_solution_lengths = load_item_recursive(
			data["maze_solution_lengths"],
			tuple(),
		)
		maze_solutions_concat = load_item_recursive(
			data["maze_solutions_concat"],
			tuple(),
		)
		maze_solutions = np.split(
			maze_solutions_concat,
			np.cumsum(maze_solution_lengths)[:-1],
			axis=0,
		)

		return cls(
			cfg=load_item_recursive(data["cfg"], tuple()),
			generation_metadata_collected=load_item_recursive(
				data["generation_metadata_collected"],
				tuple(),
			),
			mazes=[
				SolvedMaze(
					connection_list=clist,
					solution=soln,
				)
				for clist, soln in zip(
					load_item_recursive(data["maze_connection_lists"], tuple()),
					# load_item_recursive(data["maze_endpoints"], tuple()),
					maze_solutions,
					strict=False,
				)
			],
		)

	@classmethod
	def _load_legacy(cls, data: JSONdict) -> "MazeDataset":
		"""Legacy `load` method from <0.5.2. Used exclusively for profiling comparison."""
		assert data[_FORMAT_KEY] == "MazeDataset"
		return cls(
			**{
				key: load_item_recursive(data[key], tuple())
				for key in ["cfg", "mazes", "generation_metadata_collected"]
			},
		)

	def serialize(self) -> JSONdict:
		"""serialize to zanj/json"""
		if (
			SERIALIZE_MINIMAL_THRESHOLD is not None
			and len(self) >= SERIALIZE_MINIMAL_THRESHOLD
		):
			return self._serialize_minimal()
		return self._serialize_full()

	def _serialize_full(self) -> JSONdict:
		return {
			_FORMAT_KEY: "MazeDataset",
			"cfg": json_serialize(self.cfg),
			"mazes": json_serialize(self.mazes),
			"generation_metadata_collected": json_serialize(
				self.generation_metadata_collected,
			),
		}

	def _serialize_minimal(self) -> JSONdict:
		"alternate serialization where metadata is collected and mazes are stored in concatenated form"
		filtered_meta: MazeDataset
		if self.generation_metadata_collected is None:
			filtered_meta = self.filter_by.collect_generation_meta()
		else:
			filtered_meta = self

		max_solution_len: int = max(m.solution.shape[0] for m in filtered_meta.mazes)
		n_mazes: int = len(filtered_meta.mazes)
		grid_n: int = filtered_meta.cfg.grid_n

		maze_connection_lists: np.ndarray = np.empty(
			(n_mazes, 2, grid_n, grid_n),
			dtype=np.bool_,
		)
		# maze_endpoints: np.ndarray = np.empty((n_mazes, 2, 2), dtype=np.int8)
		maze_solution_lengths: np.ndarray = np.empty((n_mazes,), dtype=np.int32)
		maze_solutions: np.ndarray = np.empty(
			(n_mazes, max_solution_len, 2),
			dtype=np.int8,
		)

		for idx, maze in enumerate(filtered_meta.mazes):
			maze_connection_lists[idx] = maze.connection_list
			# maze_endpoints[idx] = np.array([maze.start_pos, maze.end_pos])
			maze_solution_lengths[idx] = maze.solution.shape[0]
			maze_solutions[idx, : maze.solution.shape[0]] = maze.solution

		return {
			_FORMAT_KEY: "MazeDataset:minimal",
			"cfg": json_serialize(filtered_meta.cfg),
			"generation_metadata_collected": json_serialize(
				filtered_meta.generation_metadata_collected,
			),
			"maze_connection_lists": maze_connection_lists,  # type: ignore[dict-item]
			# "maze_endpoints": maze_endpoints,
			"maze_solution_lengths": maze_solution_lengths,  # type: ignore[dict-item]
			"maze_solutions": maze_solutions,  # type: ignore[dict-item]
		}

	def _serialize_minimal_soln_cat(self) -> JSONdict:
		"alternate serialization where metadata is collected, and mazes and their solutions are stored in concatenated form"
		if self.generation_metadata_collected is None:
			filtered_meta = self.filter_by.collect_generation_meta()
		else:
			filtered_meta = self

		maze_solution_lengths: np.ndarray = np.array(
			[m.solution.shape[0] for m in filtered_meta.mazes],
			dtype=np.int32,
		)
		n_mazes: int = len(filtered_meta.mazes)
		grid_n: int = filtered_meta.cfg.grid_n
		total_solution_len: int = np.sum(maze_solution_lengths)

		maze_connection_lists: np.ndarray = np.empty(
			(n_mazes, 2, grid_n, grid_n),
			dtype=np.bool_,
		)
		maze_endpoints: np.ndarray = np.empty((n_mazes, 2, 2), dtype=np.int8)
		maze_solutions_concat: np.ndarray = np.empty(
			(total_solution_len, 2),
			dtype=np.int8,
		)

		solutions_running_idx: int = 0
		for idx, maze in enumerate(filtered_meta.mazes):
			maze_connection_lists[idx] = maze.connection_list
			maze_endpoints[idx] = np.array([maze.start_pos, maze.end_pos])
			soln_len: int = maze.solution.shape[0]
			maze_solution_lengths[idx] = soln_len
			maze_solutions_concat[
				solutions_running_idx : solutions_running_idx + soln_len
			] = maze.solution
			solutions_running_idx += soln_len

		return {
			_FORMAT_KEY: "MazeDataset:minimal_soln_cat",
			"cfg": json_serialize(filtered_meta.cfg),
			"generation_metadata_collected": json_serialize(
				filtered_meta.generation_metadata_collected,
			),
			"maze_connection_lists": maze_connection_lists,  # type: ignore[dict-item]
			"maze_endpoints": maze_endpoints,  # type: ignore[dict-item]
			"maze_solution_lengths": maze_solution_lengths,  # type: ignore[dict-item]
			"maze_solutions_concat": maze_solutions_concat,  # type: ignore[dict-item]
		}

	def update_self_config(self) -> None:
		"""update the config to match the current state of the dataset (number of mazes, such as after filtering)"""
		self.cfg.n_mazes = len(self.mazes)

	def custom_maze_filter(
		self,
		method: typing.Callable[[SolvedMaze], bool],
		**kwargs,
	) -> "MazeDataset":
		"""filter the dataset using a custom method"""
		output: MazeDataset = MazeDataset(
			cfg=copy.deepcopy(self.cfg),
			mazes=[m for m in self.mazes if method(m, **kwargs)],
		)
		output.cfg.applied_filters.append(
			{
				"name": f"__custom__:{method.__name__}",
				"kwargs": kwargs,
			},
		)
		output.update_self_config()
		return output


# register things with zanj
MazeDatasetConfig._dataset_class = property(  # type: ignore[method-assign]
	lambda self: MazeDataset,  # noqa: ARG005
)
register_loader_handler(
	LoaderHandler(
		check=lambda json_item, path=None, z=None: (  # noqa: ARG005
			isinstance(json_item, typing.Mapping)
			and _FORMAT_KEY in json_item
			and json_item[_FORMAT_KEY].startswith("MazeDataset")
		),
		load=lambda json_item, path=None, z=None: MazeDataset.load(json_item),  # noqa: ARG005
		uid="MazeDataset",
		source_pckg="maze_dataset.generation.maze_dataset",
		desc="MazeDataset",
	),
)


def register_maze_filter(
	method: typing.Callable[[SolvedMaze, typing.Any], bool],
) -> DatasetFilterProtocol:
	"""register a maze filter, casting it to operate over the whole list of mazes

	method should be a staticmethod of a namespace class registered with `register_filter_namespace_for_dataset`

	this is a more restricted version of `register_dataset_filter` that removes the need for boilerplate for operating over the arrays
	"""

	@functools.wraps(method)
	def wrapper(dataset: MazeDataset, *args, **kwargs) -> MazeDataset:
		# copy and filter
		new_dataset: MazeDataset = copy.deepcopy(
			MazeDataset(
				cfg=dataset.cfg,
				mazes=[m for m in dataset.mazes if method(m, *args, **kwargs)],
			),
		)
		# update the config
		new_dataset.cfg.applied_filters.append(
			dict(name=method.__name__, args=args, kwargs=kwargs),
		)
		new_dataset.update_self_config()
		return new_dataset

	return wrapper


@register_filter_namespace_for_dataset(MazeDataset)
class MazeDatasetFilters:
	"namespace for filters for `MazeDataset`s"

	@register_maze_filter
	@staticmethod
	def path_length(maze: SolvedMaze, min_length: int) -> bool:
		"""filter out mazes with a solution length less than `min_length`"""
		return len(maze.solution) >= min_length

	@register_maze_filter
	@staticmethod
	def start_end_distance(maze: SolvedMaze, min_distance: int) -> bool:
		"""filter out datasets where the start and end pos are less than `min_distance` apart on the manhattan distance (ignoring walls)"""
		return np.linalg.norm(maze.start_pos - maze.end_pos, 1) >= min_distance

	@register_dataset_filter
	@staticmethod
	def cut_percentile_shortest(
		dataset: MazeDataset,
		percentile: float = 10.0,
	) -> MazeDataset:
		"""cut the shortest `percentile` of mazes from the dataset

		`percentile` is 1-100, not 0-1, as this is what `np.percentile` expects
		"""
		lengths: np.ndarray = np.array([len(m.solution) for m in dataset])
		cutoff: int = int(np.percentile(lengths, percentile))

		filtered_mazes: list[SolvedMaze] = [
			m for m in dataset if len(m.solution) > cutoff
		]
		new_dataset: MazeDataset = MazeDataset(cfg=dataset.cfg, mazes=filtered_mazes)

		return copy.deepcopy(new_dataset)

	@register_dataset_filter
	@staticmethod
	def truncate_count(
		dataset: MazeDataset,
		max_count: int,
	) -> MazeDataset:
		"""truncate the dataset to be at most `max_count` mazes"""
		new_dataset: MazeDataset = MazeDataset(
			cfg=dataset.cfg,
			mazes=dataset.mazes[:max_count],
		)
		return copy.deepcopy(new_dataset)

	@register_dataset_filter
	@staticmethod
	def remove_duplicates(
		dataset: MazeDataset,
		minimum_difference_connection_list: int | None = 1,
		minimum_difference_solution: int | None = 1,
		_max_dataset_len_threshold: int = 1000,
	) -> MazeDataset:
		"""remove duplicates from a dataset, keeping the **LAST** unique maze

		set minimum either minimum difference to `None` to disable checking

		if you want to avoid mazes which have more overlap, set the minimum difference to be greater

		Gotchas:
		- if two mazes are of different sizes, they will never be considered duplicates
		- if two solutions are of different lengths, they will never be considered duplicates

		TODO: check for overlap?
		"""
		if len(dataset) > _max_dataset_len_threshold:
			raise ValueError(
				"this method is currently very slow for large datasets, consider using `remove_duplicates_fast` instead\n",
				"if you know what you're doing, change `_max_dataset_len_threshold`",
			)

		unique_mazes: list[SolvedMaze] = list()

		maze_a: SolvedMaze
		maze_b: SolvedMaze
		for i, maze_a in enumerate(dataset.mazes):
			a_unique: bool = True
			for maze_b in dataset.mazes[i + 1 :]:
				# after all that nesting, more nesting to perform checks
				if (minimum_difference_connection_list is not None) and (  # noqa: SIM102
					maze_a.connection_list.shape == maze_b.connection_list.shape
				):
					if (
						np.sum(maze_a.connection_list != maze_b.connection_list)
						<= minimum_difference_connection_list
					):
						a_unique = False
						break

				if (minimum_difference_solution is not None) and (  # noqa: SIM102
					maze_a.solution.shape == maze_b.solution.shape
				):
					if (
						np.sum(maze_a.solution != maze_b.solution)
						<= minimum_difference_solution
					):
						a_unique = False
						break

			if a_unique:
				unique_mazes.append(maze_a)

		return copy.deepcopy(
			MazeDataset(
				cfg=dataset.cfg,
				mazes=unique_mazes,
				generation_metadata_collected=dataset.generation_metadata_collected,
			),
		)

	@register_dataset_filter
	@staticmethod
	def remove_duplicates_fast(dataset: MazeDataset) -> MazeDataset:
		"""remove duplicates from a dataset"""
		unique_mazes = list(dict.fromkeys(dataset.mazes))
		return copy.deepcopy(
			MazeDataset(
				cfg=dataset.cfg,
				mazes=unique_mazes,
				generation_metadata_collected=dataset.generation_metadata_collected,
			),
		)

	@register_dataset_filter
	@staticmethod
	def strip_generation_meta(dataset: MazeDataset) -> MazeDataset:
		"""strip the generation meta from the dataset"""
		new_dataset: MazeDataset = copy.deepcopy(dataset)
		for maze in new_dataset:
			# hacky because it's a frozen dataclass
			maze.__dict__["generation_meta"] = None
		return new_dataset

	@register_dataset_filter
	@staticmethod
	# yes, this function is complicated hence the noqa
	def collect_generation_meta(  # noqa: C901, PLR0912
		dataset: MazeDataset,
		clear_in_mazes: bool = True,
		inplace: bool = True,
		allow_fail: bool = False,
	) -> MazeDataset:
		"""collect the generation metadata from each maze into a dataset-level metadata (saves space)

		# Parameters:
		- `dataset : MazeDataset`
		- `clear_in_mazes : bool`
			whether to clear the generation meta in the mazes after collecting it, keep it there if `False`
			(defaults to `True`)
		- `inplace : bool`
			whether to modify the dataset in place or return a new one
			(defaults to `True`)
		- `allow_fail : bool`
			whether to allow the collection to fail if the generation meta is not present in a maze
			(defaults to `False`)

		# Returns:
		- `MazeDataset`
			the dataset with the generation metadata collected

		# Raises:
		- `ValueError` : if the generation meta is not present in a maze and `allow_fail` is `False`
		- `ValueError` : if we have other problems converting the generation metadata
		- `TypeError` : if the generation meta on a maze is of an unexpected type
		"""
		if dataset.generation_metadata_collected is not None:
			return dataset
		else:
			assert dataset[0].generation_meta is not None, (
				"generation meta is not collected and original is not present"
			)
		# if the generation meta is already collected, don't collect it again, do nothing

		new_dataset: MazeDataset
		if inplace:
			new_dataset = dataset
		else:
			new_dataset = copy.deepcopy(dataset)

		gen_meta_lists: dict[bool | int | float | str | CoordTup, Counter] = (
			defaultdict(Counter)
		)
		for maze in new_dataset:
			if maze.generation_meta is None:
				if allow_fail:
					break
				raise ValueError(
					"generation meta is not present in a maze, cannot collect generation meta",
				)
			for key, value in maze.generation_meta.items():
				if isinstance(value, (bool, int, float, str)):  # noqa: UP038
					gen_meta_lists[key][value] += 1

				elif isinstance(value, set):
					# special case for visited_cells
					gen_meta_lists[key].update(value)

				elif isinstance(value, (list, np.ndarray)):  # noqa: UP038
					if isinstance(value, list):
						# TODO: `for` loop variable `value` overwritten by assignment target (Ruff PLW2901)
						try:
							value = np.array(value)  # noqa: PLW2901
						except ValueError as convert_to_np_err:
							err_msg: str = (
								f"Cannot collect generation meta for {key} as it is a list of type '{type(value[0]) = !s}'"
								"\nexpected either a basic type (bool, int, float, str), a numpy coord, or a numpy array of coords"
							)
							raise ValueError(err_msg) from convert_to_np_err

					if (len(value.shape) == 1) and (value.shape[0] == maze.lattice_dim):
						# assume its a single coordinate
						gen_meta_lists[key][tuple(value)] += 1
					# magic value is fine here
					elif (len(value.shape) == 2) and (  # noqa: PLR2004
						value.shape[1] == maze.lattice_dim
					):
						# assume its a list of coordinates
						gen_meta_lists[key].update([tuple(v) for v in value])
					else:
						err_msg: str = (
							f"Cannot collect generation meta for {key} as it is an ndarray of shape {value.shape}\n"
							"expected either a coord of shape (2,) or a list of coords of shape (n, 2)"
						)
						raise ValueError(err_msg)
				else:
					err_msg: str = (
						f"Cannot collect generation meta for {key} as it is of type '{type(value)!s}'\n"
						"expected either a basic type (bool, int, float, str), a numpy coord, or a numpy array of coords"
					)
					raise TypeError(err_msg)

			# clear the data
			if clear_in_mazes:
				# hacky because it's a frozen dataclass
				maze.__dict__["generation_meta"] = None

		new_dataset.generation_metadata_collected = {
			key: dict(value) for key, value in gen_meta_lists.items()
		}

		return new_dataset


# the code below is for doing some smarter collecting and type checking. Probably will delete.
"""
collect either the type at the field, or the shape of the field if it is an array
metadata_types: dict[str, set[type, tuple]] = dict()
for maze in new_dataset:
	for key, value in maze.generation_meta.items():
		if key not in metadata_types:
			metadata_types[key] = set()

		if isinstance(value, np.ndarray):
			metadata_types[key].add(value.shape)
		else:
			metadata_types[key].add(type(value))

# figure out what to do for each field
metadata_actions: dict[str, typing.Callable] = dict()
for key, key_type in metadata_types.items():
	if all(isinstance(kt, tuple) for kt in key_type):
		if all(kt == (2,) for kt in key_type):
			# its all coords, do a statcounter on those coords
			metadata_actions[key] = lambda vals: Counter(tuple(x) for x in vals)
		elif all(
			(len(kt) == 2) and (kt[1] == 2)
			for kt in key_type
		):
			# its a list of coords, do a statcounter on those coords
			metadata_actions[key] = lambda vals: Counter(
				tuple(x) for x in np.concatenate(vals)
			)
		else:
			# its a list of something else, do a counter on those
			# TODO: throw except here?
			metadata_actions[key] = Counter

	elif all(kt in (bool, int, float) for kt in key_type):
		# statcounter for numeric types
		metadata_actions[key] = StatCounter
	elif all(kt == str for kt in key_type):
		# counter for string types
		metadata_actions[key] = Counter
	else:
		# counter for everything else
		# TODO: throw except here?
		metadata_actions[key] = Counter
"""
