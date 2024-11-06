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
    print(f'{file_path = }')
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    module_name = file_path.stem
    print(f'{module_name = }')

    sys.path.insert(0, str(file_path.parent))

    # logger.debug(f'loading module file: {file_path}')
    spec = importlib.util.spec_from_file_location(module_name, file_path)

    # logger.debug(f'creating module fromo spec: {spec}')
    module = importlib.util.module_from_spec(spec)

    if cache_module:
        sys.modules[module_name] = module

    # logger.debug(f'executing module: {module}')
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
