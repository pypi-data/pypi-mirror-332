from pathlib import Path, PurePosixPath

from fans.logger import get_logger

from eno.convert import to_snippet
from eno.env import env

from .py.loader import Loader


logger = get_logger(__name__)
id_to_context = {}


def call_py(req: dict):
    """
    Call a Python function and using the return value as:
        - raw data
        - snippet (single / multiple)
    """
    logger.info(f'call_py: {req}')
    path = env.root / PurePosixPath(req['path'].lstrip('/'))
    func = req.get('func') or 'main'
    args = req.get('args') or []
    kwargs = req.get('kwargs') or {}
    context = req.get('context')

    if context == 'init':
        get_context(path)
        ret = None
    elif context == 'clear':
        clear_context(path)
        ret = None
    elif context is True:
        context = get_context(path)
        ret = run_func(path, func, args, kwargs, context = context)
    else:
        ret = run_func(path, func, args, kwargs, eno_path = req.get('eno_path'))

    try:
        if req.get('snippet'):
            return to_snippet(ret)
        else:
            return ret
    except Exception:
        print('call_py', req)
        raise


def run_func(path, funcname, args, kwargs, context = None, eno_path = None):
    logger.info(f'run_func {path}')
    module = Loader().load(path)
    func = getattr(module, funcname, None)
    if func:
        if context is not None:
            kwargs['context'] = context
        if hasattr(module, 'main'):
            main = module.main
            main.cwd = Path(path).parent
            main.eno_path = eno_path
        return func(*args, **kwargs)


def get_context(path):
    if path not in id_to_context:
        id_to_context[path] = {}
    return id_to_context[path]


def clear_context(path):
    if path in id_to_context:
        del id_to_context[path]
