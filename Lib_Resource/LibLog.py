"""
Base module for logging
"""

import logging


class Log:
    """
    Base Class for logging
    Level       When it's used
    DEBUG       Detailed information, typically of interest only when diagnosing problems.
    INFO        Confirmation that things are working as expected.
    WARNING     An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
    ERROR       Due to a more serious problem, the software has not been able to perform some function.
    CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
    """

    @classmethod
    def set_logging(self,logfile_path, logfile_name, loglevel):
        numeric_level = getattr(logging, loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        logging.basicConfig(format='%(levelname)s : %(asctime)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',
                            filename=logfile_path+logfile_name, filemode='w', level=numeric_level)

    @classmethod
    def log_debug(self, message="Default Debug Message"):
        logging.debug(message)

    @classmethod
    def log_info(self, message="Default Info Message"):
        logging.info(message)


    @classmethod
    def log_warning(self, message="Default Warning Message"):
        logging.warning(message)

    @classmethod
    def log_error(self, message="Default Error Message"):
        logging.error(message)

    @classmethod
    def log_critical(self, message="Default Critical Message"):
        logging.critical(message)
