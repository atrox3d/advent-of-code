import importlib
import importlib.util
import sys
import types
from pathlib import Path


def load_module_from_path(
        target_path:str,
        # python_filename:str,
        cache_module:bool=False
) -> types.ModuleType:
    '''dynamically loads a module from path and filename'''

    file_path = Path(target_path)
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    
    # get just the file name without ext
    module_name = file_path.stem

    # add the file path to sys.path, this way the loaded module
    # can import siblings
    sys.path.insert(0, str(file_path.parent))

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)

    if cache_module:
        sys.modules[module_name] = module

    spec.loader.exec_module(module)
    return module


def load_module_from_package(
        modulename:str,
        package:str=None,
        merge:bool=True
) -> types.ModuleType:
    

    if merge:
        if package is not None:
            modulename = f'{package}.{modulename}'
            package = None

    module = importlib.import_module(modulename, package)
    return module
