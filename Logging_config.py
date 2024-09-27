import logging
import os
from logging.handlers import TimedRotatingFileHandler
import time

log_format = '%(asctime)s - %(levelname)s - %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format, date_format))
logger.addHandler(console_handler)

file_handler = TimedRotatingFileHandler(
    filename= os.path.join('logs', f'log-{time.strftime("%Y-%m-%d")}.log'),
    when='midnight',
    backupCount=30
)
file_handler.setFormatter(logging.Formatter(log_format, date_format))
logger.addHandler(file_handler)
