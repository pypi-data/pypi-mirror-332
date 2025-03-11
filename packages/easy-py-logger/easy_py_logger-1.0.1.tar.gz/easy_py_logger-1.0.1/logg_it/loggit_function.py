# loggit_function.py
import logging
import sys
import functools
import traceback
import os
import re
from contextlib import ContextDecorator
from io import StringIO

class logg_it(ContextDecorator):
    """
    A decorator and context manager that simplifies logging.
    - Captures `print()` and logging output
    - Logs exceptions automatically
    - Supports log levels and custom formats
    - Can write logs to a file or console
    - Optionally logs only errors
    - Tags logs with function names
    - Highlights the exact error line
    """
    def __init__(self, log_file=None, level=logging.INFO, log_to_console=True, log_format=None, log_errors_only=False):
        """
        :param log_file: (Optional) Path to log file. If None, logs only to console.
        :param level: Logging level (default: INFO)
        :param log_to_console: If False, logs only to file (default: True)
        :param log_format: Custom log format (default: standard format)
        :param log_errors_only: If True, logs only errors (default: False)
        """
        self.log_file = log_file
        self.level = level
        self.log_to_console = log_to_console
        self.log_errors_only = log_errors_only
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level)

        # Default log format
        self.log_format = log_format or "%(asctime)s - %(levelname)s - %(message)s"

        # Ensure log handlers are added only once
        if not self.logger.hasHandlers():
            handlers = []

            # Log to file if specified
            if self.log_file:
                os.makedirs(os.path.dirname(self.log_file), exist_ok=True)  # Ensure directory exists
                file_handler = logging.FileHandler(self.log_file)
                file_handler.setFormatter(logging.Formatter(self.log_format))
                handlers.append(file_handler)

            # Log to console if enabled
            if self.log_to_console:
                console_handler = logging.StreamHandler(sys.stdout)
                console_handler.setFormatter(logging.Formatter(self.log_format))
                handlers.append(console_handler)

            for handler in handlers:
                self.logger.addHandler(handler)

        self.stdout_capture = StringIO()

    def __enter__(self):
        """ Starts capturing stdout. """
        self.original_stdout = sys.stdout
        sys.stdout = self.stdout_capture
        return self

    def __exit__(self, exc_type, exc_value, traceback_obj):
        """ Restores stdout and logs exceptions/output. """
        sys.stdout = self.original_stdout
        captured_output = self.stdout_capture.getvalue().strip()

        if captured_output and not self.log_errors_only:
            self.logger.info(f"Captured Output:\n{captured_output}")

        if exc_type is not None:
            self._log_exception(exc_type, exc_value, traceback.format_exc())

    def __call__(self, func):
        """ Allows use as a decorator and tags logs with function name. """
        function_name = func.__name__

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with self:
                try:
                    result = func(*args, **kwargs)
                    if not self.log_errors_only:
                        self.logger.info(f"[{function_name}] Function executed successfully")
                    return result
                except Exception as e:
                    self._log_exception(type(e), e, traceback.format_exc(), function_name)
                    raise
        return wrapper

    def _log_exception(self, exc_type, exc_value, traceback_obj, function_name=""):
        """ Logs exceptions with traceback and highlights the error line. """
        error_message = f"Exception in [{function_name}]: {exc_type.__name__}: {exc_value}"

        # Extract and highlight the most important line from traceback
        traceback_lines = traceback_obj.split("\n")
        error_line = next((line for line in traceback_lines if "File" in line and "line" in line), None)

        if error_line:
            highlighted_error = re.sub(r'File "(.*?)", line (\d+)', r'🔥 **\1, line \2**', error_line)
            error_message += f"\n🔴 {highlighted_error}"

        self.logger.error(error_message)
