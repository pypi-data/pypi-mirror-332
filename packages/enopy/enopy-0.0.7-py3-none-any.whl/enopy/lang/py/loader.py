import sys
import time
import runpy
import builtins
import threading
import importlib
import contextlib
from pathlib import Path

from fans.deco import singleton
from fans.logger import get_logger


logger = get_logger(__name__)
# TODO: use a dedicated directory and sym link packages
packages_root = Path('/home/fans656')
if not packages_root.exists():
    packages_root = Path('/root')
lock = threading.RLock()


@singleton
class Loader:

    def __init__(self):
        self.path_to_module = {}

    def load(self, path, sys_paths = None):
        """
        Load a Python module by given path, ensuring up to date depended modules.
        """
        with lock:
            if path not in self.path_to_module:
                self.path_to_module[path] = Module(path, sys_paths = sys_paths)
            module = self.path_to_module.get(path)
            module.refresh()
            return module.module


class Module:

    def __init__(self, path, sys_paths):
        self.path = Path(path).resolve()
        self.sys_paths = [str(packages_root)] + (sys_paths or [])
        self.path_to_imported_module = {}
        self.module = None
        self.mtime = Path(self.path).stat().st_mtime

        with self.collect_imports(), self.modified_sys_path():
            path = self.path.relative_to(packages_root)
            module_name = str(path.with_suffix('')).replace('/', '.')
            self.module = importlib.import_module(module_name)

    def refresh(self):
        logger.info(f'refresh module {self.path} with {len(self.path_to_imported_module)} deps')
        with self.modified_sys_path():
            dirty = self.path.stat().st_mtime > self.mtime
            for path, module_data in self.path_to_imported_module.items():
                module = module_data['module']
                mtime = Path(path).stat().st_mtime
                if mtime > module_data['mtime']:
                    logger.info(f'reload {module}')
                    importlib.reload(module)
                    module_data['mtime'] = time.time()
                    dirty = True
            if dirty:
                with self.collect_imports():
                    importlib.reload(self.module)

    def __import__(self, name, *args, **kwargs):
        module = importlib.__import__(name, *args, **kwargs)
        path = getattr(module, '__file__', None)
        if path:
            self.path_to_imported_module[path] = {'module': module, 'mtime': time.time()}
        return module

    @contextlib.contextmanager
    def collect_imports(self):
        orig__import = builtins.__import__
        try:
            builtins.__import__ = self.__import__
            yield
        finally:
            builtins.__import__ = orig__import

    @contextlib.contextmanager
    def modified_sys_path(self):
        orig_sys_path = list(sys.path)
        try:
            sys.path[:] = list(dict.fromkeys(self.sys_paths + sys.path))
            yield
        finally:
            sys.path = orig_sys_path
