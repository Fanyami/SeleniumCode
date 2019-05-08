#coding = utf-8

import pytesseract
from  PIL import Image
#别的公司提供的处理干扰项多的图片的api接口，他的sdk文件下载到本项目文件下即可调用
from ShowapiRequest import ShowapiRequest

#通过第三方库pytesseract，只能读取干扰性少的图片中的文字提取出来，转换为txt的类型
#识别率不高
#image = Image.open("/Users/pmy/Downloads/selenium code/test2.png")
#text = pytesseract.image_to_string(image)
#print(text)

#接start_browser中的验证码图片截取之后的步骤：解析验证码图片中的文字
#如果干扰项较多的情况下，怎么识别验证码图片中的文字，读写解析图片中的文字
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
r.addBodyPara("typeId","35")   #需读取的图片的类型
r.addBodyPara("convert_to_jpg","0")
r.addFilePara("image",r"/Users/pmy/Downloads/selenium code/test001.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']   #取json里的showapi_res_body下Result字段的参数
print(text)  #返回信息

#输入到验证码输入框中
#time.sleep(2)
#driver.find_element_by_id("captcha_code").send_keys(text)