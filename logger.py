import logging

logging.basicConfig(
    format="\n\n%(asctime)s - %(name)s - %(levelname)s\n%(message)s",
    filename='main_log.log',
    level=logging.WARNING
)
logger = logging.getLogger(__name__)


def logged_func(func):
    def logged(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            logger.exception(ex)
            raise ex
    return logged