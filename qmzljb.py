# -*- coding:utf-8 -*-
"""
const $ = new Env("全民走路计步");
cron: 36 6-22/2 * * *
"""
# 任意 http://qwjbq.lctdq.com 请求体的uid
# 变量 qmzljbck, 多变量换行分割
import random
import sys

from notify import *

qmzljbCks = os.environ.get("qmzljbck") if os.environ.get(
    "qmzljbck") else "534901\n534899"
qmzljbCkList = qmzljbCks.split("\n")
if len(qmzljbCkList) == 0 or qmzljbCks == '':
    print('未填写全民走路计步环境变量：qmzljbck')
    sys.exit()

token = '2f9eb0fc08fc31afd784590d020c34a3'


def getHeader(proxyAuthorization=None, proxy_type='xk'):
    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "qwjbq.lctdq.com",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.8.0",
    }
    if proxy_type == 'jl':
        headers['Proxy-Authorization'] = f'Basic {proxyAuthorization}'
    return headers


def init(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV11/init'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&device=Redmi Note 7 Pro&timestamp={now}&uid={uid}&ver=2.9.6'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&ver=2.9.6&sign={sign}&device=Redmi%20Note%207%20Pro&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        return res['data']
    else:
        return None


def sign(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV10/signfn'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f'签到成功，获得{res["data"]["coin"]}金币，已连续签到{res["data"]["sign_num"]}天')
        return res['data']
    else:
        print(f"签到失败：{res['msg']}")
        return None


def getTaskList(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV12/get_tasklist'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        return res['data']
    else:
        print(f"获取任务列表失败：{res['msg']}")
        return None


def sportsdays(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV5/sportsdays'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        return res['data']
    else:
        print(f"获取任务列表失败：{res['msg']}")
        return None


def do_sportsdays(uid, id, status, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/api/IndexV10/do_sportsdays'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&id={id}&status={status}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&id={id}&status={status}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f"任务状态：{res['msg']}")
        return True
    else:
        print(f"任务异常：{res['msg']}")
        return False


def getWaterList(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV6/water'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        return res['data']
    else:
        print(f"获取喝水情况失败：{res['msg']}")
        return None


def do_water(uid, waterid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV10/do_water'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}&waterid={waterid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&waterid={waterid}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f"喝水成功：获得{res['data']['coin']}金币")
    else:
        print(f"喝水失败：{res['msg']}")


def do_task(uid, taskId, title, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV10/do_task'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&id={taskId}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&id={taskId}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f"{title}-任务成功：获得{res['data']['coin']}金币")
    else:
        print(f"{title}-任务失败：{res['msg']}")


def init_draw(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV1/init_draw'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        return res['data']['total']
    else:
        print(f"获取喝水情况失败：{res['msg']}")
        return None


def do_draw(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV10/do_draw'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f"抽奖成功：获得{res['data']['coin']}金币")
    else:
        print(f"抽奖失败：{res['msg']}")
        return None


def do_draw2(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/index/Draw/do_draw'
    now = int(round(time.time() * 1000))
    headers = getHeader(proxyAuthorization, proxy_type)
    headers['Refer'] = f'http://qwjbq.lctdq.com/Index/draw/index?uid={uid}'
    payload = f'uid={uid}&type=1&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        if 'data' in str(res):
            print(f"抽奖成功：获得{res['data']['coin']}金币")
        else:
            print(f"抽奖成功：{res['msg']}")
    else:
        print(f"抽奖失败：{res['msg']}")
        return None


def getMining(uid):
    url = f'http://qwjbq.lctdq.com/Index/Room/mining?uid={uid}'
    headers = {
        "Host": "qwjbq.lctdq.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,image/tpg,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "com.cxkj_soft.jwjbq",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.get(url=url, headers=headers, timeout=20)
    text = resp.text
    matchList = re.findall(r"doLucky\('\d+'", text)
    tlz = text.split('>体力值：')[1].split('%')[0]
    miningid = text.split('miningid = parseInt("')[1].split('"')[0]
    if '<div>开始挖矿</div>' in text:
        isMining = False
    else:
        isMining = True
    goldIds = []
    if len(matchList) > 0:
        for matchInfo in matchList:
            goldIds.append(matchInfo.split("doLucky('")[1].split("'")[0])
    return goldIds, isMining, tlz, miningid


def do_mining(uid, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/index/Room/do_mining'
    headers = getHeader(proxyAuthorization, proxy_type)
    headers['Refer'] = f'http://qwjbq.lctdq.com/Index/Room/index?uid={uid}'
    payload = f'uid={uid}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f"挖宝成功")
    else:
        print(f"挖宝失败：{res['msg']}")


def getQuestion(uid):
    url = f'http://qwjbq.lctdq.com/Index/Room/index?uid={uid}'
    headers = {
        "Host": "qwjbq.lctdq.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,image/tpg,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "com.cxkj_soft.jwjbq",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    resp = requests.get(url=url, headers=headers, timeout=20)
    text = resp.text
    qid = text.split('qid = parseInt("')[1].split('"')[0]
    ans = text.split('answer = parseInt("')[1].split('"')[0]
    qno = text.split('qno = parseInt("')[1].split('"')[0]
    return qid, ans, qno


def do_question(uid, qid, ans, qno):
    url = f'http://qwjbq.lctdq.com/index/Room/do_question'
    headers = {
        "Host": "qwjbq.lctdq.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://qwjbq.lctdq.com",
        "Referer": f"http://qwjbq.lctdq.com/Index/Room/index?uid={uid}",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    payload = f'uid={uid}&answer={ans}&qid={qid}&qno={qno}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"答题正确，获得{res['data']['coin']}金币")
    else:
        print(f"答题失败：{res['msg']}")


def do_lucky(uid, goldId):
    url = f'http://qwjbq.lctdq.com/index/Room/do_lucky'
    headers = {
        "Host": "qwjbq.lctdq.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://qwjbq.lctdq.com",
        "Referer": f"http://qwjbq.lctdq.com/Index/Room/mining?uid={uid}",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    payload = f'uid={uid}&id={goldId}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"收矿成功，获得{res['data']['num']}金矿，当前{res['data']['total']}金矿")
    else:
        print(f"收矿失败：{res['msg']}")


def do_shopping(uid, goodId, consumeGold):
    url = f'http://qwjbq.lctdq.com/index/Room/do_shopping'
    headers = {
        "Host": "qwjbq.lctdq.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://qwjbq.lctdq.com",
        "Referer": f"http://qwjbq.lctdq.com/Index/Room/mining?uid={uid}",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    payload = f'uid={uid}&id={goodId}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"兑换成功，获得{res['data']['coin']}金币，消耗{consumeGold}金矿")
    else:
        print(f"兑换失败：{res['msg']}")


def do_prop(uid, propId, miningid):
    url = f'http://qwjbq.lctdq.com/index/Room/do_prop'
    headers = {
        "Host": "qwjbq.lctdq.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Pro Build/QKQ1.190915.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://qwjbq.lctdq.com",
        "Referer": f"http://qwjbq.lctdq.com/Index/Room/mining?uid={uid}",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    payload = f'uid={uid}&miningid={miningid}&type={propId}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"使用成功：{res['msg']}")
    else:
        print(f"使用失败：{res['msg']}")


def receive_task(uid, taskId, proxy=None, proxyAuthorization=None, proxy_type='xk'):
    url = f'http://qwjbq.lctdq.com/Api/IndexV9/receive_task'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&id={taskId}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader(proxyAuthorization, proxy_type)
    payload = f'uid={uid}&sign={sign}&id={taskId}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20, proxies=proxy)
    res = resp.json()
    if res['code'] == 200:
        print(f"分享成功")
    else:
        print(f"分享失败：{res['msg']}")


def get_idiom(uid):
    url = f'http://qwjbq.lctdq.com/Api/IndexV1/get_idiom'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader()
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        return res['data']
    else:
        print(f"成语接口异常：res['msg']")


def do_idiom(uid):
    url = f'http://qwjbq.lctdq.com/Api/IndexV10/do_idiom'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader()
    payload = f'uid={uid}&sign={sign}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"成语挑战成功，获得{res['data']['coin']}金币")
    else:
        print(f"成语挑战异常：{res['msg']}")


def do_step(uid, step):
    url = f'http://qwjbq.lctdq.com/Api/IndexV7/do_step'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&step={step}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader()
    payload = f'uid={uid}&sign={sign}&step={step}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"更新步数成功")
    else:
        print(f"更新步数失败：{res['msg']}")


def do_standard(uid, step):
    url = f'http://qwjbq.lctdq.com/Api/IndexV10/do_standard_step'
    now = int(round(time.time() * 1000))
    raw = f'token={token}&step={step}&timestamp={now}&uid={uid}'
    sign = hashlib.md5(raw.encode("utf-8")).hexdigest().upper()
    headers = getHeader()
    payload = f'uid={uid}&sign={sign}&step={step}&timestamp={now}'
    resp = requests.post(url=url, headers=headers, data=payload, timeout=20)
    res = resp.json()
    if res['code'] == 200:
        print(f"收取步数成功，获得{res['data']['coin']}金币")
    else:
        print(f"收取步数失败：{res['msg']}")


if __name__ == '__main__':
    global msg, model
    msg = ''
    for uid in qmzljbCkList:
        print('随机等待30-60s')
        time.sleep(random.randint(30, 60))
        initData = init(uid)
        userInfo = initData['user']
        use_coin = userInfo['use_coin']
        issign = initData['issign']
        time.sleep(0.5)
        if issign == 0:
            sign(uid)
            time.sleep(0.5)
            # step = random.randint(6000, 8000)
            # do_step(uid, step)
            # time.sleep(1)
            # do_standard(uid, step)
        taskList = getTaskList(uid)
        for taskInfo in taskList:
            title = taskInfo['title']
            type = taskInfo['type']
            status = taskInfo['status']
            taskId = taskInfo['id']
            video_num = taskInfo['video_num']
            if status == 1:
                do_task(uid, taskId, title)
            if title == '每日运动':
                sportsList = sportsdays(uid)
                for sportInfo in sportsList:
                    status2 = int(sportInfo['status'])
                    title2 = sportInfo['title']
                    id = sportInfo['id']
                    if status2 == 1:
                        print(f'去完成每日运动{title2}')
                        isFinished = do_sportsdays(uid, id, status2)
                    time.sleep(0.5)
                for sportInfo in sportsList:
                    status2 = sportInfo['status']
                    title2 = sportInfo['title']
                    id = sportInfo['id']
                    if status2 == -1:
                        print(f'去开始每日运动{title2}')
                        isStart = do_sportsdays(uid, id, status2)
                        break
            if title == '喝水打卡':
                waterList = getWaterList(uid)
                for waterInfo in waterList:
                    isNow = waterInfo['isnow']
                    iswater = waterInfo['iswater']
                    waterid = waterInfo['index']
                    if isNow == 1 and iswater == 0:
                        do_water(uid, waterid)

            if title == '幸运大转盘':
                total = init_draw(uid)
                for i in range(0, 20 - int(total)):
                    do_draw(uid)
                    time.sleep(0.5)

            if title == '金币抽大奖':
                if int(taskInfo['num']) == 0:
                    do_draw2(uid)

            if title == '挖矿赚金币':
                goldIds, isMining, tlz, miningid = getMining(uid)
                time.sleep(0.5)
                if not isMining:
                    do_mining(uid)
                    time.sleep(0.5)
                    goldIds, isMining, tlz, miningid = getMining(uid)
                    time.sleep(2)
                if len(goldIds) > 0:
                    for goldId in goldIds:
                        do_lucky(uid, goldId)
                        time.sleep(0.5)
                if 0 == int(tlz):
                    do_prop(uid, 1, miningid)
                    time.sleep(0.5)
                do_prop(uid, 2, miningid)
                time.sleep(0.5)
                do_prop(uid, 3, miningid)
                time.sleep(0.5)
                do_shopping(uid, 4, 900)
                time.sleep(0.5)
            if title == '知识小课堂':
                questionInfo = getQuestion(uid)
                qid = questionInfo[0]
                ans = questionInfo[1]
                qno = questionInfo[2]
                do_question(uid, qid, ans, qno)

            if title == '每日分享':
                if status == 0:
                    for i in range(0, 2):
                        receive_task(uid, taskId)
                        time.sleep(0.5)

            if title == '成语挑战赛':
                do_idiom(uid)

        initData = init(uid)
        userInfo = initData['user']
        use_coin = userInfo['use_coin']
        nickname = userInfo['nickname']
        print(f'账号{nickname} 当前共有{use_coin}金币')
        msg += f'账号{nickname} 当前共有{use_coin}金币\n'

    send("全民走路记步", msg)
