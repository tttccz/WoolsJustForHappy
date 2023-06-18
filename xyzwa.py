# -*- coding:utf-8 -*-
"""
const $ = new Env("5天5元微信红包");
cron: 0 12 7,12,18,21 * * *
desc: 小程序，5天5元红包，抓完包不要再登录，等到500分再去登录换红包，大毛，走下我链接，链接在read.me
"""
import hashlib
import os
import sys
import time

import requests

from notify import send

xiaoyangCks = os.environ.get("XYZWA_USER") if os.environ.get(
    "XYZWA_USER") else ""
xiaoyangList = xiaoyangCks.split("\n")
if len(xiaoyangList) == 0 or xiaoyangList == '':
    print('未填写5天5元微信红包环境变量：XYZWA_USER')
    sys.exit()


def wakeSleepSign(token, type):
    url = "https://sleepapi.25youpin.com/api/wakeSleep/sign"
    ts = int(time.time())
    payload = f'type={type}'
    raw = f"sleepEarly_apitype{type}timestamp{ts}sleepEarly_api"
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest()
    headers = {
        'Host': 'sleepapi.25youpin.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'X-Token': token,
        'content-type': 'application/x-www-form-urlencoded',
        'api-version': 'v1.0.0',
        'x-dlab-os-version': 'iOS 15.6.1',
        'request-source': 'mini',
        'x-dlab-model': 'iPhone 12<iPhone13,2>',
        'x-dlab-brand': 'iPhone',
        'sdk-version': '2.27.1',
        'sign': sign,
        'timestamp': f'{ts}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a502135f9cc0943/42/page-frame.html'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


def userInfo(token):
    url = "https://sleepapi.25youpin.com/api/user/info"
    ts = int(time.time())
    raw = f"sleepEarly_apitimestamp{ts}sleepEarly_api"
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest()
    payload = {}
    headers = {
        'Host': 'sleepapi.25youpin.com',
        'Connection': 'keep-alive',
        'X-Token': token,
        'content-type': 'application/x-www-form-urlencoded',
        'api-version': 'v1.0.0',
        'x-dlab-os-version': 'iOS 15.0.2',
        'request-source': 'mini',
        'x-dlab-model': 'iPhone 7<iPhone9,1>',
        'x-dlab-brand': 'iPhone',
        'sdk-version': '2.27.1',
        'sign': sign,
        'timestamp': f'{ts}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252f) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a502135f9cc0943/46/page-frame.html'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    return res


def setRepairSign(token):
    url = "https://sleepapi.25youpin.com/api/user/setRepairSign"
    ts = int(time.time())
    raw = f"sleepEarly_apitimestamp{ts}sleepEarly_api"
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest()
    payload = {}
    headers = {
        'Host': 'sleepapi.25youpin.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'X-Token': token,
        'content-type': 'application/x-www-form-urlencoded',
        'api-version': 'v1.0.0',
        'x-dlab-os-version': 'iOS 15.6.1',
        'request-source': 'mini',
        'x-dlab-model': 'iPhone 12<iPhone13,2>',
        'x-dlab-brand': 'iPhone',
        'sdk-version': '2.27.1',
        'sign': sign,
        'timestamp': f'{ts}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a502135f9cc0943/42/page-frame.html'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    print(res)


def getSign(token):
    url = "https://sleepapi.25youpin.com/api/wakeSleep/getSign"
    ts = int(time.time())
    raw = f"sleepEarly_apitimestamp{ts}sleepEarly_api"
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest()
    payload = {}
    headers = {
        'Host': 'sleepapi.25youpin.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'X-Token': token,
        'content-type': 'application/x-www-form-urlencoded',
        'api-version': 'v1.0.0',
        'x-dlab-os-version': 'iOS 15.6.1',
        'request-source': 'mini',
        'x-dlab-model': 'iPhone 12<iPhone13,2>',
        'x-dlab-brand': 'iPhone',
        'sdk-version': '2.27.1',
        'sign': sign,
        'timestamp': f'{ts}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a502135f9cc0943/42/page-frame.html'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    return res


def tabStatus(token):
    url = "https://sleepapi.25youpin.com/api/user/tabStatus"
    ts = int(time.time())
    raw = f"sleepEarly_apitimestamp{ts}sleepEarly_api"
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest()
    payload = {}
    headers = {
        'Host': 'sleepapi.25youpin.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'X-Token': token,
        'content-type': 'application/x-www-form-urlencoded',
        'api-version': 'v1.0.0',
        'x-dlab-os-version': 'iOS 15.6.1',
        'request-source': 'mini',
        'x-dlab-model': 'iPhone 12<iPhone13,2>',
        'x-dlab-brand': 'iPhone',
        'sdk-version': '2.27.1',
        'sign': sign,
        'timestamp': f'{ts}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a502135f9cc0943/42/page-frame.html'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    return res


def getUserSheep(token):
    url = "https://sleepapi.25youpin.com/api/user/getUserSheep?page=1&size=20&type=0"
    ts = int(time.time())
    raw = f"sleepEarly_apipage{1}size{20}type{0}timestamp{ts}sleepEarly_api"
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest()
    payload = {}
    headers = {
        'Host': 'sleepapi.25youpin.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'X-Token': token,
        'content-type': 'application/x-www-form-urlencoded',
        'api-version': 'v1.0.0',
        'x-dlab-os-version': 'iOS 15.6.1',
        'request-source': 'mini',
        'x-dlab-model': 'iPhone 12<iPhone13,2>',
        'x-dlab-brand': 'iPhone',
        'sdk-version': '2.27.1',
        'sign': sign,
        'timestamp': f'{ts}',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252e) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wx5a502135f9cc0943/42/page-frame.html'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    return res


if __name__ == '__main__':
    global msg
    msg = ''
    num = 0
    for token in xiaoyangList:
        num += 1
        print(f"\n====开始账号{num}运行任务======\n")
        getSign_ = getSign(token)
        if getSign_['code'] == 200:
            type = getSign_['data']['type']
            desc = getSign_['data']['desc']
            print(f"账号{num} {desc}")
        else:
            print(f"账号{num} {getSign_['msg']}")
            msg += f"账号{num} {getSign_['msg']}\n"
            continue
        time.sleep(1)
        if '可' in desc:
            wakeSleepSign_ = wakeSleepSign(token, type)
            if wakeSleepSign_['code'] == 200:
                print(f"账号{num} 打卡成功")
            else:
                print(f"账号{num} 打卡失败：{wakeSleepSign_['msg']}")
            time.sleep(1)
        getUserSheep_ = tabStatus(token)
        if getUserSheep_['code'] == 200:
            total = int(getUserSheep_['data']['sheep'])
        else:
            print(f"账号{num} {getUserSheep_['msg']}\n")
            msg += f"账号{num} {getUserSheep_['msg']}\n"
            continue
        userInfo_ = userInfo(token)
        if userInfo_['code'] == 200:
            wake_days = userInfo_['data']['wake_days']
            sleep_days = userInfo_['data']['sleep_days']
            nickname = userInfo_['data']['nickname']
            print(f"账号{num} {nickname} 早起打卡{wake_days}天，早睡打卡{sleep_days}天，当前积分：{total}\n")
            msg += f"账号{num} {nickname} 早起打卡{wake_days}天，早睡打卡{sleep_days}天，当前积分：{total}\n"
        else:
            print(f"账号{num} {userInfo_['msg']}\n")
            msg += f"账号{num} {userInfo_['msg']}\n"
        time.sleep(2)

    send('5天5元微信红包', msg)
