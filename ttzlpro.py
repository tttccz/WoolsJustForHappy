# -*- coding:utf-8 -*-
"""
const $ = new Env("天天走路PRO");
cron: 0,30 9-22 * * *
desc: 仅限安卓机使用， 每天1块，多号多薅
      下载地址 http://www.1y2y.com/game/187171.html
"""
# https://apittzlpro.cengaw.cn/api/XXXX  请求头 deviceId#Authorization
# 变量 ttzlprock, 多变量换行分割
import random
import sys

from notify import *

ttzlproCks = os.environ.get("ttzlprock") if os.environ.get(
    "ttzlprock") else ""
ttzlproCkList = ttzlproCks.split("\n")
if len(ttzlproCkList) == 0 or ttzlproCks == '':
    print('未填写天天走路PRO环境变量：ttzlprock')
    sys.exit()

adType = {
    "redRain": {
        "class": 10000,
        "channel": 2,
        "type": 3,
        "ecpm": "6000.0",
        "platformname": 3
    },
    "homeBubble": {
        "class": 10000,
        "channel": 2,
        "type": 23,
        "ecpm": "6000.0",
        "platformname": 3
    },
    "sign": {
        "class": 10002,
        "channel": 2,
        "type": 2,
        "ecpm": "1295.0",
        "platformname": 6
    },
    "zuan": {
        "class": 10000,
        "channel": 2,
        "type": 9,
        "ecpm": "1075.0",
        "platformname": 6
    },
    "news": {
        "class": 10000,
        "channel": 2,
        "type": 6,
        "ecpm": "1175.0",
        "platformname": 6
    },
    "video": {
        "class": 10000,
        "channel": 2,
        "type": 7,
        "ecpm": "1299.0",
        "platformname": 6
    }
}


def getParam(type):
    if type == 'rain':
        class1 = adType['redRain']['class']
        channel = adType['redRain']['channel']
        type2 = adType['redRain']['type']
        platformname = adType['redRain']['platformname']
    elif type == 'bubble':
        class1 = adType['homeBubble']['class']
        channel = adType['homeBubble']['channel']
        type2 = adType['homeBubble']['type']
        platformname = adType['homeBubble']['platformname']
    elif type == 'sign':
        class1 = adType['sign']['class']
        channel = adType['sign']['channel']
        type2 = adType['sign']['type']
        platformname = adType['sign']['platformname']
    elif type == 'zuan':
        class1 = adType['zuan']['class']
        channel = adType['zuan']['channel']
        type2 = adType['zuan']['type']
        platformname = adType['zuan']['platformname']
    elif type == 'news':
        class1 = adType['news']['class']
        channel = adType['news']['channel']
        type2 = adType['news']['type']
        platformname = adType['news']['platformname']
    elif type == 'video':
        class1 = adType['video']['class']
        channel = adType['video']['channel']
        type2 = adType['video']['type']
        platformname = adType['video']['platformname']
    return class1, channel, type2, platformname


def getHeader(authorization, deviceId, proxyAuthorization=None, proxy_type='xk'):
    headers = {
        "accept": "application/json",
        "device": deviceId,
        "oaid": deviceId,
        "store": "juliang",
        "version": "106",
        "platform": "1",
        "Authorization": f"Bearer {authorization}",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 10; {model} MIUI/V12.5.4.0.QFHCNXM)",
        "Host": "apittzlpro.cengaw.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    if proxy_type == 'jl':
        headers['Proxy-Authorization'] = f'Basic {proxyAuthorization}'
    return headers


