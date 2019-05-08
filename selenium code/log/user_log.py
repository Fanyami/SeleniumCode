#coding = utf-8
#打印日志

import logging
import os
import datetime

class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 流对象consle,控制台输出日志
        # 流添加addHandler
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)
        # logger.debug("teste")
        # consle.close()
        # logger.removeHandler(consle)

        # 创建同日期的文件名字
        # 获取文件路径  _(_file__:当前文件路径)  （dirname文件所在文件夹路径）
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        # 获取当前时间,按年月日格式来
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_dir + "/" + log_file

        # 文件输出日志，

        # file_handle = logging.FileHandler("/Users/pmy/Downloads/selenium code/log/logs/test.log")
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        # 输出日志格式化,进入Formatter方法里面看参数介绍
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s --> %(funcName)s %(levelno)s: %(levelname)s ------> %(message)s')
        self.file_handle.setFormatter(formatter)

        self.logger.addHandler(self.file_handle)

        #self.logger.debug("teste1234")


    def get_log(self):
        return  self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()


