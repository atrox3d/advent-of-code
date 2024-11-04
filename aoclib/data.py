from pathlib import Path
import types

def get_inputpath(
        module:types.ModuleType,
        inputpath:str=None,
        suffix='txt'
) -> str:
    if inputpath is None:
        inputpath = Path(module.__file__).with_suffix(f'.{suffix}')
    return inputpath