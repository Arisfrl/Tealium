import inspect
import logging
import os

# NOTSET=0.
# DEBUG=10.
# INFO=20.
# WARN=30.
# ERROR=40.
# CRITICAL=50.

class LogGen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        logName = inspect.stack()[1][3]

        logger = logging.getLogger(logName)
        fileHandler = logging.FileHandler(path)
        formatter = logging.Formatter(fmt='%(asctime)s: %(levelname)s: %(name)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)

        for i in inspect.stack()[1]:
            logger.info(i)
            logger.info(type(i))

        return logger
