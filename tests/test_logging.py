import inspect
import logging

def test_demo_logging():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    filehandler = logging.FileHandler("logfile.log")

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("THIS IS A DEBUG STATEMENT")
    logger.info("THIS IS A INFO STATEMENT")
    logger.warning("THIS IS A WARNING STATEMENT")
    logger.error("THIS IS A ERROR STATEMENT")
    logger.critical("THIS IS A CRITICAL STATEMENT")


