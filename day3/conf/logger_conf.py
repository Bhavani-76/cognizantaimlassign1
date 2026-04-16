#config log format
import logging
"""
set up a logger for healthcare application
"""

def setup_logger():
    """
    create a logger for healthcare application
    """
    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)

    """
    check if logger already has a handlers to avoid duplicate logs
    """

    if logger.hasHandlers():
        return logger
    """
    create a file handler to write logs to healthcare.log file
    """
    file_handler = logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)

    """
    create formatter to specify the log formart and date format
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
