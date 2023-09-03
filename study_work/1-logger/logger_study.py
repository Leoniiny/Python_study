import logging

'''
logger.record:生成日志-->>得到的是对象
looger.formatter:将生成的日志对象转换为字符串
logger.handler:将日志记录输出到指定的日志位置和存储形式
记录器（Logger）：提供应用程序代码直接使用的接口
处理器（Handler）：将日志记录（由记录器创建）发送到适当的目的地
筛选器（Filter）：提供了更细粒度的功能，用于确定要输出的日志记录
格式器（Formatter）：程序在最终输出日志记录的内容格式
logging日志等级：CRITICAL(50) > ERROR(40) > WARNING(30) > INFO(20) > DEBUG(10)
'''


class LoggerStudy():
    def __init__(self):
        # 设定记录器名称，没有填默认未root
        self.logger = logging.getLogger()
        # 设置输出等级
        self.logger.setLevel(level=logging.INFO)

    def logger_print(self):
        """
        asctime:运行时间
        name:运行模块
        levelname：日志级别
        message：日志内容
        basicConfig参数：
            filename：将日志信息写入文件中，指定该设置项后日志信息就不会被输出到控制台了
            filemode：指定日志文件的打开模式，默认为'a'，只有filename存在时起作用
            format：指定日志格式字符串
                %(asctime) s：打印日志的时间
                %(name)s ：记录器名称
                %(levelname) s：打印日志级别的名称
                %(message) s：打印日志信息
            datefmt：指定日期/时间格式，format中包含时间字段%(asctime)s时才有效--'%Y/%m/%d %H:%M:%S'
        """
        # 基础配置
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s -  \
        %(pathname) s',datefmt='%Y/%m/%d %H:%M:%S',filename="./logger_file.log")

        self.logger.info("this is a logger info.")
        self.logger.debug("Debug")
        self.logger.warning('Warning exists')
        self.logger.info('Finish')

    def handler_study(self):
        self.handler = logging.FileHandler("logger_file.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)


if __name__ == '__main__':
    # 声明logger对象，日志名称不输入就是root
    logger = logging.getLogger("feiwu")
    # 设置日志输出等级
    logger.setLevel(logging.INFO)
    # 声明handler对象
    handler = logging.FileHandler('output.log')
    # 声明1个格式化对象，针对处理器的输出指定一个格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
