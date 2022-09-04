import importlib.metadata
import warnings
from importlib import import_module
from types import ModuleType
from typing import List, NamedTuple, Optional, Tuple, Union

from packaging.version import LegacyVersion, Version, parse

PackageNameType = str
PackageVersionType = Union[None, str, Version, LegacyVersion]
PackageNameAndVersionType = Tuple[PackageNameType, PackageVersionType]
FullSpecType = Union[
    PackageNameType,
    PackageNameAndVersionType,
    List[Union[PackageNameType, PackageNameAndVersionType]],
]


def get_module_version(
    module: ModuleType,
) -> Union[Version, LegacyVersion, None]:
    """Function to get the version of a package installed on the system."""
    try:
        # package has been installed, so it has a version number
        # from pyproject.toml
        raw_module_version = getattr(
            module,
            "__version__",
            importlib.metadata.version(module.__package__ or module.__name__),
        )
        return parse(raw_module_version)
    except Exception as e:
        warnings.warn(
            (
                f"Could not parse version of {module} "
                f"as a valid version number. Error: {e}"
            ),
            UserWarning,
            stacklevel=2,
        )
        return None


class ModuleSpec(NamedTuple):
    module_name: PackageNameType
    module_version: PackageVersionType


class necessary:
    """Check if a module is installed and optionally check its version."""

    def __init__(
        self,
        modules: FullSpecType,
        soft: bool = False,
        message: Optional[str] = None,
    ):
        """
        Args:
            modules (FullSpecType): Either a module name, a tuple
                consisting of (module name, version), or a list containing a
                mix of the two.
            soft (bool): If True, the function will return False if the
                module is not installed. If False, the function will raise an
                ImportError.
            message (Optional[str]): If provided, the function will raise the
                given message. If your message contains "{module_name}" and
                "{module_version}", the function will replace them with the
                their respective values.

        Raises:
            ImportError: If the module is not installed and `soft` is False.
        """
        parsed_modules_spec = self.parse_modules_spec_input(modules)
        self._necessary = all(
            self.check_module_is_available(
                module_spec=module_spec, soft_check=soft, message=message
            )
            for module_spec in parsed_modules_spec
        )

    def parse_modules_spec_input(
        self, modules_spec: FullSpecType
    ) -> List[ModuleSpec]:
        if not isinstance(modules_spec, list):
            modules_spec = [modules_spec]

        parsed_modules_spec: List[ModuleSpec] = []
        for module_spec in modules_spec:
            if isinstance(module_spec, str):
                parsed_modules_spec.append(ModuleSpec(module_spec, None))
            elif isinstance(module_spec, tuple) and len(module_spec) == 2:
                parsed_modules_spec.append(ModuleSpec(*module_spec))
            else:
                raise ValueError(
                    "`modules_spec` must be either a module name, a tuple "
                    "consisting of (module name, version), or a list "
                    f"containing a mix of the two; I could not recognize "
                    f"{repr(modules_spec)} as a valid input."
                )
        return parsed_modules_spec

    def check_module_is_available(
        self,
        module_spec: ModuleSpec,
        soft_check: bool = False,
        message: Optional[str] = None,
    ) -> bool:

        # this is the message to raise in case of failure and if no custom
        # message is provided by the user.
        if message is None:
            message = "'{module_name}' is required, please install it."
            if module_spec.module_version is not None:
                message = "version '{module_version}' of " + message

        # fist check is to see if we can import the module.
        try:
            module = import_module(module_spec.module_name)
        except ModuleNotFoundError:
            if soft_check:
                return False
            else:
                raise ImportError(message.format(**module_spec._asdict()))

        # then let's check if a minimum version is specified and if so,
        # check it.
        if module_spec.module_version is not None:
            module_version = get_module_version(module)

            if module_version is None:
                return True

            if not isinstance(
                module_spec.module_version, (Version, LegacyVersion)
            ):
                requested_version = parse(module_spec.module_version)
            else:
                requested_version = module_spec.module_version

            if requested_version > module_version:
                if soft_check:
                    return False
                else:
                    raise ImportError(message.format(**module_spec._asdict()))
        return True

    def __bool__(self) -> bool:
        return self._necessary

    def __enter__(self) -> "necessary":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass
