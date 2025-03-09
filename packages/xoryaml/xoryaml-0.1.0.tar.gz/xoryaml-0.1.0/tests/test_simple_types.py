import inspect
import json

import pytest

import xoryaml

SIMPLE_TYPES = (1, 1.0, -1, None, "my_str", True, False)


def test_loads_trailing():
    """
    loads() handles trailing whitespace
    """
    assert xoryaml.loads("{}\n\t ") == {}


def test_loads_trailing_invalid():
    """
    loads() handles trailing invalid
    """
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, "{}\n\t a")


@pytest.mark.parametrize("obj", SIMPLE_TYPES, ids=repr)
def test_simple_types(obj):
    """
    loads() equivalent to json on simple types
    """
    test = json.dumps(obj)
    assert json.loads(test) == xoryaml.loads(test)


@pytest.mark.parametrize("obj", SIMPLE_TYPES, ids=repr)
def test_simple_round_trip(obj):
    """
    dumps(), loads() round trip on simple types
    """
    assert xoryaml.loads(xoryaml.dumps(obj)) == obj


@pytest.mark.parametrize("obj", (1, 3.14, [], {}, None), ids=repr)
def test_loads_type(obj):
    """
    loads() invalid type
    """
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, obj)


def test_valueerror():
    """
    xoryaml.YAMLDecodeError is a subclass of ValueError
    """
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, "{")
    pytest.raises(ValueError, xoryaml.loads, "{")


def test_default_empty_kwarg():
    """
    dumps() empty kwarg
    """
    assert xoryaml.dumps(None, **{}) == "---\n~"


def test_loads_signature():
    """
    loads() valid __text_signature__
    """
    assert str(inspect.signature(xoryaml.loads)), "(obj == /)"
    inspect.signature(xoryaml.loads).bind("[]")


def test_dumps_module_str():
    """
    xoryaml.dumps.__module__ is a str
    """
    assert xoryaml.dumps.__module__ == "xoryaml"


def test_loads_module_str():
    """
    xoryaml.loads.__module__ is a str
    """
    assert xoryaml.loads.__module__ == "xoryaml"


def test_bytes_buffer():
    """
    dumps() trigger buffer growing where length is greater than growth
    """
    a = "a" * 900
    b = "b" * 4096
    c = "c" * 4096 * 4096
    output = f"---\n- {a}\n- {b}\n- {c}"
    assert xoryaml.dumps([a, b, c]) == output


def test_dumps_none():
    assert xoryaml.dumps(None) == "---\n~"


def test_dumps_key():
    assert xoryaml.dumps({"key": None}) == "---\nkey: ~"


def test_dumps_key_value():
    assert xoryaml.dumps({"key": 4}) == "---\nkey: 4"


def test_dumps_key_sequence():
    assert xoryaml.dumps({"key": [4, 5]}) == "---\nkey:\n  - 4\n  - 5"


def test_loads_key():
    data = """
    key:
    """
    assert xoryaml.loads(data) == {"key": None}


def test_loads_key_value():
    data = """
    key:
        4
    """
    assert xoryaml.loads(data) == {"key": 4}


def test_loads_key_sequence():
    data = """
    key:
        - 4
        - 5
    """
    assert xoryaml.loads(data) == {"key": [4, 5]}


def test_loads_bytes_empty():
    data = b""
    assert xoryaml.loads(data) is None


def test_loads_bytes_key():
    data = b"""
    key:
    """
    assert xoryaml.loads(data) == {"key": None}


def test_loads_bytes_key_value():
    data = b"""
    key:
        4
    """
    assert xoryaml.loads(data) == {"key": 4}


def test_loads_bytes_key_sequence():
    data = b"""
    key:
        - 4
        - 5
    """
    assert xoryaml.loads(data) == {"key": [4, 5]}
