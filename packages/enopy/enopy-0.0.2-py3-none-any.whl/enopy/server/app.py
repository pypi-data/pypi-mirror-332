import traceback
import os

from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from fans.logger import get_logger
from fans.path import Path

from eno.parse import parse_eno


logger = get_logger(__name__)


app = FastAPI(
    title = 'eno',
    description = 'eno server',
    version = '1.0.0',
    docs_url = None,
    redoc_url = '/api/',
    openapi_url = '/api/openapi.json',
)


@app.on_event('startup')
def on_startup():
    pass


@app.on_event('shutdown')
def on_shutdown():
    pass


@app.post('/api/get-eno')
def get_eno(data: dict):
    path = data['path']

    root_dir = Path(os.environ.get('ENOS') or '/enos')
    if path:
        eno_path = get_eno_fpath(path)
        if not eno_path:
            raise HTTPException(404, 'no eno found')
        with eno_path.open() as f:
            text = f.read()
        eno = parse_eno(text, eno_path.parent)
        return eno
    else:
        return [str(d) for d in root_dir.iterdir()]


@app.post('/api/parse-eno')
def get_eno(data: dict):
    eno = parse_eno(data['text'], Path(data['path']).parent)
    return eno


@app.get('/{path:path}')
def fallback(path):
    if path.endswith('.js'):
        return FileResponse(f'frontend/dist/{path}')
    return FileResponse('frontend/dist/index.html')


def get_eno_fpath(rel_path):
    root_dir = Path(os.environ.get('ENOS') or '/enos')
    eno_path = root_dir / rel_path.lstrip('/')
    for suffix in [eno_path.suffix, '.eno', '.js', '.py']:
        if eno_path.with_suffix(suffix).exists():
            return eno_path.with_suffix(suffix)
