import logging
import sys
from typing import Callable
from typing import List

import defopt

from pypi_test_ameynert.tools.hello import hello

_tools: List[Callable] = [hello]


def setup_logging(level: str = "INFO") -> None:
    """Set up basic logging to print to the console."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(name)s:%(funcName)s:%(lineno)s [%(levelname)s]: %(message)s",
    )


def run() -> None:
    """Set up logging, then hand over to defopt for running command line tools."""
    setup_logging()
    logger = logging.getLogger("pypi_test_ameynert")
    logger.info("Executing: " + " ".join(sys.argv))
    defopt.run(
        funcs=_tools,
        argv=sys.argv[1:],
    )
    logger.info("Finished executing successfully.")
