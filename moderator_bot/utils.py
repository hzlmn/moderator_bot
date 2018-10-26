from pathlib import Path

import yaml


def load_config(path):
    with Path(path).open() as fp:
        return yaml.load(fp.read())
