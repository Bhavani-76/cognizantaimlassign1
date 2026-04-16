import sys 
import os
#add project root to python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)


from conf.logger_conf import setup_logger
"""
Entry point for the appliaction. This module initializes the application and starts the main loop.

"""
logger = setup_logger()

def run():
    """
    test logger
    """
    logger.info("app run")
""" handle entry point """
if __name__ == "__main__":
    run()