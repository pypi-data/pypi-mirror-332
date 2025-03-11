import pytest

import xoryaml

LOADS_RECURSION_LIMIT = 1024


def test_loads_recursion_partial():
    """
    loads() recursion limit partial
    """
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, "[" * (1024 * 1024))


def test_loads_recursion_valid_limit_array():
    """
    loads() recursion limit at limit array
    """
    n = LOADS_RECURSION_LIMIT + 1
    value = b"[" * n + b"]" * n
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_limit_object():
    """
    loads() recursion limit at limit object
    """
    n = LOADS_RECURSION_LIMIT
    value = b'{"key":' * n + b'{"key":true}' + b"}" * n
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_limit_mixed():
    """
    loads() recursion limit at limit mixed
    """
    n = LOADS_RECURSION_LIMIT
    value = b"[" + b'{"key":' * n + b'{"key":true}' + b"}" * n + b"]"
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_excessive_array():
    """
    loads() recursion limit excessively high value
    """
    n = 10000000
    value = b"[" * n + b"]" * n
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_limit_array_pretty():
    """
    loads() recursion limit at limit array pretty
    """
    n = LOADS_RECURSION_LIMIT + 1
    value = b"[\n  " * n + b"]" * n
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_limit_object_pretty():
    """
    loads() recursion limit at limit object pretty
    """
    n = LOADS_RECURSION_LIMIT
    value = b'{\n  "key":' * n + b'{"key":true}' + b"}" * n
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_limit_mixed_pretty():
    """
    loads() recursion limit at limit mixed pretty
    """
    n = LOADS_RECURSION_LIMIT
    value = b"[\n  " + b'{"key":' * n + b'{"key":true}' + b"}" * n + b"]"
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)


def test_loads_recursion_valid_excessive_array_pretty():
    """
    loads() recursion limit excessively high value pretty
    """
    n = 10000000
    value = b"[\n  " * n + b"]" * n
    pytest.raises(xoryaml.YAMLDecodeError, xoryaml.loads, value)
