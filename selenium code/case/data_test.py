#coding = utf-8

import ddt
import  unittest

@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("this is setUp")
    def tearDown(self):
        print("this is tearDown")

    #1,2  3,4  5,6 弄成数据统一管理

    @ddt.data(
        ["1", "2"],
        ["3", "4"],
        ["5", "6"]
    )
    @ddt.unpack    #解包
    def test_add(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()