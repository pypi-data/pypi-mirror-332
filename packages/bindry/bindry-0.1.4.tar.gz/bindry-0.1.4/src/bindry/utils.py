import importlib
from typing import Type

from .exceptions import DependencyInjectionException


def locate(class_path: str) -> Type:
    """Dynamically import a class from a module path."""
    if not class_path or not isinstance(class_path, str):
        raise DependencyInjectionException(f"Invalid class path: {class_path}")

    try:
        # Validate class path format
        if ".." in class_path or class_path.startswith(".") or class_path.endswith("."):
            raise DependencyInjectionException(
                f"Invalid class path format: {class_path}"
            )

        # Split the class path into module path and class name.
        try:
            module_path, class_name = class_path.rsplit(".", 1)
        except ValueError:
            # Handle builtin types if no dot is present
            if isinstance(__builtins__, dict):
                builtin = __builtins__.get(class_path)
            else:
                builtin = getattr(__builtins__, class_path, None)
            if builtin is not None:
                return builtin
            raise DependencyInjectionException(f"Invalid class path: {class_path}")

        # Import the module that directly contains the class.
        module = importlib.import_module(module_path)
        # Retrieve the class from the module.
        return getattr(module, class_name)

    except ImportError as e:
        raise ImportError(f"Could not locate class '{class_path}': {str(e)}")
    except AttributeError as e:
        raise ImportError(f"Could not locate class '{class_path}': {str(e)}")
    except Exception as e:
        raise DependencyInjectionException(
            f"Invalid class path format '{class_path}': {str(e)}"
        )
