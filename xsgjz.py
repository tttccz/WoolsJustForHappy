# -*- coding:utf-8 -*-
"""
const $ = new Env("小时工记账");
cron: 15 7,14,20 * * *
"""
# https://market-h5.julanling.com  请求头 authorization（不含Bearer）#请求体中deviceToken
# 变量 xsgjzck, 多变量换行分割
import random
import sys

from notify import *

xsgjzCks = os.environ.get("xsgjzck") if os.environ.get("xsgjzck") else ""
xsgjzCkList = xsgjzCks.split("\n")
if len(xsgjzCkList) == 0 or xsgjzCks == '':
    print('未填写小时工记账环境变量：xsgjzck')
    sys.exit()


def batchListByPositions(bearer, deviceToken):
    url = f'https://market-h5.julanling.com/market-center/api2/assignment/batchListByPositions?positions=MONEY_CENTER_NEW_WELFARE,MONEY_CENTER_DAILY_WELFARE,MONEY_CENTER_GLOBAL_WELFARE,MONEY_CENTER_WEEK_WELFARE&os=ANDROID&appVersion=4.4.50&appChannel=xsgjz_yingyongbao&deviceToken={deviceToken}'
    headers = {
        'Host': 'market-gateway.julanling.com',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {bearer}',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://market-h5.julanling.com',
        'x-requested-with': 'com.julangling.xsgjz',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://market-h5.julanling.com/market-mobile/?backConfirm=true&titleHide=true&hideBack=true&needRefresh=true&position=tab&systemSource=XSG',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    resp = requests.get(url=url, headers=headers, timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        return res['results']['assignmentListResp']['MONEY_CENTER_DAILY_WELFARE']['assignments'], res['results'][
            'balance']
    else:
        print(res['errorStr'])
        return None, None


