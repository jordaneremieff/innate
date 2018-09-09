from innate import Innate

innate = Innate(description="MyApp CLI")


@innate()
def hello(name):
    """
    Print Hello with a name argument.

    myapp hello you
    """
    print(f"Hello, {name}")


@innate()
async def helloasync(name):
    """
    Print Hello with a name argument in a coroutine.

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
