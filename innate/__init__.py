import sys
import argparse
import typing
import asyncio
import concurrent.futures
from functools import partial
from inspect import signature, getdoc

from innate.__version__ import __version__


class Innate:
    def __init__(self, description: str = f"Innate CLI {__version__}") -> None:
        self.description = description
        self.parser = argparse.ArgumentParser(description=description)
        self.subparsers = self.parser.add_subparsers()

    def __call__(self, name: str = None) -> typing.Callable:
        def decorator(func: typing.Callable) -> typing.Callable:
            parser_name = name or func.__name__
            parser = self.subparsers.add_parser(parser_name, help=getdoc(func))
            sig = signature(func)
            parser.set_defaults(func=func)

            kwargs = {}

            for parameter in sig.parameters.values():

                if parameter.annotation is not parameter.empty:
                    kwargs["type"] = parameter.annotation

                if parameter.default is not parameter.empty:
                    arg_name = f"--{parameter.name}"
                    kwargs["default"] = parameter.default
                else:
                    arg_name = parameter.name

                parser.add_argument(arg_name, **kwargs)

            return func

        return decorator

    async def cli(self):
        if len(sys.argv) == 1:
            self.parser.print_help()
            sys.exit()

        args = vars(self.parser.parse_args())
        func = args.pop("func")
        command = partial(func, **args)

        if not asyncio.iscoroutinefunction(func):
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
            loop = asyncio.get_event_loop()
            sync_command = partial(loop.run_in_executor, executor, command)
            try:
                loop.run_until_complete(asyncio.wait_for(sync_command(), None))
            finally:
                return

        await command()

    def main(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(loop.create_task(self.cli()))
