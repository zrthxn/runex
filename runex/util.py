from types import FunctionType
from argparse import ArgumentParser


def reflection(func: FunctionType) -> ArgumentParser:
    """
    Reflection
    -------------

    This function can be used to create an argparser for a function to be run as a CLI.
    For this to work, all you need to do is have a function in the module with the right type-annotations
    and all optional values should have a default value.

        ```python
        # Here model_name is required and data_path is optional
        def train(model_name: str, data_path: str = "data.json"):
            ''' This docstring will be the CLI help text
            '''
            ...
        ```

    You can even see the required inputs for a function using the `--help` flag.
    """
    
    annotations = func.__annotations__
    defaults = func.__defaults__

    parser = ArgumentParser(description = func.__doc__)

    # Required args are the first arguments for which a default value
    # is not available. This will add those as required.
    required = list(annotations.items())[:len(annotations) - len(defaults)]
    for aname, atype in required:
        parser.add_argument(f"--{aname}", 
                            type=atype, 
                            help='%(type)s',
                            required=True)

    # Optional args are those for which a default value is available.
    optional = list(annotations.items())[len(annotations) - len(defaults):]
    for (aname, atype), dvalue in zip(optional, defaults):
        parser.add_argument(f"--{aname}", 
                            type=atype, 
                            help='%(type)s (default %(default)s)',
                            default=dvalue)

    return parser
