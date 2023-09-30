# Logging stuff
from logging import getLogger, StreamHandler, Formatter
from logging import INFO

logger = getLogger(__name__)
logger.setLevel(INFO)

ch = StreamHandler()
ch.setFormatter(Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(ch)

from .decorator import experiment
from .datalog import log

# ===========================
# CLI _______________________

def cli():
    from sys import argv
    pass
