import logging
import os
import sys
from logging import handlers

import time

logger = logging.getLogger("app")
formatter = logging.Formatter("%(asctime)s %(levelname)-8s: %(message)s")

# filehan = logging.FileHandler("/Users/arvin/Documents/code/test/log1/test.log")
# filehan.setFormatter(formatter)

cons = logging.StreamHandler()
cons.formatter = formatter
# logger.addHandler(filehan)
logger.addHandler(cons)

import datetime

now = datetime.datetime.now()
# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 各模块目录
MODULE_DIR = {

    'log_dir': os.path.join(BASE_DIR, 'log/logs'),  # 测试脚本目录

}
ROOT_PATH = os.path.join(MODULE_DIR['log_dir'])
print(ROOT_PATH)
#
filename = "{}.log".format(now)
full_path = os.path.join(ROOT_PATH, filename)
th = handlers.TimedRotatingFileHandler(filename=full_path, when="s", backupCount=3,
                                       encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
th.setFormatter(formatter)
logger.addHandler(th)
# logger.setLevel(logging.INFO)

logger.debug("this is debug info1")
logger.info("this is debug info2")
logger.warning("this is debug info")
logger.error("this is debug info")
logger.fatal("this is debug info")
logger.critical("this is debug info")
