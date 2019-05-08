#coding = utf-8

import unittest

#case要以test开始，默认才会打印结果testfirst01
class FirstCase01(unittest.TestCase):

    # 所有case的前置条件
    @classmethod
    def setUpClass(cls):
        print("所有case执行的前置条件")

    # 所有case的后置条件
    @classmethod
    def tearDownClass(cls):
        print("所有case执行的后置条件")


    #某一条case的前置条件
    def setUp(self):
        print("某一条case的前置条件")

    # 某一条case的后置条件
    def tearDown(self):
        print("某一条case的前置条件")

    #添加跳过
    #@unittest.skip("不执行第一条")
    def testfirst002(self):
        print("testfirst002")

    def testfirst001(self):
        print("testfirst001")

    #def testfirst02(self):
        #print("testfirst02")

    def testfirst003(self):
        print("testfirst003")


if __name__ == '__main__':
    #unittest.main()

    #unittest的容器
    #只执行第二条case
    #顺序与添加顺序有关
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst002'))
    suite.addTest(FirstCase01('testfirst001'))
    suite.addTest(FirstCase01('testfirst003'))
    unittest.TextTestRunner.run(suite)