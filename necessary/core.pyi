from typing import TYPE_CHECKING, Literal, Optional, Union

from packaging.version import LegacyVersion, Version

if TYPE_CHECKING:
    def necessary(
        module_name: str,
        min_version: Optional[Union[str, Version, LegacyVersion]] = None,
        soft_check: bool = False,
    ) -> Literal[True]: ...

else:
    def necessary(
        module_name: str,
        min_version: Optional[Union[str, Version, LegacyVersion]] = None,
        soft_check: bool = False,
    ) -> bool: ...
