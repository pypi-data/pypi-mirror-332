import re

import toml
from dotenv import dotenv_values


decoder = toml.TomlDecoder()

dot_env_values = dotenv_values()
RE_ENV_VAR = r"\$([A-Z_][A-Z0-9_]+)"


def env_replace(x, fail_on_missing=True):
    env_var = x.groups()[0]
    print(f"env_var: {env_var}")
    if fail_on_missing:
        p = dot_env_values.get(env_var)
        if not p:
            raise ValueError(f"{env_var} not found in environment.")
    else:
        p = dot_env_values.get(env_var, "")
    return p


def process(item, fail_on_missing=True):
    iter_ = None
    if isinstance(item, dict):
        iter_ = item.items()
    elif isinstance(item, list):
        iter_ = enumerate(item)

    def _env_replace(x):
        return env_replace(x, fail_on_missing)

    for i, val in iter_:
        if isinstance(val, (dict, list)):
            process(val)
        elif isinstance(val, str):
            if re.match(RE_ENV_VAR, val):
                r = re.sub(RE_ENV_VAR, _env_replace, val)

                # Try to first load the value from the environment variable
                # (i.e. make what seems like a float a float, what seems like a
                item[i], _ = decoder.load_value('"{}"'.format(r))


def toml_load(*args, **kwargs):
    data = toml.load(*args, **kwargs)
    process(data)
    return data


def toml_loads(*args, **kwargs):
    data = toml.loads(*args, **kwargs)
    process(data)
    return data
