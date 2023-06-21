#!/usr/bin/env python3

"""
Hybrid Database Model for Extended NLP Context
Error handling script for the Hybrid Database Model application.

This script provides a centralized error handling mechanism.
"""

# Standard library imports
import traceback
import logging
from datetime import datetime

class ErrorHandler:
    """
    ErrorHandler class for managing and logging errors.
    """

    def __init__(self, log_file="error_log.txt"):
        """
        Initialize ErrorHandler with log file name.

        :param log_file: The file to write error logs to.
        """
        self.log_file = log_file

    def handle_error(self, exception, context=""):
        """
        Handle the provided exception by logging and optionally print to the console.

        :param exception: The exception to handle.
        :param context: Optional additional context about when/where the error occurred.
        """
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Build the error message
        error_message = f"ERROR: {type(exception).__name__} occurred at {current_time}.\n"
        if context:
            error_message += f"Context: {context}\n"
        error_message += f"Message: {str(exception)}\n"
        error_message += "Traceback:\n"
        error_message += "".join(traceback.format_tb(exception.__traceback__))

        # Log the error message
        self._log_error(error_message)

        # Optionally print the error message to the console
        print(error_message)

    def _log_error(self, error_message):
        """
        Write the error message to the log file.

        :param error_message: The error message to log.
        """
        with open(self.log_file, "a") as log_file:
            log_file.write(error_message + "\n\n")