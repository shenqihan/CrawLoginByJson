import json
from selenium import webdriver
import time

url = 'https://www.douban.com/'
driver = webdriver.Chrome()

driver.get(url)
# 卡主浏览器 回车继续运行
input('回车自动登录')

driver.get(url)
# 删除第一次建立连接时的cookie
driver.delete_all_cookies()

# 读取本地的cookie文件
with open('zhihu.json', 'r', encoding='utf8') as f:
    listCookies = json.loads(f.read())

for cookie in listCookies:
    driver.add_cookie({
        "domain": ".douban.com",
        "expiry": 1561948479,
        "httpOnly": cookie['httpOnly'],
        "name": cookie['name'],
        "path": "/",
        "secure": cookie['secure'],
        "value": cookie['value']
    })
# 读取完cookie刷新页面
driver.refresh()
input('按回车键退出')
driver.close()


'''

Cookie: _zap=2708a41d-1ade-45a1-b5fd-19f703b5bd8f; _xsrf=gEsuDuFHjQBQ7shnc9UAy0arMfAgeA3l; d_c0="AFDnhOoQIQ6PTgzDsr4fXA3nB0TY_7QLQrY=|1535517195"; tst=h; q_c1=3093837d70994070be115216897f5b9a|1545101827000|1535517514000; __utmc=51854390; __gads=ID=0509fa0acc9a4f85:T=1546093285:S=ALNI_MZEnKrhVZfEteAv-ihAZDNQb6OpxA; __utma=51854390.1299166473.1546092225.1546170517.1546172529.3; __utmz=51854390.1546172529.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; l_n_c=1; l_cap_id="MjBlMzMwN2NlYjYwNDRmYjg5NWVhZGI3ZjE0NzVhZTA=|1546173339|e746025ddf59e6e3acbdcbc0e916f2dca81e8cbb"; r_cap_id="ZDlkYzBlMjgzMjhmNGExYTg5MDE3NDJhZDE4MjUwZWQ=|1546173339|67eec163442e922e1730c71bd1c999cd083072fc"; cap_id="YmNkNWI1MjNhYTlmNDEzM2IwZjNjZWE0NTJkNzZiZGU=|1546173339|9c813760edef6bbc901bd970c97ccdefdd41cc94"; n_c=1; __utmv=51854390.000--|2=registration_date=20180828=1^3=entry_date=20180829=1; auth_type=cXFjb25u|1546173376|981b57eca7f1dd32fd46772ccb7e1ef775cefd15; token="NkY2Rjg0RTdDNTNEOUQ5QTMxRjVERTdDMUQxQkEzQ0M=|1546173376|8ecd2e60573298768f7b934e6318422c94c7aed6"; client_id="OTg3RDlENzdBQzIwQzAwQTBDOENBOTVFNDhCOTE1MUU=|1546173376|ffeffb7bbeb31740fd135c564f65383d9c0bc63a"; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; capsion_ticket="2|1:0|10:1546180684|14:capsion_ticket|44:MGNjYWNjZGVjYzAwNDI3ZWJiYjZlZTA0YjRiYThhYWM=|3b86e74a607718cecb2f58afe264edbf30dbf1301ca81daf54dd6db07299046f"

'''