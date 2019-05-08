#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PIL import Image

#from ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))   #title_contains检查页面是否正确

#element = driver.find_element_by_class_name("controls")
#EC.invisibility_of_element_located(element)   #判断元素是否可见 ，只可找一次
# 通过定位方式，WebDriverWait通过智能等待去找页面元素，
# 只要传入定位的值就可以了，会在规定的时间之内找元素，如果找到了就往下运行，没找到返回false
#locator = (By.CLASS_NAME,"controls")      #定位
#WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))  #判断元素是否可见


#输入的信息与预想的信息是否一致
#email_element = driver.find_element_by_id("register_email")
#print(email_element.get_attribute("placeholder"))  #拿值测试
#email_element.send_keys("login_01@163.com")
#print(email_element.get_attribute("value"))



#解析验证码
driver.save_screenshot("/Users/pmy/Downloads/selenium code/test.png")   #保存整个网页的截图
#从大图片中裁剪出验证码的图片
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)   #得到验证码图片所在的位置坐标，结果格式{"x":123,"y":345}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("/Users/pmy/Downloads/selenium code/test.png")   #调用图片
img = im.crop((left,top,right,height))             #按照坐标裁剪图片
img.save("/Users/pmy/Downloads/selenium code/test1.png")
#图片不对和分配率有关


#接start_browser中的验证码图片截取之后的步骤：解析验证码图片中的文字
#如果干扰项较多的情况下，怎么识别验证码图片中的文字，读写解析图片中的文字
#r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
#r.addBodyPara("typeId","35")   #需读取的图片的类型
#r.addBodyPara("convert_to_jpg","0")
#r.addFilePara("image",r"/Users/pmy/Downloads/selenium code/test1.png")
#res = r.post()
#text = res.json()['showapi_res_body']['Result']   #取json里的showapi_res_body下Result字段的参数
#print(text)  #返回信息

#输入到验证码输入框中
#time.sleep(2)
#driver.find_element_by_id("captcha_code").send_keys(text)


#time.sleep(5)



driver.close()   #创建一个就要关掉一个，因为调用一次就创建一个，所以才会运行的越来越卡




#如何生成多个不同的用户名和邮箱
#for i in range(5):
    #user_email = ''.random.sample('1234567890abcdefg', 5) + "@163.com" #不加''.,结果是个 ['a','b','c','q','2'] 的list,加了''，结果就是字符串abcg2
    #print(user_email)




#driver.find_element_by_id("register_email").send_keys("login_01@163.com")  #通过页面标签中ID定位

# 页面中有四个form-control input-lg，所以会报错：Compound class names not permitted，
# 因为定位的元素不唯一，会看第一个class=form-control input-lg的能否输入，能则输入给第一个
# 改用上一级标签的class+这一级标签的class，如果上一级标签的class+这一级标签的class也是不唯一的，是list表单
# 则改为find_elements_by_class_name，再选取元素对应的下标,如第二个=[1];
#user_name_element_node = driver.find_elements_by_class_name("controls")[1]
#user_name_element = user_name_element_node.find_element_by_class_name("form-control")
#user_name_element.send_keys("pmypmy")                                      #通过页面标签中class定位
#当查看是否返回是多个元素时，用find_elements_by_class_name，再print（len（user_name_element））查看list个数

#driver.find_element_by_name("password").send_keys("123456")  #通过页面标签中name定位

#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")   #通过xpath进行定位












