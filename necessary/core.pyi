from typing import Literal, Optional, Union, TYPE_CHECKING

from packaging.version import LegacyVersion, Version


if TYPE_CHECKING:
    def necessary(
        module_name: str,
        min_version: Optional[Union[str, Version, LegacyVersion]] = None,
        soft_check: bool = False
    ) -> Literal[True]:
        ...
else:
    def necessary(
        module_name: str,
        min_version: Optional[Union[str, Version, LegacyVersion]] = None,
        soft_check: bool = False
    ) -> bool:
        ...
