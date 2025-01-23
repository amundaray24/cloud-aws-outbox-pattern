import logging
import os

from lambda_utils_xray.xray_formatter import XRayFormatter
from lambda_utils_xray.xray_manager import AWSXRayManager

class Logger:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
      cls._instance._init()
    return cls._instance

  def _init(self):
    AWSXRayManager()

  def get_logger(self, name: str):
    """
    Retrieves a configured logger.
    :param name: The logger's name.
    :return: A logger instance.
    """
    handler = logging.StreamHandler()
    handler.setFormatter(XRayFormatter('%(asctime)s - %(levelname)s - [trace_id=%(trace_id)s span_id=%(span_id)s] %(message)s'))
    handler.setLevel(self._get_log_level())

    logger = logging.getLogger(name)
    logger.setLevel(self._get_log_level())
    logger.addHandler(handler)
    logger.propagate = False
    return logger

  @staticmethod
  def _get_log_level():
    """
    Retrieves the log level from the environment variable LOG_LEVEL.
    Defaults to INFO if not set.
    """
    levels = {
      "DEBUG": logging.DEBUG,
      "INFO": logging.INFO,
      "WARNING": logging.WARNING,
      "ERROR": logging.ERROR,
      "CRITICAL": logging.CRITICAL,
    }
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    return levels.get(level, logging.INFO)
