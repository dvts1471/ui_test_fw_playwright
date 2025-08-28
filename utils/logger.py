import logging

from constants import LOG_LEVEL


class Logger:
    _loggers = {}

    def __init__(self, name=__name__, level=LOG_LEVEL):
        self.name = name
        if name not in self._loggers:
            self._loggers[name] = self._get_logger(name=name, level=level)

    @property
    def logger(self):
        return self._loggers[self.name]

    def _get_logger(self, name=__name__, level=LOG_LEVEL):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.hasHandlers():
            logger.handlers.clear()
        handler = logging.StreamHandler()
        formatter = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def info(self, msg):
        self.logger.info(msg=msg)

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg=msg)