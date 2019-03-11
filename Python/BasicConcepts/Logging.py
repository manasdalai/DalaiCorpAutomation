'''Logging mechanism in Python
Logging the status to a file'''
import logging

logging.basicConfig(filename='PythonExecutionLog.log', level=logging.DEBUG)  # Define logging file location and name
logging.debug("Debugging information")  # Log Debug message to file
logging.info("Information detail")  # Log info message to file
logging.warning("Warning message")  # Log warning message to file
logging.error("Reporting Error Message")  # Log an error message to file
logging.critical("Critical Error ... Shutting Down server")  # Log a Critical message to a file
