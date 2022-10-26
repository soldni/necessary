from types import ModuleType
from typing import (
    TYPE_CHECKING,
    Callable,
    Generic,
    List,
    Literal,
    NamedTuple,
    Optional,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from packaging.version import LegacyVersion, Version
from typing_extensions import ParamSpec, TypeAlias

PackageNameType: TypeAlias = str
PackageVersionType: TypeAlias = Union[str, Version, LegacyVersion]
PackageNameAndVersionType: TypeAlias = Tuple[
    PackageNameType, PackageVersionType
]
FullSpecType: TypeAlias = Union[
    PackageNameType,
    PackageNameAndVersionType,
    List[Union[PackageNameType, PackageNameAndVersionType]],
]

class ModuleSpec(NamedTuple):
    module_name: PackageNameType
    module_version: PackageVersionType

def get_module_version(
    module: ModuleType,
) -> Union[Version, LegacyVersion, None]: ...

class necessary:
    def __init__(
        self,
        modules: FullSpecType,
        soft: bool = ...,
        message: Optional[str] = ...,
    ): ...
    def parse_modules_spec_input(
        self, modules_spec: FullSpecType
    ) -> List[ModuleSpec]: ...
    def check_module_is_available(
        self,
        module_spec: ModuleSpec,
        soft_check: bool = ...,
        message: Optional[str] = ...,
    ) -> bool: ...
    def __enter__(self) -> "necessary": ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

    if TYPE_CHECKING:  # noqa: Y002
        def __bool__(self) -> Literal[True]: ...
    else:
        def __bool__(self) -> bool: ...

# this is internal type in NecessaryCls
_T_INT = TypeVar("_T_INT")
# this is for the parameters for callable that produces _T_INT
_P_INT = ParamSpec("_P_INT")

# this is to bind the type of the class/method to decorate
# to the NecessaryCls type above
_T_EXT = TypeVar("_T_EXT")

@overload
class NecessaryCls(Generic[_P_INT, _T_INT]):
    def __init__(
        self,
        decorated: Callable[_P_INT, _T_INT],
        modules: FullSpecType,
        soft: bool = ...,
        message: Optional[str] = ...,
    ): ...
    def __call__(
        self, *args: _P_INT.args, **kwargs: _P_INT.kwargs
    ) -> _T_INT: ...
    @classmethod
    def decorate(
        cls,
        modules: FullSpecType,
        soft: bool = ...,
        message: Optional[str] = ...,
    ) -> Callable[[_T_EXT], _T_EXT]: ...
