import json
from selenium import webdriver
import time

url = 'https://www.douban.com/'
driver = webdriver.Chrome()

driver.get(url)
# 卡主浏览器 回车继续运行
input('请手动登录')

# 获取cookie并通过json模块将dict转换成str
dictCookies = driver.get_cookies()  # 核心
jsonCookies = json.dumps(dictCookies)
print(jsonCookies)
# 登录完成后将cookie保存到本地文件
with open('zhihu.json', 'w') as f:
    f.write(jsonCookies)
time.sleep(3)
driver.close()
