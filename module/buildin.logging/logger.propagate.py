# -*- coding:utf-8 -*-
# 测试传播机制

# -*- coding:utf-8 -*-
# 创建一个console logger
import logging
import logging.handlers
import sys

from logging import StreamHandler, Formatter

logging.basicConfig(
    format="[%(name)s] %(asctime)s-%(name)s-%(levelname)s-%(message)s",
    level=logging.ERROR
)

logger = logging.getLogger("console")
logger.setLevel(logging.INFO)

# 创建formater
console_formater = Formatter('[%(name)s] %(asctime)s [%(levelname)s] : %(message)s')

# 创建handler
console_handler = StreamHandler(sys.stdout)
console_handler.setFormatter(console_formater)

logger.addHandler(console_handler)

# 开启传播
# logger = INFO , debug被忽略
# 虽然 root logger = ERROR ; 但是由于是传播来的 , 还是会输出 info ~ critical 的错误信息
logger.propagate = True
logger.debug('1.debug')
logger.info('1.info')
logger.warning('1.warning')
logger.error('1.error')
logger.critical('1.critical')

# 关闭传播
# 只会打印 logger 输出的 ,不会打印 root logger
logger.propagate = False
logger.debug('2.debug')
logger.info('2.info')
logger.warning('2.warning')
logger.error('2.error')
logger.critical('2.critical')