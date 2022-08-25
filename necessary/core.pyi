from types import ModuleType
from typing import (
    TYPE_CHECKING,
    List,
    Literal,
    NamedTuple,
    Optional,
    Tuple,
    Union,
)

from packaging.version import LegacyVersion, Version
from typing_extensions import TypeAlias

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
        def __bool__(self) -> Literal[True]: ...
