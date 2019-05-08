#coding =utf-8

#通过读取read_ini文件下的ReadIni类，来对获取的配置文件中的数据进行定位和定位元素的封装
#还有进行了容错处理

from util.read_ini import ReadIni


class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_classname(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return  None