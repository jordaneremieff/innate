# innate

Small library for implementing command-line interfaces in Python 3.6+ projects. Supports both async and sync functions.

## Installation

`pip3 install innate`

## Example

```python
from innate import Innate

innate = Innate(description="MyApp CLI")


@innate()
async def helloasync(name):
    """
    Print Hello with a name argument in a coroutine.

    myapp hello you
    """
    print(f"Hello, {name}")


@innate()
def hello(name):
    """
    Print Hello with a name argument.

    myapp hello you
    """
    print(f"Hello, {name}")


@innate()
def hello_world():
    """Print 'Hello World!' to the console."""
    print("Hello world!")


@innate("helloworld")
def helloworld():
    """Print 'Hello World!' to the console with a defined name."""
    print("Hello world!")


@innate()
def add(x: int, y: int):
    """
    Enter two values to add. Must be integers.

    myapp add 1 2
    """
    print(f"{x} + {y} = {x + y}")


@innate()
def add_x_or_100(x: int, y: int = 100):
    """
    Enter two values to add or a single value to add 100. Must be integers.

    myapp add_x_or_100 1
    myapp add_x_or_100 1 --y 1
    """
    print(f"{x} + {y} = {x + y}")

```

```
usage: myapp [-h]
             {helloasync,hello,hello_world,helloworld,add,add_x_or_100} ...

MyApp CLI

positional arguments:
  {helloasync,hello,hello_world,helloworld,add,add_x_or_100}
    helloasync          Print Hello with a name argument in a coroutine. myapp
                        hello you
    hello               Print Hello with a name argument. myapp hello you
    hello_world         Print 'Hello World!' to the console.
    helloworld          Print 'Hello World!' to the console with a defined
                        name.
    add                 Enter two values to add. Must be integers. myapp add 1
                        2
    add_x_or_100        Enter two values to add or a single value to add 100.
                        Must be integers. myapp add_x_or_100 1 myapp
                        add_x_or_100 1 --y 1

optional arguments:
  -h, --help            show this help message and exit
```

Full example project in `example/`.
