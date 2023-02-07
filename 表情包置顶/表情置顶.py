import requests
import json
import hashlib
import time
import fileinput

sblist = []

for line in open("itemid.txt"):
    newstr = line.strip()
    print(newstr)
    sblist.append(newstr)



# print(sblist)

with open('bqcookie.txt', encoding='utf-8') as a:
    # 读取文件
    result = json.load(a)
    # 获取姓名
    # print(result.get('cookie'))  # 熊猫
    # # 获取城市
    # print(result.get('csrf'))  # 上海



hl = hashlib.md5()

acckey = result.get('access_key')


id = result.get('item_id')

appsec = "560c52ccd288fed045859ed18bffd973"

#
# id = 2954




def now():
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }

    response = requests.get('http://api.bilibili.com/x/report/click/now',  headers=headers,
                            verify=False)

    ts = response.text
    jsonobj = json.loads(ts)
    nowww = jsonobj['data']['now']

    return nowww


def name():
    zhi = f'item_id={id}&part=suit'
    url = 'https://api.bilibili.com/x/garb/mall/item/suit/v2?' + zhi  # 记得重新修改请求号
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    r = requests.get(url, headers=headers)
    text = r.text
    jsonobj = json.loads(text)
    name = jsonobj['data']['suit_items']['emoji_package'][0]['items'][0]['name']
    nname = jsonobj['data']['item']["name"]
    print(nname)
    return name






def find():

    ac = f'access_key={acckey}&appkey=1d8b6e7d45233436&build=6460400&business=reply&c_locale=zh_CN&channel=yingyonghui&mobi_app=android&platform=android&s_locale=zh_CN&statistics=%7B"appId"%3A1%2C"platform"%3A3%2C"version"%3A"6.46.0"%2C"abtest"%3A""%7D&ts={now()}'
    sign = ac + appsec
    # print(sign)
    hl.update(sign.encode(encoding='utf-8'))
    ssgin = ac+"&sign="+hl.hexdigest()

    # print(ssgin)

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }


    response = requests.get('https://api.biliapi.net/x/emote/setting/panel', params=ssgin, headers=headers)
    tex = response.text
    js = json.loads(tex)

    code = js['code']
    if code != 0:
        print("acckey输入错误  请关闭程序重新填写")
        input("-----")



    int_count = 0
    wd = tex[:tex.rfind(f',"text":"{name()}')][-10:]   #id=装扮编号

    # print(wd)
    # fuck = wd[:wd.rfind(',"te')][-5:]
    # print(wd)

    for i in wd:
        # 判断是否为数字
        if i.isdigit():
            int_count += 1

    # print("数字 = %d" % (int_count))

    # fffuck = fuck[-2:]



    if int_count == 2:
        fffuck = wd[-2:]
        print("对应表情id：" + str(fffuck))
        return fffuck
    if int_count == 3:
        fffuck = wd[-3:]
        print("对应表情id：" + str(fffuck))
        return fffuck
    if int_count == 4:
        fffuck = wd[-4:]
        print("对应表情id：" + str(fffuck))
        return fffuck

    else:
        print("bug----请反馈相应的装扮")
        print(wd)




# find()





# find()


def zhiding():
    acce = f'access_key={acckey}&appkey=1d8b6e7d45233436&build=6460400&business=reply&c_locale=zh_CN&channel=yingyonghui&mobi_app=android&platform=android&s_locale=zh_CN&sort={find()}&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.46.0%22%2C%22abtest%22%3A%22%22%7D&ts={now()}'
    sign = acce + appsec
    # print(sign)
    hl.update(sign.encode(encoding='utf-8'))
    sssgin = acce + "&sign=" + hl.hexdigest()
    # print(sssgin)






    headers = {
    "env": "prod",
    "APP-KEY":"android",
    "User-Agent": "Mozilla/5.0 BiliDroid/6.46.0(bbcallen @ gmail.com) os/android model/VOG-AL10mobi_app/android build/6460400 channel/yingyonghui innerVer/6460400 osVer/5.1.1 network/2",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Content-Length": "350",
    "Host": "api.biliapi.net",
    "Connection": "Keep-Alive",
    "Accept - Encoding": "gzip",

    }

    resp = requests.post('https://api.biliapi.net/x/emote/package/sort', headers=headers, data=sssgin)
    te = resp.text

    print(te)
    print("请求成功  如果code:0就是修改成功  不然就自己看提示吧\n")


sbblist = reversed(sblist)


for id in sbblist:
     int_coun = 0
     for i in id:
         # 判断是否为数字
          if i.isdigit():
            int_coun += 1
     # print("数字 = %d" % (int_coun))
     if int_coun == 0:
        print("空文本--跳过")
        continue
     name()
     zhiding()



input("运行完毕\n")