import pathlib
from collections import namedtuple
from typing import Iterable


def tuple_function(x) -> tuple:
    return tuple(x)

def node_function_factory(node):
    def node_function(x):
        return node(*x)
    return node_function

def container_to_tuple(container):
    if not hasattr(container, "__contains__"):
        raise TypeError
    values = []
    if not hasattr(container, "get"):
        contents = list(container)
        return_func = tuple_function
    else:
        keys = list(container.keys())
        contents = [container[k] for k in keys]
        return_func = node_function_factory(namedtuple("Node", keys))
    for item in contents:
        if not hasattr(item, "__contains__") or hasattr(item, "capitalize"):  # not a container or a string
            values.append(item)
        else:
            values.append(container_to_tuple(item))
    return return_func(values)


def parse_configuration(lines: Iterable[str]):
    result = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", maxsplit=1)
        k, v = k.strip(), v.strip()
        keys = k.split(".")
        r = result
        for i in range(len(keys) - 1):
            if keys[i] not in r:
                r[keys[i]] = {}
            r = r[keys[i]]
        r[keys[-1]] = v

    return container_to_tuple(result)


def get_configuration(path: pathlib.Path):
    """Read PATH and make contents available as (nested) NamedTuple.

    :param path: File with configuration
    """
    with path.open("r") as f:
        return parse_configuration(f.readlines())


