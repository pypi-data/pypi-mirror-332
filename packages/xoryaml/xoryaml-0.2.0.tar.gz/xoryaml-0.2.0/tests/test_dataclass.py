# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import abc
import uuid
from dataclasses import InitVar, dataclass, field
from enum import Enum
from typing import ClassVar, Dict, Optional

import pytest

import xoryaml


class AnEnum(Enum):
    ONE = 1
    TWO = 2


@dataclass
class EmptyDataclass:
    pass


@dataclass
class EmptyDataclassSlots:
    __slots__ = ()


@dataclass
class Dataclass1:
    name: str
    number: int
    sub: Optional["Dataclass1"]


@dataclass
class Dataclass2:
    name: Optional[str] = field(default="?")


@dataclass
class Dataclass3:
    a: str
    b: int
    c: dict
    d: bool
    e: float
    f: list
    g: tuple


@dataclass
class Dataclass4:
    a: str = field()
    b: int = field(metadata={"unrelated": False})
    c: float = 1.1


@dataclass
class Datasubclass(Dataclass1):
    additional: bool


@dataclass
class Slotsdataclass:
    __slots__ = ("a", "b", "_c", "d")
    a: str
    b: int
    _c: str
    d: InitVar[str]
    cls_var: ClassVar[str] = "cls"


@dataclass
class Defaultdataclass:
    a: uuid.UUID
    b: AnEnum


@dataclass
class UnsortedDataclass:
    c: int
    b: int
    a: int
    d: Optional[Dict]


@dataclass
class InitDataclass:
    a: InitVar[str]
    b: InitVar[str]
    cls_var: ClassVar[str] = "cls"
    ab: str = ""

    def __post_init__(self, a: str, b: str):
        self._other = 1
        self.ab = f"{a} {b}"


class AbstractBase(abc.ABC):
    @abc.abstractmethod
    def key(self):
        raise NotImplementedError


def test_dataclass():
    """
    dumps() dataclass
    """
    obj = Dataclass1("a", 1, None)
    assert xoryaml.dumps(obj) == "---\nname: a\nnumber: 1\nsub: ~"


def test_dataclass_recursive():
    """
    dumps() dataclass recursive
    """
    obj = Dataclass1("a", 1, Dataclass1("b", 2, None))
    dumped = xoryaml.dumps(obj)
    assert dumped == "---\nname: a\nnumber: 1\nsub:\n  name: b\n  number: 2\n  sub: ~"


def test_dataclass_circular():
    """
    dumps() dataclass circular
    """
    obj1 = Dataclass1("a", 1, None)
    obj2 = Dataclass1("b", 2, obj1)
    obj1.sub = obj2
    with pytest.raises(xoryaml.YAMLEncodeError):
        xoryaml.dumps(obj1)


def test_dataclass_empty():
    """
    dumps() no attributes
    """
    assert xoryaml.dumps(EmptyDataclass()) == "---\n{}"


def test_dataclass_empty_slots():
    """
    dumps() no attributes slots
    """
    assert xoryaml.dumps(EmptyDataclassSlots()) == "---\n{}"


def test_dataclass_default_arg():
    """
    dumps() dataclass default arg
    """
    obj = Dataclass2()
    assert xoryaml.dumps(obj) == '---\nname: "?"'


def test_dataclass_types():
    """
    dumps() dataclass types
    """
    obj = Dataclass3("a", 1, {"a": "b"}, True, 1.1, [1, 2], (3, 4))
    dumped = xoryaml.dumps(obj)
    assert (
        dumped
        == "---\na: a\nb: 1\nc:\n  a: b\nd: true\ne: 1.1\nf:\n  - 1\n  - 2\ng:\n  - 3\n  - 4"
    )


def test_dataclass_metadata():
    """
    dumps() dataclass metadata
    """
    obj = Dataclass4("a", 1, 2.1)
    assert xoryaml.dumps(obj) == "---\na: a\nb: 1\nc: 2.1"


def test_dataclass_classvar():
    """
    dumps() dataclass class variable
    """
    obj = Dataclass4("a", 1)
    assert xoryaml.dumps(obj) == "---\na: a\nb: 1\nc: 1.1"


def test_dataclass_subclass():
    """
    dumps() dataclass subclass
    """
    obj = Datasubclass("a", 1, None, False)
    assert xoryaml.dumps(obj) == "---\nname: a\nnumber: 1\nsub: ~\nadditional: false"


def test_dataclass_slots():
    """
    dumps() dataclass with __slots__ does not include InitVar or ClassVar
    """
    obj = Slotsdataclass("a", 1, "c", "d")
    assert "__dict__" not in dir(obj)
    assert xoryaml.dumps(obj) == "---\na: a\nb: 1\n_c: c"


def test_dataclass_init():
    """
    dumps() does not include InitVar or ClassVar
    """
    obj = InitDataclass("zxc", "vbn")
    assert xoryaml.dumps(obj) == "---\nab: zxc vbn"


@dataclass(frozen=True)
class ConcreteAbc(AbstractBase):
    __slots__ = ("attr",)

    attr: float

    def key(self):
        return "dkjf"


class TestAbstractDataclass:
    def test_dataclass_abc(self):
        obj = ConcreteAbc(1.0)
        assert xoryaml.dumps(obj) == "---\nattr: 1"