def receiveAwardByBusinessType(bearer, deviceToken, businessType):
    url = f'https://market-gateway.julanling.com/market-center/api2/assignment/receiveAwardByBusinessType'
    payload = {
        "os": "ANDROID",
        "appVersion": "4.4.50",
        "appChannel": "xsgjz_yingyongbao",
        "deviceToken": deviceToken,
        "businessType": businessType
    }
    headers = {
        'Host': 'market-gateway.julanling.com',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {bearer}',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://market-h5.julanling.com',
        'x-requested-with': 'com.julangling.xsgjz',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://market-h5.julanling.com/market-mobile/?backConfirm=true&titleHide=true&hideBack=true&needRefresh=true&position=tab&systemSource=XSG',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(payload), timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        print(f'领取奖励成功：获得{res["results"]["awardInfos"][0]["amount"]}金币')
    else:
        print(f'领取奖励失败：{res["errorStr"]}')


def signIn(bearer, deviceToken):
    url = f'https://market-gateway.julanling.com/market-center/api2/signIn/signIn'
    payload = {
        "os": "ANDROID",
        "appVersion": "4.4.50",
        "appChannel": "xsgjz_yingyongbao",
        "deviceToken": deviceToken
    }
    headers = {
        'Host': 'market-gateway.julanling.com',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Bearer {bearer}',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://market-h5.julanling.com',
        'x-requested-with': 'com.julangling.xsgjz',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://market-h5.julanling.com/market-mobile/?backConfirm=true&titleHide=true&hideBack=true&needRefresh=true&position=tab&systemSource=XSG',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(payload), timeout=20)
    res = resp.json()
    # print(res)
    if res['errorCode'] == 0:
        print(f'签到成功：获得{res["results"]["amount"]}金币，已连续签到{res["results"]["continuousDays"]}天')
    else:
        print(f'签到失败：{res["errorStr"]}')


def detailCore(bearer, deviceToken):
    url = f'https://market-gateway.julanling.com/market-center/api2/dial/detailCore?appChannel=xsgjz_yingyongbao&appVersion=4.4.50&appPackage=com.julangling.xsgjz&deviceToken={deviceToken}&operatingSystem=ANDROID'
    headers = {
        "Host": "market-gateway.julanling.com",
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {bearer}",
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        "content-type": "application/json",
        "origin": "https://xsg-api.julanling.com",
        "x-requested-with": "com.julangling.xsgjz",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://xsg-api.julanling.com/pages/actives/turntable/index.html",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.get(url=url, headers=headers, timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        currentProgress = res["results"]['dialBoxResp']['currentProgress']
        dialValidNum = res["results"]['dialValidNum']
        goldAmount = res["results"]['goldAmount']
        print(
            f'当前总共{goldAmount}金币，本日已抽奖{currentProgress}次，当前时段还有{dialValidNum}次抽奖机会')
        return int(currentProgress), int(dialValidNum)
    else:
        print(f'{res["errorStr"]}')
        return 0, 0


def gachaIndex(bearer, deviceToken):
    url = f'https://market-gateway.julanling.com/market-center/api2/gacha/index?deviceToken={deviceToken}&version=4.4.50&os=ANDROID&appVersion=4.4.50&appChannel=xsgjz_yingyongbao'
    headers = {
        "Host": "market-gateway.julanling.com",
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {bearer}",
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        "content-type": "application/json",
        "origin": "https://h5.julanling.com",
        "x-requested-with": "com.julangling.xsgjz",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://h5.julanling.com/twist_egg/index.html?backConfirm=true&titleHide=true&systemSource=XSG&xsgBack=true",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.get(url=url, headers=headers, timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        remainTimes = res["results"]['remainTimes']
        remainVideoTimes = res["results"]['remainVideoTimes']
        print(f'本日还有{remainTimes}次扭蛋机会，还剩{remainVideoTimes}次观看视频获取扭蛋机会')
        return int(remainTimes), int(remainVideoTimes)
    else:
        print(f'{res["errorStr"]}')
        return 0, 0


def luckDraw(bearer, deviceToken):
    url = f'https://xsg-api.julanling.com/market-center/api2/dial/luckyDraw'
    payload = {
        "appChannel": "xsgjz_yingyongbao",
        "appVersion": "4.4.50",
        "appPackage": "com.julangling.xsgjz",
        "deviceToken": deviceToken,
        "operatingSystem": "ANDROID"
    }
    headers = {
        "Host": "market-gateway.julanling.com",
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {bearer}",
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        "content-type": "application/json",
        "origin": "https://xsg-api.julanling.com",
        "x-requested-with": "com.julangling.xsgjz",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://xsg-api.julanling.com/pages/actives/turntable/index.html",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(payload), timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        currentProgress = res["results"]['dialBoxResp']['currentProgress']
        dialValidNum = res["results"]['dialValidNum']
        goldAmount = res["results"]['goldAmount']
        if 'amount' in str(res["results"]):
            amount = res["results"]['amount']
        else:
            amount = 0
        print(
            f'抽奖成功：获得{amount}金币，当前总共{goldAmount}金币，本日已抽奖{currentProgress}次，当前时段还有{dialValidNum}次抽奖机会')
        return int(currentProgress), int(dialValidNum)
    else:
        print(f'抽奖失败：{res["errorStr"]}')
        return 0, 0


def openBox(bearer, deviceToken, type):
    url = f'https://market-gateway.julanling.com/market-center/api2/dial/openBox'
    payload = {
        "businessType": f"XSG_BOX_{type}",
        "appChannel": "xsgjz_yingyongbao",
        "appVersion": "4.4.50",
        "appPackage": "com.julangling.xsgjz",
        "deviceToken": deviceToken,
        "operatingSystem": "ANDROID"}
    headers = {
        "Host": "market-gateway.julanling.com",
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {bearer}",
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        "content-type": "application/json",
        "origin": "https://xsg-api.julanling.com",
        "x-requested-with": "com.julangling.xsgjz",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://xsg-api.julanling.com/pages/actives/turntable/index.html",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(payload), timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        currentProgress = res["results"]['dialBoxResp']['currentProgress']
        goldAmount = res["results"]['goldAmount']
        openBoxAwards = res["results"]['openBoxAwards']
        amount = 0
        bizNo = None
        for award in openBoxAwards:
            if award['awardType'] == 'GOLD':
                amount = award['amount']
            if award['awardType'] == 'DOUBLE_VIDEO':
                bizNo = award['bizNo']
        print(f'抽奖成功：获得{amount}金币，当前总共{goldAmount}金币，本日已抽奖{currentProgress}次')
        return bizNo
    else:
        print(f'抽奖失败：{res["errorStr"]}')
        return None


def luckDrawEgg(bearer, deviceToken):
    url = f'https://market-gateway.julanling.com/market-center/api2/gacha/luckyDraw'
    payload = {
        "deviceToken": deviceToken,
        "version": "4.4.50",
        "os": "ANDROID",
        "appVersion": "4.4.50",
        "appChannel": "xsgjz_yingyongbao"
    }
    headers = {
        "Host": "market-gateway.julanling.com",
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {bearer}",
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36;_android{version:4450,versionName:4.4.50,userType:1,sdkVersion:29,statusBarHeight:29,toolBarHeight:73,imei:,oaid:db8b4a33fdf46e78,channel:xsgjz_yingyongbao,uid:10201}_android',
        "content-type": "application/json",
        "origin": "https://h5.julanling.com",
        "x-requested-with": "com.julangling.xsgjz",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://h5.julanling.com/twist_egg/index.html?backConfirm=true&titleHide=true&systemSource=XSG&xsgBack=true",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(payload), timeout=20)
    res = resp.json()
    if res['errorCode'] == 0:
        name = res["results"]['name']
        remainTimes = res["results"]['remainTimes']
        print(f'扭蛋成功：获得{name}，本日还有{remainTimes}次扭蛋机会')
        return int(dialValidNum)
    else:
        print(f'扭蛋失败：{res["errorStr"]}')
        return 0


if __name__ == '__main__':
    global msg, model
    msg = ''
    num = 0
    for user in xsgjzCkList:
        print(f'\n=====开始第{num + 1}账号运行=====\n')
        time.sleep(random.randint(30, 60))
        deviceToken = user.split("#")[1]
        bearer = user.split("#")[0]
        signIn(bearer, deviceToken)
        taskList, coin = batchListByPositions(bearer, deviceToken)
        for taskInfo in taskList:
            statistics = taskInfo['statistics']
            assignmentProcessDesc = taskInfo['assignmentProcessDesc']
            businessType = taskInfo['businessType']
            if businessType == 'XSG_MONEY_CENTER_DIAL_1' or businessType == 'XSG_MONEY_CENTER_GACHA_1':
                hasDrawTimes = int(assignmentProcessDesc.split('">')[1].split('</span>/')[0])
                needDrawTimes = int(assignmentProcessDesc.split('">')[1].split('</span>/')[1].split('</div>')[0])
                remainTimes = taskInfo['assignmentStatusInfo']['remainTimes']

                achieveTimes = int(taskInfo['achieveTimes'])
                if needDrawTimes == hasDrawTimes and achieveTimes == 0:
                    receiveAwardByBusinessType(bearer, deviceToken, businessType)
                    time.sleep(5)

        hasDrawTimes, dialValidNum = detailCore(bearer, deviceToken)
        if dialValidNum > 0:
            for drawTimes in range(0, dialValidNum):
                hasDrawTimes, dialValidNum = luckDraw(bearer, deviceToken)
                time.sleep(5)
                if hasDrawTimes == 5:
                    openBox(bearer, deviceToken, 'ONE')
                if hasDrawTimes == 19:
                    openBox(bearer, deviceToken, 'TWO')
                if dialValidNum == 0:
                    break
        else:
            print('当前时段抽奖次数为0！')

        drawEggTimes, remainVideoTimes = gachaIndex(bearer, deviceToken)
        if drawEggTimes > 0:
            for drawTimes in range(0, drawEggTimes):
                dialValidNum = luckDrawEgg(bearer, deviceToken)
                time.sleep(5)
        else:
            print('扭蛋机抽奖次数为0！')

        # if remainVideoTimes > 0:
        #     for drawTimes in range(0, remainVideoTimes):
        #         dialValidNum = luckDrawEgg(bearer, deviceToken)
        #         time.sleep(5)
        # else:
        #     print('扭蛋机抽奖次数为0！')
        taskList, coin2 = batchListByPositions(bearer, deviceToken)
        diffCoin = int(coin2) - int(coin)
        print(f'账号{num + 1}共有{coin2}金币，本次运行获得{diffCoin}金币')
        msg += f'账号{num + 1}共有{coin2}金币，本次运行获得{diffCoin}金币\n'

    print("\n==========================\n")
    print(msg)
    send("小时工记账", msg)
