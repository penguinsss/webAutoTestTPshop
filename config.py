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

# 日志器（logger）是入口，真正干活儿的是处理器（handler），
# 处理器（handler）还可以通过过 滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作

def config_log():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    sh = logging.StreamHandler()  # 把日志输出到控制台
    # 将日志信息记录到文件中，以特定的时间间隔切换日志文件。
    # filename: 日志文件名
    # when: 时间单位，可选参数
    #     S - Seconds
    #     M - Minutes
    #     H - Hours
    #     D - Days
    #     midnight - roll over at midnight
    #     interval: 时间间隔
    #     backupCount: 日志文件备份数量。如果backupCount大于0，那么当生成新的日志文件时， 将只保留backupCount个文件，删除最老的文件。
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='S',
                                                   interval=5,
                                                   backupCount=4)

    sh.setFormatter(formatter)
    th.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(th)
