# xoryaml

## Why?

Yet Another YAML library for Python ;)

I wanted a memory-safe and reasonably fast YAML library that could handle
`datetime` types. It takes inspiration (as well as a bit of the test suite)
from [orjson](https://github.com/ijl/orjson).

## Demo

```python
@dataclasses.dataclass
class YAYAMLModule:
    name: str
    released: datetime.datetime
    tuples: tuple[str, str]
    sets: set[str]
    dicts: dict[int, str]

module = YAYAMLModule(
    "xoryaml",
    released=datetime.datetime.now(datetime.timezone.utc),
    tuples=("supported", "of course"),
    sets={"why", "not?"},
    dicts={1: "No,", 2: "fíjate."},
)
print(xoryaml.dumps(module))
# ---
# name: xoryaml
# released: "2025-03-08T17:01:14.569027Z"
# tuples:
#   - supported
#   - of course
# sets:
#   - not?
#   - why
# dicts:
#   1: "No,"
#   2: fíjate.
print(xoryaml.loads(xoryaml.dumps(module)))
# {
#     "name": "xoryaml",
#     "released": "2025-03-08T17:01:14.569027Z",
#     "tuples": ["supported", "of course"],
#     "sets": ["why", "not?"],
#     "dicts": {1: "No,", 2: "fíjate."},
# }
```

In addition to datetimes, dataclasses, sets, and tuples are automatically
handled. You don't need to pass any settings for these to work. On the other
hand, you don't get any other settings either ;)

If you want to restore the parsed data into python data structures, I highly
recommend [pydantic](https://docs.pydantic.dev/latest/).

```python
validator = pydantic.TypeAdapter(YAYAMLModule).validator.validate_python
print(validator(xoryaml.loads(xoryaml.dumps(module))))
# YAYAMLModule(
#     name="xoryaml",
#     released=datetime.datetime(2025, 3, 08, 17, 1, 14, 569027, tzinfo=TzInfo(UTC)),
#     tuples=("supported", "of course"),
#     sets={"not?", "why"},
#     dicts={1: "No,", 2: "fíjate."},
# )
```

## Thanks

This project would not be possible without:

- [pyo3](https://pyo3.rs/): Rust-python interop
- [yaml-rust2](https://github.com/ethiraric/yaml-rust2): Pure Rust YAML impl
- [orjson](https://github.com/ijl/orjson): Parts of test suite
- [ryaml](https://github.com/emmatyping/ryaml): Parts of test suite
- [speedate (pydantic)](https://github.com/pydantic/speedate): Date formatting


## Dev install
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Install maturin: `uv tool install maturin`
- Make a venv `uv venv`
- Activate the venv `source .venv/bin/activate`
- Build and install `uv pip install -e '.[bench]'`
- Optional: build release `maturin develop --release`
- Run tests `pytest`

In order to keep the interface to native code as simple as possible, I have
implemented part of the interface in Python. Not sure if this is a bad idea, but
it seems to work fine? Let me know if otherwise.

## Run tests on all supported versions of python locally

- Install tox: `uv tool install tox --with tox-uv`
- Run: `tox`
