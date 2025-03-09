import os

import pytest

import xoryaml

pytestmark = pytest.mark.skipif(os.environ.get("CI") is not None, reason="CI")


DATA = [
    [
        "college",
        -380608299.3165369,
        {
            "closely": 595052867,
            "born": False,
            "stomach": True,
            "expression": True,
            "chosen": 34749965,
            "somebody": False,
        },
        "positive",
        True,
        False,
    ],
    "price",
    2018186817,
    "average",
    "young",
    -1447308110,
]

SRC = """
---
- - college
  - -380608299.3165369
  - closely: 595052867
    born: false
    stomach: true
    expression: true
    chosen: 34749965
    somebody: false
  - positive
  - true
  - false
- price
- 2018186817
- average
- young
- -1447308110

"""

MULTIDOC = (
    """
---
basis: true
discussion: 1690275082
twice: count
another: false
tiny:
  worth: straw
  plus: ride
  duty: basis
  wave:
    - seeing
    - outline
    - true
    - congress
    - -870479755
    - truck
  large: rhyme
  load: did
...
---
getting:
  final:
    - false
    - true
    - -2020793880.414512
    - true
    - -950872146.990103
    - thing
  arrange: naturally
  breakfast: 1065730575
  clothes: drop
  mean: flame
  north: silly
fireplace: why
prove: true
various: true
breeze: true
us: true
"""
    * 1000
)


@pytest.mark.benchmark(group="dumps")
def test_xoryaml_bench_dumps(benchmark):
    benchmark(xoryaml.dumps, DATA)


@pytest.mark.benchmark(group="dumps")
def test_pyyaml_bench_dumps(benchmark):
    import yaml
    from yaml import CDumper

    benchmark(yaml.dump, DATA, Dumper=CDumper)


@pytest.mark.benchmark(group="loads")
def test_xoryaml_bench_loads(benchmark):
    benchmark(xoryaml.loads, SRC)


@pytest.mark.benchmark(group="loads")
def test_pyyaml_bench_loads(benchmark):
    import yaml
    from yaml import CSafeLoader

    benchmark(yaml.load, SRC, Loader=CSafeLoader)


def xoryaml_loads_all(str):
    list(xoryaml.loads_all(str))


def pyyaml_loads_all(str):
    import yaml
    from yaml import CSafeLoader

    list(yaml.load_all(str, Loader=CSafeLoader))


@pytest.mark.benchmark(group="loads_all")
def test_xoryaml_bench_loads_all(benchmark):
    benchmark(xoryaml_loads_all, MULTIDOC)


@pytest.mark.benchmark(group="loads_all")
def test_pyyaml_bench_loads_all(benchmark):
    benchmark(pyyaml_loads_all, MULTIDOC)
