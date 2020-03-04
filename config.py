"""配置文件（如：日志模块
                当前文件所在目录的绝对路径：BASE_DIR = os.path.dirname(os.path.abspath(__file__))  ）"""
import logging.handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ★★ 日志导入一次即可，不管在哪个地方导入，其他任何地方都是可用的
# 日志：
#   1 在配置文件中定义
#   2 基类包中的init模块中调用
#   3 在程序的入口suite中导入基类包，从而调用日志方法


def config_log():
    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    sh = logging.StreamHandler()
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='S',
                                                   interval=5,
                                                   backupCount=4)

    sh.setFormatter(formatter)
    th.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(th)
