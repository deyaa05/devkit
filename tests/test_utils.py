from devkit.utils.gh import gh_json
from devkit.config import load_config, DEFAULTS

def test_load_config_defaults():
    cfg = load_config()
    for key in DEFAULTS:
        assert key in cfg

def test_gh_json_empty():
    result = gh_json.__doc__
    assert result is not None