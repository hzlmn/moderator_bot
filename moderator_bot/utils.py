from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import yaml
from aiotools import async_ctx_manager


def load_config(path):
    with Path(path).open() as fp:
        return yaml.load(fp.read())


@async_ctx_manager
async def setup_executor(workers_count):
    executor = ProcessPoolExecutor(max_workers=workers_count)
    yield executor
    executor.shutdown(wait=True)
