import logging
import os


def _get_log_level():
  """Get the log level from the environment variable LOG_LEVEL"""
  levels = {
    "DEBUG"   : logging.DEBUG,
    "INFO"    : logging.INFO,
    "WARNING" : logging.WARNING,
    "ERROR"   : logging.ERROR,
    "CRITICAL": logging.CRITICAL
  }
  level = os.getenv("LOG_LEVEL", "INFO").upper()
  return levels.get(level, logging.INFO)


def build_logger(logger_name):
    """Configure a logger with the specified name"""
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(_get_log_level())
    logger.addHandler(console_handler)
    return logger


def build_logger_custom(logger_name, custom_formatter):
  """Configure a logger with the specified name"""
  logger = logging.getLogger(logger_name)
  console_handler = logging.StreamHandler()
  console_handler.setFormatter(custom_formatter)
  console_handler.setLevel(_get_log_level())
  logger.addHandler(console_handler)
  return logger