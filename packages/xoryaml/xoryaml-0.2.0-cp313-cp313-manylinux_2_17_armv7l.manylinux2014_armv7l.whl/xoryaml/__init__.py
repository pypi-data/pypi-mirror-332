import typing

from .xoryaml import YAMLDecodeError, YAMLEncodeError
from .xoryaml import dumps as _dumps
from .xoryaml import loads_all as _loads_all


def dumps(obj: typing.Any, /) -> typing.Optional[str]:
    return _dumps(obj)


def loads_all(obj: typing.AnyStr, /) -> list[typing.Any]:
    if isinstance(obj, bytes):
        return _loads_all(obj.decode())
    elif isinstance(obj, str):
        return _loads_all(obj)
    raise YAMLDecodeError(obj)


def loads(obj: typing.AnyStr, /) -> typing.Any:
    result = loads_all(obj)
    if result:
        return result[0]


__all__ = ["YAMLDecodeError", "YAMLEncodeError", "dumps", "loads", "loads_all"]
