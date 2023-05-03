# python的日志模块将主要的日志分为5个等级（debug/info/warning/error/critical），默认情况下主要记录后3个
# 日志模块通过basicConfig()方法指定日志输出路径，记录格式和，记录等级等等
# 通过disable()方法可以禁用所有日志
import logging

logging.basicConfig(filename="test.log", format='[%(asctime)s] %(levelname)s %(name)s %(message)s', level=logging.INFO)
logging.disable()

logging.debug("this is debug level")
logging.info("this is info level")
logging.warning("this is warning level")
logging.error("this is error level")
logging.critical("this is critical level")