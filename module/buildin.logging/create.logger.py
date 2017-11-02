# -*- coding:utf-8 -*-
# 创建一个console logger
import logging
import logging.handlers
import sys

from logging import StreamHandler, Formatter

logger = logging.getLogger("console")
logger.setLevel(logging.INFO)

# 创建formater
console_formater = Formatter('%(asctime)s [%(levelname)s] : %(message)s')

# 创建handler
console_handler = StreamHandler(sys.stdout)
console_handler.setFormatter(console_formater)

logger.addHandler(console_handler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

