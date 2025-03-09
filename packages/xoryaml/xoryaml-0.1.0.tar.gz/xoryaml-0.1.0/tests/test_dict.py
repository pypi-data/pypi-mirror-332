# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import pytest

import xoryaml


def test_dict():
    """
    dict
    """
    obj = {"key": "value"}
    ref = "---\nkey: value"
    assert xoryaml.dumps(obj) == ref
    assert xoryaml.loads(ref) == obj


def test_dict_empty():
    obj = [{"key": [{}] * 4096}] * 4096
    dumped = xoryaml.dumps(obj)
    assert dumped
    assert xoryaml.loads(dumped) == obj


def test_dict_large_dict():
    """
    dict with >512 keys
    """
    obj = {"key_%s" % idx: [{}, {"a": [{}, {}, {}]}, {}] for idx in range(513)}
    assert len(obj) == 513
    dumped = xoryaml.dumps(obj)
    assert dumped
    assert xoryaml.loads(dumped) == obj


def test_dict_large_4096():
    """
    dict with >4096 keys
    """
    obj = {"key_%s" % idx: "value_%s" % idx for idx in range(4097)}
    assert len(obj) == 4097
    dumped = xoryaml.dumps(obj)
    assert dumped
    assert xoryaml.loads(dumped) == obj


def test_dict_large_65536():
    """
    dict with >65536 keys
    """
    obj = {"key_%s" % idx: "value_%s" % idx for idx in range(65537)}
    assert len(obj) == 65537
    dumped = xoryaml.dumps(obj)
    assert dumped
    assert xoryaml.loads(dumped) == obj


def test_dict_large_keys():
    """
    dict with keys too large to cache
    """
    obj = {"keeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey": "value"}
    ref = (
        "---\nkeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey: value"
    )
    assert xoryaml.dumps(obj) == ref
    assert xoryaml.loads(ref) == obj


def test_dict_unicode_key():
    """
    dict unicode keys
    """
    obj = {"🐈": "value"}
    ref = "---\n🐈: value"
    assert xoryaml.dumps(obj) == ref
    assert xoryaml.loads(ref) == obj
    assert xoryaml.loads(ref)["🐈"] == "value"


def test_dict_numeric_key():
    """
    dict invalid key dumps()
    """
    obj = {1: "value"}
    ref = "---\n1: value"
    assert xoryaml.dumps(obj) == ref
    assert xoryaml.loads(ref) == obj
    assert xoryaml.loads(ref)[1] == "value"


def test_dict_invalid_key_dumps():
    """
    dict invalid key dumps()
    """
    with pytest.raises(xoryaml.YAMLEncodeError):
        xoryaml.dumps({b"key": "value"})


def test_dict_invalid_key_loads():
    """
    dict invalid key loads()
    """
    with pytest.raises(xoryaml.YAMLDecodeError):
        xoryaml.loads('{{"a":true}:true}')
