# -*- coding:utf-8 -*-
import logging

#
# logger = logging.getLogger('WUTP')
# logger.setLevel(10)
# logger.error('hahaha')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

foo_logging = logging.getLogger('foo')
foo_logging.propagate = False
foo_logging.setLevel(logging.ERROR)
foo_bar_logging = logging.getLogger('foo.bar')

foo_bar_logging.warning('foo.bar')

print(foo_logging.getEffectiveLevel())
print(foo_logging.isEnabledFor(logging.WARNING))
