import logging
import pathlib
import sys
from dataclasses import dataclass
from logging import LogRecord
from logging.handlers import TimedRotatingFileHandler
from typing import Dict, Literal

from gcs_logger.enums import LogColor, FontWeight

LOG_FORMATTER = "%(asctime)s : %(name)s :%(levelname)s: %(message)s"


@dataclass
class LogLevelStyle:
    """Contains options for printing messages in a console that supports ANSI colors, used by ColorHandler."""

    color: LogColor
    font_weight: FontWeight


class _ColoredStream:
    """A class that loosely wraps around a stream that a logger writes to,
    allowing callers to write text to the stream in a particular color."""

    def __init__(self, stream):
        self.stream = stream

    @classmethod
    def supported(cls, stream=sys.stdout):
        """A class method that returns True if the current platform supports
        coloring terminal output using this method. Returns False otherwise."""
        if not stream.isatty():
            return False  # auto color only on TTYs
        try:
            # REASON: (Magnus) curses may not be importable. Whether we can import it determines which code path we take
            #  here. This is cleaner than workarounds such as importing an alternative that does nothing at the top.
            # pylint: disable=import-outside-toplevel
            import curses
        except ImportError:
            return False
        # REASON: (Magnus) Literally any problem should result in False.
        # noinspection PyBroadException
        try:
            try:
                return curses.tigetnum("colors") > 2
            except curses.error:
                curses.setupterm()
                return curses.tigetnum("colors") > 2
        except Exception as exc:
            print(exc.__traceback__)
            # NOTE: (Magnus) Raw copy/pasted code raised and then returned False, resulting in a warning.
            # guess false in case of error
            return False

    def write(self, text, color: LogColor, font_weight: FontWeight):
        """
        Write the given text to the stream in the given color.
        @param text: Text to be written to the stream.
        @param color: A LogColor, e.g. LogColor.BLACK, LogColor.RED...
        @param font_weight: A FontWeight, e.g. FontWeight.NORMAL or FontWeight.BOLD.
        """
        self.stream.write(f"\x1b[{color.value};{font_weight.value}m{text}\x1b[0m")


class ColorHandler(logging.StreamHandler):
    """
    A handler for loggers that write messages with colors according to the log level.
    For example, logging.INFO messages will be green and logging.ERROR messages will be red.
    Example usage:
      logger = logging.getLogger(__name__)
      logger.addHandler(ColorHandler())
      logger.setLevel(logging.INFO)
    """

    def __init__(self, stream=sys.stdout):
        # noinspection PyTypeChecker
        super().__init__(_ColoredStream(stream))
        super().setFormatter(logging.Formatter(LOG_FORMATTER))

    def emit(self, record: LogRecord):
        # Log level to color name and shrinkage
        level_styles: Dict[int, LogLevelStyle] = {
            logging.DEBUG: LogLevelStyle(color=LogColor.GRAY, font_weight=FontWeight.NORMAL),
            logging.INFO: LogLevelStyle(color=LogColor.GREEN, font_weight=FontWeight.NORMAL),
            logging.WARNING: LogLevelStyle(color=LogColor.YELLOW, font_weight=FontWeight.NORMAL),
            logging.ERROR: LogLevelStyle(color=LogColor.RED, font_weight=FontWeight.NORMAL),
            logging.CRITICAL: LogLevelStyle(color=LogColor.RED, font_weight=FontWeight.BOLD),
        }

        style: LogLevelStyle = level_styles.get(record.levelno, LogColor.BLUE)
        # NOTE: _ColoredStream changes the signature of self.stream.write
        stream: _ColoredStream = self.stream
        formatted_message = self.format(record) + "\n"

        stream.write(
            text=formatted_message,
            color=style.color,
            font_weight=style.font_weight,
        )


def get_gcs_logger(
    name: str | None = None,
    log_level: str | Literal[0, 10, 20, 30, 40, 50] = logging.INFO,
    filename: str | None = None,
) -> logging.Logger:
    """
    :param name: The name of the logger.
    :param log_level: The log level of the logger, e.g. "INFO" or logging.INFO or 10(int for INFO). Will default to logging.INFO.
    :param filename: The name of the file to write logs to. If None, logs will be written to stdout only
    :return: A logger with the given name and log level that writes messages with colors according to the log level.
    """
    if isinstance(log_level, str):
        log_level = log_level.upper()

    if log_level not in (0, 10, 20, 30, 40, 50, "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        raise ValueError(f"Invalid log level. Received: {log_level}")

    logger = logging.getLogger(name)

    # set all __name__ or Root logger to debug to allow the lowest level of logging to be passed to any handlers
    logger.setLevel(logging.DEBUG)

    # NOTE: we use logger.handlers instead of logger.hasHandlers() because the latter traverses the entire logger hierarchy
    #   the former only checks the immediate logger
    if not logger.handlers:
        color_handler = ColorHandler()
        color_handler.setLevel(log_level)
        logger.addHandler(color_handler)

    if filename:
        path = pathlib.Path.home() / filename
        # NOTE: Delay is set to True to prevent the files being opened before it has anything to write
        #   This is important because the logger is initialized in many places and can cause file locks
        file_handler = TimedRotatingFileHandler(
            path, when="midnight", interval=1, backupCount=7, delay=True
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(LOG_FORMATTER))
        logger.addHandler(file_handler)

    return logger