def loadAd(authorization, deviceId, type, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    class1, channel, type, platformname = getParam(type)
    url = f'https://apittzlpro.cengaw.cn/api/v2/ads/action/load?class={class1}&&channel={channel}&type={type}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        print('加载广告成功')
        return res['result']
    else:
        return None


def showedAd(authorization, deviceId, type, tid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    class1, channel, type, platformname = getParam(type)
    ecpm = '6000.0'
    url = f'https://apittzlpro.cengaw.cn/api/v2/ads/action/showed?class={class1}&channel={channel}&type={type}&ecpm={ecpm}&tid={tid}&platformname={platformname}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']
    else:
        print('展示广告失败！')
        return None


def clickedAd(authorization, deviceId, type, tid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    class1, channel, type, platformname = getParam(type)
    ecpm = '6000.0'
    url = f'https://apittzlpro.cengaw.cn/api/v2/ads/action/clicked?class={class1}&channel={channel}&type={type}&ecpm={ecpm}&tid={tid}&platformname={platformname}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']
    else:
        # print('模拟点击一次广告')
        return None


def compeletedAd(authorization, deviceId, type, tid, ticket='', proxy=None, proxyAuthorization=None, proxy_type='xk'):
    class1, channel, type, platformname = getParam(type)
    ecpm = '6000.0'
    url = f'https://apittzlpro.cengaw.cn/api/v2/ads/action/completed?class={class1}&type={type}&ticket={ticket}&ecpm={ecpm}&tid={tid}&platformname={platformname}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        print('广告观看完成！')
        if ticket != '':
            coin = res['result']['reward']
            coupon = res['result']['coupon']
            print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
        return res['result']
    else:
        return None


def initAd(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/ads/action/init'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['success']
    else:
        return None


def getBubble(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/bubble'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        interval = int(res['result']['interval'])
        hasChance = interval == 0
        if hasChance:
            print('查询气泡广告状态成功：可以观看广告')
            return True
        else:
            print(f'查询气泡广告状态成功：还剩{interval}秒可以查看广告')
        return False
    else:
        return False


def postBubble(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/bubble'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.post(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['coin']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def getBubble2(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/bubble2'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        interval = int(res['result']['interval'])
        hasChance = interval == 0
        if hasChance:
            print('查询气泡2广告状态成功：可以观看广告')
            return True
        else:
            print(f'查询气泡2广告状态成功：还剩{interval}秒可以查看广告')
        return False
    else:
        return False


def postBubble2(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/bubble2'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.post(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['coin']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def signState(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/sign'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        hasSign = False
        items = res['result']['items']
        for item in items:
            if '今天' in item['days']:
                hasSign = item['status']
                break
        if hasSign:
            print('今日已签到')
        else:
            print(f'今日尚未签到')
        return hasSign
    else:
        return False


def postSign(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/sign'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.post(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['coin']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def getRedRain(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/rain'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        red_e = int(res['result']['red_e'])
        red_e_show_ad = int(res['result']['red_e_show_ad'])
        red_e_time = int(res['result']['red_e_time'])
        hasChance = red_e != 0
        if hasChance:
            print(f'查询红包雨广告状态成功：可以观看广告，本日剩余{red_e_show_ad}机会')
        else:
            print(f'查询红包雨广告状态成功：还剩{red_e_time}秒可以查看广告，本日剩余{red_e_show_ad}机会')
        return hasChance
    else:
        return False


def postRedRain(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/reward/rain'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.post(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['coin']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def getMyInfo(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/member/profile'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    try:
        res = resp.json()
        if res['success']:
            nickname = res['result']['nickname']
            point = res['result']['point']
            ticket = res['result']['ticket']
            print(f'获取用户信息成功：{nickname},{point}金币,{ticket}提现券')
            return nickname, point, ticket
        else:
            print(f'获取用户信息失败：{str(res)}')
            return None, None, None
    except:
        print(f'获取用户信息失败：{str(res)}')
        return None, None, None


def getZuanTicket(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/zhuan/video'
    payload = f"type=1"
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']['ticket']
    return None


def getZuanIndex(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/zhuan/index'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.post(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']['items']
    return None


def newsCost(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/news/cost'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        print('阅读新闻计时开始')


def newsCoin(authorization, deviceId, ticket='', proxy=None, proxyAuthorization=None, proxy_type='xk'):
    if ticket == '':
        url = f'https://apittzlpro.cengaw.cn/api/v2/news/coin'
    else:
        url = f'https://apittzlpro.cengaw.cn/api/v2/news/coin?ticket={ticket}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    # print(str(res))
    if res['success']:
        if ticket == '':
            return res['result']
        else:
            reward = res['result']['reward']
            print(f'领取奖励成功：获得{reward}金币')
            return res['result']


def videoCost(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/video/cost?type=short'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        print('观看短视频计时开始')


def videoCoin(authorization, deviceId, ticket='', proxy=None, proxyAuthorization=None, proxy_type='xk'):
    if ticket == '':
        url = f'https://apittzlpro.cengaw.cn/api/v2/video/coin'
    else:
        url = f'https://apittzlpro.cengaw.cn/api/v2/video/coin?ticket={ticket}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    # print(str(res))
    if res['success']:
        if ticket == '':
            return res['result']
        else:
            reward = res['result']['reward']
            print(f'领取奖励成功：获得{reward}金币')
            return res['result']


def redEnv(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/news/redenv'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['reward']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def redVideoEnv(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/video/redenv'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['reward']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def done(authorization, deviceId, id, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/zhuan/done'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    payload = f'id={id}'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['coin']
        coupon = res['result']['coupon']
        print(f'领取奖励成功：获得{coin}金币,{coupon}提现券')
    else:
        print(f'领取奖励失败：{str(res)}')


def newsCount(authorization, deviceId, isOpen, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/news/sdk/zhuan/count?isfirstopen={isOpen}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        print(f'当前文章阅读进度{res["result"]["count"]}/{res["result"]["max"]}')


def getKanList(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/kan/index?page=1&per_page=200'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']['data']


def clickKan(authorization, deviceId, id, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/kan/click?id={id}'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']['ticket']


def getKanPrize(authorization, deviceId, id, ticket, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/kan/index'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    payload = f'id={id}&ticket={ticket}'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        coin = res['result']['coin']
        print(f'领取奖励成功：获得{coin}金币')
    else:
        print(f'领取奖励失败：{str(res)}')


def exchange(authorization, deviceId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/cash/exchange'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    resp = requests.get(url=url, headers=headers, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        return res['result']


def postExchange(authorization, deviceId, mount, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'https://apittzlpro.cengaw.cn/api/v2/cash/exchange'
    headers = getHeader(authorization, deviceId, proxyAuthorization, proxy_type)
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    payload = f'gate=wechat&amount={mount}&lat=&lng=&root=0&sim=1&debug=1&model={model}&power=0&vpn=0'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['success']:
        print(res['result']['message'])
        return True
    return False


if __name__ == '__main__':
    global msg, model
    msg = ''
    models = ['Redmi Note 7 Pro', 'MI 8', 'MI 9']
    try:
        random.shuffle(ttzlproCkList)
        for ttzlproCK in ttzlproCkList:
            model = models[random.randint(0, len(models) - 1)]
            print("随机等待60-100秒")
            time.sleep(random.randint(60, 100))
            deviceId = ttzlproCK.split("#")[0]
            authorization = ttzlproCK.split("#")[1]
            myInfo = getMyInfo(authorization, deviceId)
            if myInfo[0] is None:
                continue
            time.sleep(random.randint(1, 3))
            hasSign = signState(authorization, deviceId)
            time.sleep(random.randint(1, 3))
            if not hasSign:
                adInfo = loadAd(authorization, deviceId, 'sign')
                time.sleep(random.randint(2, 3))
                tid = adInfo['tid']
                showedAd(authorization, deviceId, 'sign', tid)
                time.sleep(random.randint(2, 3))
                initAd(authorization, deviceId)
                print('随机等待15-20秒')
                time.sleep(random.randint(2, 5))
                clickedAd(authorization, deviceId, 'sign', tid)
                time.sleep(random.randint(15, 20))
                compeletedAd(authorization, deviceId, 'sign', tid)
                time.sleep(random.randint(2, 3))
                postSign(authorization, deviceId)
            bubbleChance = getBubble(authorization, deviceId)
            if bubbleChance:
                adInfo = loadAd(authorization, deviceId, 'bubble')
                time.sleep(random.randint(2, 3))
                tid = adInfo['tid']
                showedAd(authorization, deviceId, 'bubble', tid)
                time.sleep(random.randint(2, 3))
                initAd(authorization, deviceId)
                print('随机等待15-20秒')
                time.sleep(random.randint(2, 5))
                clickedAd(authorization, deviceId, 'sign', tid)
                time.sleep(random.randint(15, 20))
                compeletedAd(authorization, deviceId, 'bubble', tid)
                time.sleep(random.randint(2, 3))
                postBubble(authorization, deviceId)
            time.sleep(random.randint(1, 3))
            bubble2Chance = getBubble2(authorization, deviceId)
            if bubble2Chance:
                adInfo = loadAd(authorization, deviceId, 'bubble')
                time.sleep(random.randint(2, 3))
                tid = adInfo['tid']
                showedAd(authorization, deviceId, 'bubble', tid)
                time.sleep(random.randint(2, 3))
                initAd(authorization, deviceId)
                print('随机等待15-20秒')
                time.sleep(random.randint(2, 5))
                clickedAd(authorization, deviceId, 'bubble', tid)
                time.sleep(random.randint(15, 20))
                compeletedAd(authorization, deviceId, 'bubble', tid)
                time.sleep(random.randint(2, 3))
                postBubble2(authorization, deviceId)
            time.sleep(random.randint(1, 3))
            hasRedRainChance = getRedRain(authorization, deviceId)
            time.sleep(random.randint(1, 3))
            if hasRedRainChance:
                adInfo = loadAd(authorization, deviceId, 'rain')
                time.sleep(random.randint(2, 3))
                tid = adInfo['tid']
                showedAd(authorization, deviceId, 'rain', tid)
                time.sleep(random.randint(2, 3))
                initAd(authorization, deviceId)
                print('随机等待15-20秒')
                time.sleep(random.randint(2, 5))
                clickedAd(authorization, deviceId, 'rain', tid)
                time.sleep(random.randint(15, 20))
                compeletedAd(authorization, deviceId, 'rain', tid)
                time.sleep(random.randint(2, 3))
                postRedRain(authorization, deviceId)
            time.sleep(random.randint(2, 3))
            taskList = getZuanIndex(authorization, deviceId)
            for taskInfo in taskList:
                taskId = int(taskInfo['id'])
                title = taskInfo['title']
                taskTime = int(taskInfo['time'])
                if '$' in taskInfo['rate']:
                    todayTimes = int(taskInfo['rate'].split('$')[0])
                    targetTimes = int(taskInfo['rate'].split('$')[1])
                    print(f'任务{title}本日已完成{todayTimes}/{targetTimes}')
                    if taskId == 8 and todayTimes <= targetTimes:
                        if targetTimes == todayTimes:
                            print(f'去领取任务{title}奖励')
                            done(authorization, deviceId, taskId)
                        else:
                            print('查询任务广告成功，可以观看广告')
                            newsCost(authorization, deviceId)
                            time.sleep(1)
                            coinResult = newsCoin(authorization, deviceId)
                            coinTicket = coinResult['ticket']
                            coinTime = int(coinResult['time'])
                            time.sleep(coinTime)
                            newsCoinResult2 = newsCoin(authorization, deviceId, coinTicket)
                            count = int(newsCoinResult2['count'])
                            target = int(newsCoinResult2['target'])
                            print(f'再看{target - count}次可获得红包奖励')
                            if count == target:
                                adInfo = loadAd(authorization, deviceId, 'news')
                                time.sleep(random.randint(2, 3))
                                tid = adInfo['tid']
                                showedAd(authorization, deviceId, 'news', tid)
                                time.sleep(random.randint(2, 3))
                                initAd(authorization, deviceId)
                                print('随机等待15-20秒')
                                time.sleep(random.randint(2, 5))
                                clickedAd(authorization, deviceId, 'news', tid)
                                time.sleep(random.randint(15, 20))
                                compeletedAd(authorization, deviceId, 'news', tid)
                                time.sleep(random.randint(2, 3))
                                redEnv(authorization, deviceId)
                        time.sleep(random.randint(2, 3))
                    if taskId == 7 and todayTimes <= targetTimes:
                        if targetTimes == todayTimes:
                            print(f'去领取任务{title}奖励')
                            done(authorization, deviceId, taskId)
                        else:
                            print('查询任务广告成功，可以观看广告')
                            videoCost(authorization, deviceId)
                            time.sleep(1)
                            coinResult = videoCoin(authorization, deviceId)
                            coinTicket = coinResult['ticket']
                            coinTime = int(coinResult['time'])
                            time.sleep(coinTime)
                            newsCoinResult2 = videoCoin(authorization, deviceId, coinTicket)
                            count = int(newsCoinResult2['count'])
                            target = int(newsCoinResult2['target'])
                            print(f'再看{target - count}次可获得红包奖励')
                            if count == target:
                                adInfo = loadAd(authorization, deviceId, 'video')
                                time.sleep(random.randint(2, 3))
                                tid = adInfo['tid']
                                showedAd(authorization, deviceId, 'video', tid)
                                time.sleep(random.randint(2, 3))
                                initAd(authorization, deviceId)
                                print('随机等待15-20秒')
                                time.sleep(random.randint(2, 5))
                                clickedAd(authorization, deviceId, 'video', tid)
                                time.sleep(random.randint(15, 20))
                                compeletedAd(authorization, deviceId, 'video', tid)
                                time.sleep(random.randint(2, 3))
                                redVideoEnv(authorization, deviceId)
                        time.sleep(random.randint(2, 3))
                    if taskId == 24 and todayTimes <= targetTimes:
                        if targetTimes == todayTimes:
                            print(f'去领取任务{title}奖励')
                            done(authorization, deviceId, taskId)
                        else:
                            newsCount(authorization, deviceId, 1)
                            time.sleep(30)
                            newsCount(authorization, deviceId, 0)
                    if taskId == 21 and todayTimes <= targetTimes:
                        if targetTimes == todayTimes:
                            print(f'去领取任务{title}奖励')
                            done(authorization, deviceId, taskId)
                        else:
                            kanList = getKanList(authorization, deviceId)
                            for kanInfo in kanList:
                                taskId = kanInfo['id']
                                taskName = kanInfo['name']
                                isOk = int(kanInfo['is_ok'])
                                if isOk == 0:
                                    print(f'去完成{taskName}')
                                    kanTicket = clickKan(authorization, deviceId, taskId)
                                    print('随机等待60秒')
                                    time.sleep(60)
                                    getKanPrize(authorization, deviceId, taskId, kanTicket)
                        time.sleep(5)
                if taskId == 9:
                    todayTimes = title.split('>')[1].split('<')[0]
                    targetTimes = title.split('/')[2].split('）')[0]
                    text = taskInfo['text']
                    if targetTimes == todayTimes:
                        print(f'去领取任务{title}奖励')
                        done(authorization, deviceId, taskId)
                    else:
                        print(f'任务{text}本日已完成{todayTimes}/{targetTimes}')
                        print('查询任务广告成功，可以观看广告')
                        ticket = getZuanTicket(authorization, deviceId)
                        adInfo = loadAd(authorization, deviceId, 'zuan')
                        time.sleep(random.randint(2, 3))
                        tid = adInfo['tid']
                        showedAd(authorization, deviceId, 'zuan', tid)
                        time.sleep(random.randint(2, 3))
                        initAd(authorization, deviceId)
                        print('随机等待15-20秒')
                        time.sleep(random.randint(2, 5))
                        clickedAd(authorization, deviceId, 'zuan', tid)
                        time.sleep(random.randint(15, 20))
                        compeletedAd(authorization, deviceId, 'zuan', tid, ticket)
                        time.sleep(random.randint(2, 3))
            nickname, coin, ticket = getMyInfo(authorization, deviceId)
            exchangeInfo = exchange(authorization, deviceId)
            time.sleep(random.randint(2, 3))
            exchangeList = exchangeInfo['items']
            hasWechat = int(exchangeInfo['has_wechat'])
            if hasWechat != 1:
                msg += f'[{nickname}] {coin}金币，{ticket}提现券，未绑定微信无法提现\n'
            else:
                if '每天只能提一次' in str(exchangeInfo):
                    print('今日已经提现过')
                    msg += f'[{nickname}] {coin}金币，{ticket}提现券\n'
                else:
                    if ticket >= 1000:
                        print('开始提现1元，随机等待10-60秒')
                        time.sleep(random.randint(10, 60))
                        isSuccess = postExchange(authorization, deviceId, 1)
                        nickname, coin, ticket = getMyInfo(authorization, deviceId)
                        if isSuccess:
                            msg += f'[{nickname}] {coin}金币，{ticket}提现券，提现1元成功\n'
                        else:
                            msg += f'[{nickname}] {coin}金币，{ticket}提现券，提现1元失败\n'
                    else:
                        msg += f'[{nickname}] {coin}金币，{ticket}提现券\n'
        send("\n天天走路PRO", msg)
    except Exception as e:
        print("\n天天走路PRO脚本异常,失败原因 ", str(e))
        if str(e) == "list index out of range":
            send("\n天天走路PRO脚本异常,失败原因 ", f"{str(e)}")
