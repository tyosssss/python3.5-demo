# -*- coding:utf-8 -*-
# 配置root logger
import logging

logging.basicConfig(
    datefmt='%Y%m%d%H%M%S',
    format="%(asctime)s: %(message)s",
    level=logging.DEBUG
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
