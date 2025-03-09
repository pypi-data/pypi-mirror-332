import pytest

import xoryaml


def test_circular_dict():
    """
    dumps() circular reference dict
    """
    obj = {}  # type: ignore
    obj["obj"] = obj
    with pytest.raises(xoryaml.YAMLEncodeError):
        xoryaml.dumps(obj)


def test_circular_list():
    """
    dumps() circular reference list
    """
    obj = []
    obj.append(obj)
    with pytest.raises(xoryaml.YAMLEncodeError):
        xoryaml.dumps(obj)


def test_circular_nested():
    """
    dumps() circular reference nested dict, list
    """
    obj = {}  # type: ignore
    obj["list"] = [{"obj": obj}]
    with pytest.raises(xoryaml.YAMLEncodeError):
        xoryaml.dumps(obj)
