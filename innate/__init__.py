import sys
import argparse
from inspect import signature


class Innate:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Innate CLI")
        self.subparsers = self.parser.add_subparsers()

    def __call__(self, name):
        def decorator(func):
            parser = self.subparsers.add_parser(name)
            parser.set_defaults(func=func)
            sig = signature(func)
            for parameter in sig.parameters.values():
                if parameter.default == parameter.empty:
                    parser.add_argument(parameter.name, type=parameter.annotation)
                else:
                    parser.add_argument(
                        f"--{parameter.name}",
                        default=parameter.default,
                        type=parameter.annotation,
                    )
            return func

        return decorator

    def cli(self, args=None):
        if len(sys.argv) == 1:
            self.parser.print_help()
            sys.exit()
        args = self.parser.parse_args()
        _args = vars(args)
        func = _args.pop("func")
        func(**_args)
