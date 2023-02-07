import requests
import json
import time
import pandas as pd
import openpyxl
from collections import Counter
#
# df=pd.read_excel('个性装扮骗子总集.xlsx')
# print("输出值",df.sample(3).values)#这个方法类似于head()方法以及df.values方法

with open('a.json', encoding='utf-8') as a:
    # 读取文件
    result = json.load(a)
    # 获取姓名
    # print(result.get('cookie'))  # 熊猫
    # # 获取城市
    # print(result.get('csrf'))  # 上海



cookie = result.get('cookie')   #举个栗子  实际的长度要长一些
# print(cookie)
# csrf = result.get('csrf')  #再举个栗子   实际的长度要长一些   这玩意和bili_jct的数据是一样的  在cookie里找找
ccsrf =  cookie.split(";")[1]
csrf = ccsrf.split("=")[1]
# print(csrf)






sblist = []
ssblist = []

for line in open("拉黑UID.txt"):
    newstr = line.strip()
    # print(newstr)
    sblist.append(newstr)
print("提取-拉黑UID.txt成功")

for ssbb in open("取消拉黑UID.txt"):
    newstr = ssbb.strip()
    # print(newstr)
    ssblist.append(newstr)
print("读取-取消拉黑UID.txt成功")


# uuid = 253042446





def lahei():



    headers = {
        'authority': 'api.bilibili.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'origin': 'https://space.bilibili.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://space.bilibili.com/{uuid}?spm_id_from=333.337.0.0',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': f"{cookie}",
    }





    data = {
        'fid': f'{uuid}',
        'act': f'{act}',
        're_src': '11',
        'spmid': '333.999.0.0',

        'jsonp': 'jsonp',
        'csrf': f'{csrf}',
    }

    response = requests.post('https://api.bilibili.com/x/relation/modify', headers=headers, data=data)

    text = response.text
    jsonobj = json.loads(text)
    code = jsonobj['code']
    if code == 0:

        print(hehe + "成功:uid " + str(uuid))
    if code == 22013:
        print(jsonobj)
    if code != 0 and code != 22013:
        print(jsonobj)
        input("如果不是账号未登录或csrf错误   请反馈此bug---并关闭程序")

def name():
    headers = {
        'authority': 'api.bilibili.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'origin': 'https://space.bilibili.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://space.bilibili.com/{uuid}?spm_id_from=333.337.0.0',
        'accept-language': 'zh-CN,zh;q=0.9',

    }

    params = {
        'mid': f'{uuid}',
        'token': '',
        'platform': 'web',
        'wts': '1674924573',
    }

    response = requests.get('https://api.bilibili.com/x/space/wbi/acc/info', params=params,
                            headers=headers)

    text = response.text
    jss = json.loads(text)
    code = jss['code']

    if code == 0:
        # print("活")
        lahei()
    if code == -404:
        print("该账户已注销或找不到 跳过")
    if code != 0 and code != -404:
        print(text)
        input("出现了预期之外的错误 请反馈并关闭程序")







why = input("拉黑 = 1 ，解除拉黑 = 2，请输入相应数字并按回车 ：")
print(why)

if why != "1" and why != "2":
    print("输入不规范")



if why == "1":
    for uuid in sblist:
        hehe = "拉黑"
        act = 5
        int_coun = 0
        for i in uuid:
            # 判断是否为数字
            if i.isdigit():
                int_coun += 1
        # print("数字 = %d" % (int_coun))
        if int_coun == 0:
            print("空文本--跳过")
            continue
        lahei()
        time.sleep(1)


if why == "2":
    for uuid in ssblist:
        hehe = "解除"
        act = 6
        int_coun = 0
        for i in uuid:
            # 判断是否为数字
            if i.isdigit():
                int_coun += 1
        # print("数字 = %d" % (int_coun))
        if int_coun == 0:
            print("空文本--跳过")
            continue
        lahei()
        time.sleep(1)




input("运行结束")
# lahei()



