#coding = utf-8

#po模型
#所有用到的页面都定义成一个类，继承自基础的Page类
#把页面中用到的元素定义成方法
#把页面上一些操作定义成方法
#case 数据 页面 分开

#case层 需要输入

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import os
import HTMLTestRunner
import time
import sys
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = "/Users/pmy/Downloads/selenium code/image/test001.png"
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.5itest.cn/register')

        cls.driver.maximize_window()

    #unittest前置条件：打开网站  某一条case的前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()      #加self使driver变成全局的
        self.driver.get('http://www.5itest.cn/register')
        log.debug("this is debug")
        self.login = RegisterBusiness(self.driver)

    #unittest后置条件：关闭driver   某一条case的后置条件
    def tearDown(self):
        time.sleep(2)
        #判断当前程序的运行是否有异常  python 3
        #拿到当前运行的错误信息，返回的是list
        for method_name,error in self._outcome.errors:
               if error:
                    case_name = self._testMethodName
                    file_path = os.path.join(os.getcwd() + "/report/" + case_name+".png")
                    self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()


    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','user111','111111',self.file_name)
        #if email_error == True:
            #print("注册成功了，此条case执行失败")
        #通过assert判断是否为error，体现在报告中
        self.assertFalse(email_error,'case执行了')  #返回true 不等于 false ，输出'case执行了'

    def test_login_username_error(self):
        username_error = self.login.login_name_error('3422@163.com', 'ss', '111111', self.file_name)
        #if username_error == True:
            #print("注册成功了，此条case执行失败")
        self.assertFalse(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_code_error('3422@163.com', 'ss1111', '111111', self.file_name)
        #if code_error == True:
            #print("注册成功了，此条case执行失败")
        self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.login.login_password_error('3422@163.com', 'ss1111', '111', self.file_name)
        #if password_error == True:
            #print("注册成功了，此条case执行失败")
        self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.user_base('3422@163.com', 'ss1111', '111111', self.file_name)
        #if self.login.register_success() == True:
            #print("注册成功")
        self.assertFalse(success)

'''
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''


#打开网站->执行不同的case->关闭->打开网站->执行不同的case
if __name__ == '__main__':
    unittest.main()
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    # unittest的容器
    # 只执行第二条case
    # 顺序与添加顺序有关
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    # unittest.TextTestRunner().run(suite)
    # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first123 report", description=u"这个是我们第一次测试报告",
                                           verbosity=2)
    runner.run(suite)
