from collections import namedtuple

import pytest

import xoryaml

ORDERED_SEQUENCE_TYPES = ([1, 2], (1, 2), namedtuple("t", ["one", "two"])(1, 2))
UNOEDERED_SEQUENCE_TYPES = ({1, 2}, frozenset((1, 2)))


@pytest.mark.parametrize("obj", ORDERED_SEQUENCE_TYPES, ids=repr)
def test_ordereed_round_trip(obj):
    dumped = xoryaml.dumps(obj)
    assert dumped
    assert xoryaml.loads(dumped) == [1, 2]


@pytest.mark.parametrize("obj", UNOEDERED_SEQUENCE_TYPES, ids=repr)
def test_unordered_round_trip(obj):
    dumped = xoryaml.dumps(obj)
    assert dumped
    assert set(xoryaml.loads(dumped)) == {1, 2}
