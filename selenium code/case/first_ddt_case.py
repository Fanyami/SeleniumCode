#coding = utf-8

import ddt
import unittest
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import os
import HTMLTestRunner
import time
import sys
from util.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()
# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
class FirstDdtCase(unittest.TestCase):

    #unittest前置条件：打开网站  某一条case的前置条件
    def setUp(self):
        self.driver = webdriver.Chrome()      #加self使driver变成全局的
        self.driver.get('http://www.5itest.cn/register')
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

    '''
       @ddt.data(
               ['12','Mushishi01','111111','code','user_email_error','请输入有效的电子邮件地址'],
               ['@qq.com','Mushishi01','111111','code','user_email_error','请输入有效的电子邮件地址'],
               ['12@qq.com','Mushishi01','111111','code','user_email_error','请输入有效的电子邮件地址']
           )
       @ddt.unpack
       '''

    @ddt.data(*data)
    def test_register_case(self, data):
        #list赋值
        email, username, password, self.file_name, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, self.file_name, assertCode, assertText)
        self.assertFalse(email_error, "测试失败")

if __name__ == '__main__':
    unittest.main()
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case.html")
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description=u"这个是我们第一次测试报告1",
                                           verbosity=2)
    runner.run(suite)