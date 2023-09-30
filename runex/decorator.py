from types import GeneratorType, FunctionType
from typing import Any

from . import logger
from .registry import register
from .datalog import log


def _decorator(func: FunctionType, name: str, *args, **kwargs) -> Any:
    """ Function Run Controller
    """
    
    def __inner(*_args, **_kwargs):
        logger.debug(f"[RUN] {name}")
        returns = func(*_args, **_kwargs)
        # TODO: Maybe have some functionality to remember result when
        # the params are the same, so we dont need to run repeatedly.
        
        if isinstance(returns, GeneratorType):
            # If the experiments are yielding to log
            collector = list()
            for row in returns:
                log(row, name)
                collector.append(row)
            return collector
    
        elif returns is not None:
            # Experiment returns once after the expt to log
            log(returns, name)
            return returns
    
    register(name, __inner, func)
    return __inner
 

def experiment(ident, *args, **kwargs) -> FunctionType:
    """
    @experiment
    -----------
    This is the central `@experiment` decorator around which everything is based.
    """
    
    if type(ident) == FunctionType:
        # We have a plain decorator
        # @experiment
        return _decorator(ident, ident.__name__, *args, **kwargs)
        
    elif type(ident) == str:
        # We have a decorator with params
        # @experiment("Some other name", a="sdf") 
        return lambda func: _decorator(func, ident, *args, **kwargs)
