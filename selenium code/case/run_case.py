# coding=utf-8
import unittest
import os

#运行所有unittest py文件的主入口

class RunCase(unittest.TestCase):
    def test_case01(self):
        #case_path = os.path.join(os.getcwd(), 'case')
        #print(case_path)
        path = os.getcwd()  #获取项目当前路径
        #print(path)
        suite = unittest.defaultTestLoader.discover(path, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
