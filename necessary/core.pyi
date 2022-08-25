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

def _parse_spec_input(modules_spec: FullSpecType) -> List[ModuleSpec]: ...
def get_module_version(
    module: ModuleType,
) -> Union[Version, LegacyVersion, None]: ...
def _necessary_one(
    module_spec: ModuleSpec,
    soft_check: bool = ...,
    message: Optional[str] = ...,
) -> bool: ...

if TYPE_CHECKING:  # noqa: Y002
    def necessary(
        modules_spec: FullSpecType,
        soft_check: bool = ...,
        message: Optional[str] = ...,
    ) -> Literal[True]: ...

else:
    def necessary(
        modules_spec: FullSpecType,
        soft_check: bool = ...,
        message: Optional[str] = ...,
    ) -> bool: ...
