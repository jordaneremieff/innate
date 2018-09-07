# innate

Small library for implementing command-line interfaces in Python 3.6+ projects.

## Installation

`pip3 install innate`

## Example

```python
from innate import Innate

innate = Innate()


@innate("mycommand")
def noargs():
    print("Example command.")


@innate("print_string")
def singlearg(s):
    print(f"Hello {s}")


@innate("test_default")
def test(s, mydefault="defaultval"):
    print(f"Arg s={s}, mydefault={mydefault}")


@innate("test_annotation")
def typed_args(s: str, myint: int = 11):
    print(f"Arg s={s}, myint={myint}")
```

Full example project in `example/`.
