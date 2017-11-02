# -*- coding:utf-8 -*-
# TimedRotatingFileHandler
import logging
import time
from logging.handlers import TimedRotatingFileHandler

trf_debug_handler = TimedRotatingFileHandler(
    filename="logs/log_debug.log",
    interval=1,
    when="D"
)
trf_debug_handler.setLevel(logging.DEBUG)

trf_info_handler = TimedRotatingFileHandler(
    filename="log_info.log",
    interval=1,
    when="D"
)
trf_info_handler.setLevel(logging.INFO)

trf_warning_handler = TimedRotatingFileHandler(
    filename="log_warning.log",
    interval=1,
    when="D"
)
trf_warning_handler.setLevel(logging.WARNING)

trf_error_handler = TimedRotatingFileHandler(
    filename="log_error.log",
    interval=1,
    when="D"
)
trf_error_handler.setLevel(logging.ERROR)

logging.basicConfig(
    format="[%(asctime)s] : %(message)s",
    handlers=[trf_debug_handler, trf_info_handler, trf_warning_handler, trf_error_handler],
    level=logging.DEBUG
)


logging.debug('debug1')
logging.info('info1')
logging.warning('warning1')
logging.error('error1')
