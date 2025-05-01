from lambda_utils_logger.logger_util import Logger

logger = Logger().get_logger(__name__)

class CleanerUseCase:

  @staticmethod
  def execute():
    logger.info(f"CleanerUseCase")

    logger.info(f"CleanerUseCase executed")

