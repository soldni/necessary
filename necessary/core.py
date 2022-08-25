import importlib
from typing import Optional, Union

from packaging.version import LegacyVersion, Version, parse


def necessary(
    module_name: str,
    min_version: Optional[Union[str, Version, LegacyVersion]] = None,
    soft_check: bool = False,
) -> bool:
    """Function to check if a module is installed and optionally check its
    version.

    Args:
        module_name (str): The name of the module to check.
        mim_version (Optional[Union[str, Version, LegacyVersion]]): The version
            of the module to check. If None, the function will not check the
            version.
        soft_check (bool): If True, the function will return False if the
            module is not installed. If False, the function will raise an
            ImportError.

    Returns:
        bool: True if the module is installed and the version is correct;
            False if the module is not installed/version is incorrect and
            `soft` is True.

    Raises:
        ImportError: If the module is not installed and `soft` is False.
    """
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        if soft_check:
            return False
        else:
            raise ImportError(f"{module_name} is required for this module")

    if min_version is not None:
        module_version = parse(module.__version__)

        if not isinstance(min_version, (Version, LegacyVersion)):
            min_version = parse(min_version)

        if min_version > module_version:
            if soft_check:
                return False
            else:
                raise ImportError(
                    f"Version {min_version} is required for module "
                    f"{module}, but you have {module_name} version "
                    f"{module_version}"
                )
    return True
