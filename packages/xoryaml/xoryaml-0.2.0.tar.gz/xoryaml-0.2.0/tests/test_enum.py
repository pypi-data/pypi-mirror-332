import enum

import xoryaml


class StrEnum(str, enum.Enum):
    AAA = "aaa"


class IntEnum(int, enum.Enum):
    ONE = 1


class IntEnumEnum(enum.IntEnum):
    ONE = 1


class IntFlagEnum(enum.IntFlag):
    ONE = 1


class AutoEnum(enum.auto):
    A = "a"


class FloatEnum(float, enum.Enum):
    ONE = 1.1


def test_int_enum():
    dumped = xoryaml.dumps(IntEnum.ONE)
    assert dumped == "---\n1"


def test_intenum_enum():
    dumped = xoryaml.dumps(IntEnumEnum.ONE)
    assert dumped == "---\n1"


def test_intflag_enum():
    dumped = xoryaml.dumps(IntFlagEnum.ONE)
    assert dumped == "---\n1"


def test_auto_enum():
    dumped = xoryaml.dumps(AutoEnum.A)
    assert dumped == "---\na"


def test_float_enum():
    dumped = xoryaml.dumps(FloatEnum.ONE)
    assert dumped == "---\n1.1"


def test_str_enum():
    dumped = xoryaml.dumps(StrEnum.AAA)
    assert dumped == "---\naaa"


def test_non_str_keys_enum():
    dumped = xoryaml.dumps({StrEnum.AAA: 1})
    assert dumped == "---\naaa: 1"
    dumped = xoryaml.dumps({IntEnum.ONE: 1})
    assert dumped == "---\n1: 1"
