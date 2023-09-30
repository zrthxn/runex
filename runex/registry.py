from . import logger

_REGISTRY_ = dict()
""" Experiment Registry
"""


def register(name, inner, func):
    if name in _REGISTRY_:
        logger.warn(f"Experiment `{name}` already registered. Overwriting.")
    
    # Register Function
    logger.debug(f"[REG] {name}")
    
    _REGISTRY_[name] = {
        "id": name,
        "run": inner,
        "func": func
    }