# -*- coding:utf-8 -*-
"""
const $ = new Env("太平通");
cron: 0 12 0,8,13,20 * * *
"""
import json
import os
import random
import sys
import time

import requests

from notify import send

tptCks = os.environ.get("tptck") if os.environ.get("tptck") else ""

lotterySwitch = os.environ.get("tptLotterySwitch") if os.environ.get("tptLotterySwitch") else "false"
lotteryTimes = os.environ.get("tptLotteryTimes") if os.environ.get("tptLotteryTimes") else "1"
tptCkList = tptCks.split("\n")
if len(tptCkList) == 0 or tptCks == '':
    print('未填写太平通环境变量：tptck')
    sys.exit()


def queryUserPoints(token, tokenKey):
    url = "https://ecustomer.cntaiping.com/campaignsms/integral/queryUserPoints"
    payload = json.dumps({
        "sourceOrganId": 932
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = requests.request("POST", url, headers=headers, data=payload, timeout=5)
    res = response.json()
    return res


def taskList(token, tokenKey):
    url = "https://ecustomer.cntaiping.com/campaignsms/goldParty/task/list"

    payload = json.dumps({
        "activityNumber": "goldCoinParty",
        "rewardFlag": 1,
        "openMsgRemind": 1
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.post(url=url, headers=headers, data=payload, timeout=5)
    res = response.json()
    return res


def finish(token, tokenKey, taskId):
    url = "https://ecustomer.cntaiping.com/campaignsms/goldParty/task/finish"
    payload = json.dumps({
        "taskIds": [
            taskId
        ]
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload, timeout=5)
    res = response.json()
    return res


def add(token, tokenKey):
    url = "https://ecustomer.cntaiping.com/campaignsms/goldParty/goldCoin/add"
    payload = json.dumps({
        "taskIds": [
            taskId
        ]
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.request("POST", url, headers=headers, data=payload, timeout=5)
    res = response.json()
    return res


def signInfo(token, tokenKey):
    url = "https://ecustomer.cntaiping.com/campaignsms/couponAndsign"

    payload = json.dumps({})
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


def getArticle(token, tokenKey, page):
    url = f"https://ecustomer.cntaiping.com/informationms/app/config/get/{page}"
    payload = json.dumps({
        "city": 1,
        "pageSize": 10,
        "type": "GENERAL_PLUGIN",
        "trackDesc": "赚金币任务",
        "plugInId": "701b3099297148a8ba979ad9c982b561"
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


def getDetail(token, tokenKey, contentId):
    url = "https://ecustomer.cntaiping.com/informationms/app/v2/article/web/detail"

    payload = json.dumps({
        "articleId": contentId,
        "source": "TPT",
        "detailUrl": f"https://ecustomercdn.itaiping.com/static/newscontent/#/info?articleId={contentId}&source=TPT&x_utmId=10013&x_businesskey=articleId",
        "deviceId": "",
        "version": "V2"
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


def genCoin(token, tokenKey, contentId):
    url = "https://ecustomer.cntaiping.com/informationms/app/v2/read/gold"
    payload = json.dumps({
        "articleId": contentId,
        "source": "TPT"
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def getAllCoin(token, tokenKey):
    url = "https://ecustomer.cntaiping.com/campaignsms/coinBubble/getAllCoins"
    payload = json.dumps({})
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-mc-type': 'gateway.user',
        'x-ac-black-box': token,
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    print(res)
    return res['data']['coinNum']


def registerAndLogin(tokenKey, activityCode):
    url = "https://ecustomer.cntaiping.com/tptplaybox/api/account/registerAndLogin"
    payload = json.dumps({
        "activityCode": activityCode,
        "phone": "",
        "smsCode": "",
        "ticket": "",
        "thirdAccount": tokenKey,
        "registerData": {}
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'activityCode': activityCode,
        'platform': '',
        'tokenkey': tokenKey,
        'channel': '0',
        'User-Agent': ua,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['value']['accessKey']


def getPublicInfo(tokenKey, accessKey, activityCode):
    url = f"https://ecustomer.cntaiping.com/tptplaybox/api/activity/getPublicInfo?activityCode={activityCode}"
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'activityCode': 'subj1602',
        'accessKey': accessKey,
        'platform': '',
        'tokenkey': tokenKey,
        'channel': '0',
        'User-Agent': ua,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("GET", url, headers=headers)


def getBaseInfo(tokenKey, accessKey, activityCode):
    url = f"https://ecustomer.cntaiping.com/tptplaybox/api/activity/getBaseInfo?activityCode={activityCode}"
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'activityCode': 'subj1602',
        'accessKey': accessKey,
        'platform': '',
        'tokenkey': tokenKey,
        'channel': '0',
        'User-Agent': ua,
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()


def doEvaluation1(token, tokenKey, accessKey, activityCode):
    url = "https://ecustomer.cntaiping.com/tptplaybox/api/evaluation/doEvaluation"
    payload = json.dumps({
        "activityCode": activityCode
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'activityCode': activityCode,
        'channel': '0',
        'User-Agent': ua,
        'Content-Type': 'application/json',
        'x-ac-black-box': token,
        'accessKey': accessKey,
        'platform': '',
        'tokenkey': tokenKey,
        'Accept': '*/*',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def doEvaluation2(token, tokenKey, accessKey, activityCode, questionCode, optionCode, evaluationId):
    url = "https://ecustomer.cntaiping.com/tptplaybox/api/evaluation/doEvaluation"
    payload = json.dumps({
        "activityCode": activityCode,
        "questionCode": questionCode,
        "optionCode": optionCode,
        "evaluationId": evaluationId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'activityCode': activityCode,
        'channel': '0',
        'User-Agent': ua,
        'Content-Type': 'application/json',
        'x-ac-black-box': token,
        'accessKey': accessKey,
        'platform': '',
        'tokenkey': tokenKey,
        'Accept': '*/*',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def lottery(token, tokenKey, accessKey, activityCode, x_utmId='', p_xCubeActivityCode=''):
    url = "https://ecustomer.cntaiping.com/tptplaybox/api/activity/lottery"
    if 'love' in activityCode:
        payload = json.dumps({
            "activityCode": activityCode,
            "lotteryMap": {
                "businessInfo": f"{{\"xCubeActivityCode\": \"{activityCode}\",\"shareCode\": \"\"}}"
            }
        })
    else:
        payload = json.dumps({
            "activityCode": activityCode,
            "lotteryMap": {
                "businessInfo": f"{{\"xCubeActivityCode\": \"{activityCode}\",\"x_businesskey\":\"xCubeActivityCode\",\"x_utmId\": \"{x_utmId}\",\"p_xCubeActivityCode\": \"{p_xCubeActivityCode}\",\"shareCode\": \"\"}}"
            }
        })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'activityCode': activityCode,
        'channel': '0',
        'User-Agent': ua,
        'Content-Type': 'application/json',
        'x-ac-black-box': token,
        'accessKey': accessKey,
        'platform': '',
        'tokenkey': tokenKey,
        'Accept': '*/*',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['success']:
        print(f'抽奖成功，获得{res["value"][0]["showName"]}')
    else:
        print(f'抽奖异常：{activityCode}-{res["errorMsg"]}')


def farmUserInfo(tokenKey):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/user/home"

    payload = {}
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    if int(res['code']) == 200:
        return res['data']
    else:
        print(f"获取农场信息失败：{res['msg']}")
        return None


def farmTaskList(tokenKey):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/task/list"
    payload = {}
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    if int(res['code']) == 200:
        return res['data']
    else:
        print((res['msg']))
        return None


def queryAllServiceAccount(tokenKey, page):
    url = "https://ecustomer.cntaiping.com/userms/serviceAccount/queryAllServiceAccount/v1"
    payload = json.dumps({
        "page": page,
        "pageSize": 15
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'accept': 'application/json',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': '',
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'content-type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == '0000':
        return res['data']['contents']
    else:
        return None


def getTaskData(tokenKey, taskId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/task/get-task-data"
    payload = json.dumps({
        "tid": taskId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Content-Length': '10',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    print(res['msg'])


def getTaskResult(tokenKey):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/task/get-task-result"
    payload = "{}"
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == 200:
        if len(res['data']) > 0:
            print(f'任务完成，领取{res["data"][0]["water"]}颗水滴')
        else:
            print(f'没有可领取的水滴！')
    else:
        print(res['msg'])


def subscribed(token, tokenKey, serviceId):
    url = "https://ecustomer.cntaiping.com/userms/serviceAccount/subscribe"
    payload = json.dumps({
        "serviceAccountId": serviceId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'accept': 'application/json',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'content-type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['success']:
        print("关注成功")
        return True
    else:
        print(res['msg'])
        return False


def completeTask(token, tokenKey, taskId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/task/complete-red-envelope"
    payload = json.dumps({
        "tid": taskId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == 200:
        print(f'任务完成，领取{res["data"]["water"]}颗水滴')
    else:
        print(f'领取水滴失败：{res["msg"]}')


def completeTask2(token, tokenKey, taskId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/task/complete-task"
    payload = json.dumps({
        "type": taskId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == 200:
        print(f'任务完成，领取{res["data"]["water"]}颗水滴')
    else:
        print(f'领取水滴失败：{res["msg"]}')


def toWater(tokenKey, userId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/tree/watering"
    payload = json.dumps({
        "tree_user_id": userId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == 200:
        print(f"浇水成功，剩余{res['data']['sy_water']}水滴")
        upgrade_reward_id = None
        if res['data']['is_upgrade_reward']:
            upgrade_reward_id = res['data']['upgrade_reward_id']
        return res['data']['sy_water'], res['data']['is_upgrade_reward'], upgrade_reward_id


def toFertilizer(tokenKey, userId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/tree/fertilizer"
    payload = json.dumps({
        "tree_user_id": userId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == 200:
        print(f"施肥成功，剩余{res['data']['sy_fertilizer']}肥料")
        upgrade_reward_id = None
        if res['data']['is_upgrade_reward']:
            upgrade_reward_id = res['data']['upgrade_reward_id']
        return res['data']['sy_fertilizer'], res['data']['is_upgrade_reward'], upgrade_reward_id


def receiveReward(tokenKey, rewardId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/tree/receive-upgrade-reward"
    payload = json.dumps({
        "reward_id": rewardId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['code'] == 200:
        print(f'领取果树升级奖励成功：获得{res["data"]["water"]}水滴，{res["data"]["balance"]}爱心')
        return res["data"]["sy_water"], res["data"]["w_id"]


def openBox(tokenKey, wId):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/user/open-welfare_box"
    payload = json.dumps({
        'w_id': wId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    print(f'领取宝箱成功：{res}')


def getTodayWater(tokenKey):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/user/get-today-water"
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("GET", url, headers=headers)
    res = response.json()
    if int(res['code']) == 200:
        print(f'领取每日水滴成功：获得{res["data"]["water"]}水滴')
    else:
        print('领取每日水滴失败：' + res['msg'])


def farmLogin(tokenKey):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/login"
    payload = "{\"type\":\"\",\"share_user_id\":\"\"}"
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;yuangongejia#ios#kehutong#CZBIOS',
        'Connection': 'keep-alive',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'ENV': 'app'
    }
    response = requests.request("POST", url, headers=headers, data=payload)


def giftBag(token, tokenKey):
    url = "https://ecustomer.cntaiping.com/campaignsms/dailySign/giftBag"

    payload = json.dumps({})
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Content-Length': '2',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-channel-id': 'KHT',
        'x-ac-black-box': token,
        'x-ac-mc-type': 'gateway.user',
        'User-Agent': ua,
        'x-ac-token-ticket': tokenKey,
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    if res['success']:
        return res['data']
    else:
        return None


def getWelfareBox(tokenKey):
    url = "https://ecustomer.cntaiping.com/love-tree/v2/api/user/get-welfare-box?type=1"
    payload = {}
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'API-TOKEN': tokenKey,
        'ENV': 'app',
        'User-Agent': ua,
        'Origin': 'https://ecustomercdn.itaiping.com',
        'X-Requested-With': 'com.cntaiping.tpapp',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    print(res)
    if res['code'] == 200:
        return res['data']['w_id']
    else:
        return None


def exchangeReceive(token, tokenKey, ua, ecardNo):
    url = "https://ecustomer.cntaiping.com/campaignsms/coin/exchange/receive"

    payload = json.dumps({
        "id": ecardNo
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-black-box': token,
        'x-ac-token-ticket': tokenKey,
        'x-ac-channel-id': 'KHT',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'User-Agent': ua,
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'x-ac-mc-type': 'gateway.user',
        'Connection': 'keep-alive'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


def queryCouponInfo(tokenKey, ua, couponId):
    url = "https://ecustomer.cntaiping.com/campaignsms/coupon/queryCouponInfo"
    payload = json.dumps({
        "couponId": couponId
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-os-info': 'IOS',
        'x-ac-token-ticket': tokenKey,
        'x-ac-channel-id': 'KHT',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'User-Agent': ua,
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'x-ac-mc-type': 'gateway.user',
        'Connection': 'keep-alive'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def getECard(tokenKey, ua, couponCode, couponId):
    url = "https://ecustomer.cntaiping.com/campaignsms/coupon/getActivationCode"
    payload = json.dumps({
        "couponCode": couponCode,
        "couponId": couponId,
        "isNewVersion": True
    })
    headers = {
        'Host': 'ecustomer.cntaiping.com',
        'Accept': 'application/json;charset=UTF-8',
        'x-ac-os-info': 'IOS',
        'x-ac-token-ticket': tokenKey,
        'x-ac-channel-id': 'KHT',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Origin': 'https://ecustomercdn.itaiping.com',
        'User-Agent': ua,
        'Referer': 'https://ecustomercdn.itaiping.com/',
        'x-ac-mc-type': 'gateway.user',
        'Connection': 'keep-alive'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


if __name__ == '__main__':
    msg = ''
    idx = 0
    for tptCk in tptCkList:
        token = tptCk.split('@')[0]
        tokenKey = tptCk.split('@')[1]
        ua = tptCk.split('@')[2]
        idx += 1
        try:
            availableScoreBefore = queryUserPoints(token, tokenKey)['data']['scoreAccountInfo']['availableScore']
        except:
            # msg += f'账号{idx} token已过期，请重新抓取ck\n'
            print(f'账号{idx} token已过期，请重新抓取ck')
            continue
        if availableScoreBefore >= 2000:
            exchangeReceive_ = exchangeReceive(token, tokenKey, ua, 70)
            if exchangeReceive_['success']:
                couponId = exchangeReceive_['data']['couponId']
                time.sleep(0.6)
                queryCouponInfo_ = queryCouponInfo(tokenKey, ua, couponId)
                if queryCouponInfo_['success']:
                    couponCode = queryCouponInfo_['data']['couponInfo']['couponCode']
                    getECard_ = getECard(tokenKey, ua, couponCode, couponId)
                    if getECard_['success']:
                        eCardPwd = getECard_["data"]["activationCodePw"]
                        print(f'获得E卡-卡密：{eCardPwd}')
                        msg += f"账号{idx}兑换20元E卡成功，消耗2000积分"
                        send('太平通E卡兑换-20元E卡', eCardPwd)
                else:
                    print(f'账号{idx} ' + queryCouponInfo_['msg'])
            else:
                print(f'账号{idx} ' + exchangeReceive_['msg'])

        if availableScoreBefore >= 1000:
            exchangeReceive_ = exchangeReceive(token, tokenKey, ua, 69)
            if exchangeReceive_['success']:
                couponId = exchangeReceive_['data']['couponId']
                time.sleep(0.6)
                queryCouponInfo_ = queryCouponInfo(tokenKey, ua, couponId)
                if queryCouponInfo_['success']:
                    couponCode = queryCouponInfo_['data']['couponInfo']['couponCode']
                    getECard_ = getECard(tokenKey, ua, couponCode, couponId)
                    if getECard_['success']:
                        eCardPwd = getECard_["data"]["activationCodePw"]
                        print(f'获得E卡-卡密：{eCardPwd}')
                        msg += f"账号{idx}兑换10元E卡成功，消耗1000积分"
                        send('太平通E卡兑换-10元E卡', eCardPwd)
                else:
                    print(f'账号{idx} ' + queryCouponInfo_['msg'])
            else:
                print(f'账号{idx} ' + exchangeReceive_['msg'])
        if availableScoreBefore >= 500:
            exchangeReceive_ = exchangeReceive(token, tokenKey, ua, 68)
            if exchangeReceive_['success']:
                couponId = exchangeReceive_['data']['couponId']
                time.sleep(0.6)
                queryCouponInfo_ = queryCouponInfo(tokenKey, ua, couponId)
                if queryCouponInfo_['success']:
                    couponCode = queryCouponInfo_['data']['couponInfo']['couponCode']
                    getECard_ = getECard(tokenKey, ua, couponCode, couponId)
                    if getECard_['success']:
                        eCardPwd = getECard_["data"]["activationCodePw"]
                        print(f'获得E卡-卡密：{eCardPwd}')
                        msg += f"账号{idx}兑换5元E卡成功，消耗500积分"
                        send('太平通E卡兑换-5元E卡', eCardPwd)
                else:
                    print(f'账号{idx} ' + queryCouponInfo_['msg'])
            else:
                print(f'账号{idx} ' + exchangeReceive_['msg'])

        # if availableScoreBefore >= 200:
        #     exchangeReceive_ = exchangeReceive(token, tokenKey, ua, 67)
        #     if exchangeReceive_['success']:
        #         couponId = exchangeReceive_['data']['couponId']
        #         time.sleep(0.6)
        #         queryCouponInfo_ = queryCouponInfo(tokenKey, ua, couponId)
        #         if queryCouponInfo_['success']:
        #             couponCode = queryCouponInfo_['data']['couponInfo']['couponCode']
        #             getECard_ = getECard(tokenKey, ua, couponCode, couponId)
        #             if getECard_['success']:
        #                 eCardPwd = getECard_["data"]["activationCodePw"]
        #                 print(f'获得E卡-卡密：{eCardPwd}')
        #                 msg += f"账号{idx}兑换2元E卡成功，消耗1000积分"
        #                 send('太平通E卡兑换-2元E卡', eCardPwd)
        #         else:
        #             print(queryCouponInfo_['msg'])
        #     else:
        #         print(exchangeReceive_['msg'])

    idx = 0
    for tptCk in tptCkList:
        token = tptCk.split('@')[0]
        tokenKey = tptCk.split('@')[1]
        ua = tptCk.split('@')[2]
        idx += 1
        try:
            availableScoreBefore = queryUserPoints(token, tokenKey)['data']['scoreAccountInfo']['availableScore']
        except:
            msg += f'账号{idx} token已过期，请重新抓取ck\n'
            print(f'账号{idx} token已过期，请重新抓取ck')
            continue
        print(f'账号{idx}登陆成功，当前积分：{availableScoreBefore}')
        dailySignRsp = signInfo(token, tokenKey)['data']['dailySignRsp']
        nearSignDetails = dailySignRsp['nearSignDetails']
        print(f'账号{idx} 已连续签到{dailySignRsp["continueSign"]}天')
        giftBagList = giftBag(token, tokenKey)
        if giftBagList is not None:
            for giftBag_ in giftBagList:
                giftBagStatus = int(giftBag_['status'])
                activityCode = giftBag_['activityCode']
                jumpUrl = giftBag_['jumpUrl']
                if giftBagStatus == 1:
                    accessKey = registerAndLogin(tokenKey, activityCode)
                    lottery(token, tokenKey, accessKey, activityCode)
        taskList_ = None
        for k1 in range(0, 5):
            try:
                taskList_ = taskList(token, tokenKey)['data']['taskList']
                break
            except:
                continue
        if taskList_ is None:
            continue
        else:
            for taskInfo in taskList_:
                taskName = taskInfo['name']
                isComplete = taskInfo['isComplete']
                taskId = taskInfo['taskId']
                taskStatus = taskInfo['taskStatus']
                isFinished = False
                isAdded = False
                if taskName == '邀请注册':
                    continue
                if not isComplete:
                    print(f'\n去完成任务：{taskName}')
                    articleList = []
                    if taskName == '浏览资讯':
                        page = 1
                        articleList = getArticle(token, tokenKey, page)['data']
                        if len(articleList) == 0:
                            continue
                        for articleInfo_ in articleList:
                            articleInfo = articleInfo_['cell']['0'][0]
                            title = articleInfo['title']
                            contentId = articleInfo['contentId']
                            print(f'\n获取文章信息成功，本次阅读[{title}]，随机等待10s')
                            try:
                                getDetail(token, tokenKey, contentId)
                                time.sleep(random.randint(15, 20))
                                genCoin(token, tokenKey, contentId)
                                print(f'文章阅读完成！')
                                time.sleep(3)
                            except:
                                continue
                        for k1 in range(0, 5):
                            try:
                                coinNum = getAllCoin(token, tokenKey)
                                print(f'\n本次阅读资讯获得{coinNum}个金币')
                                break
                            except:
                                continue
                    else:
                        for k1 in range(0, 5):
                            try:
                                isFinished = finish(token, tokenKey, taskId)['success']
                                break
                            except:
                                continue
                        if isFinished:
                            for k1 in range(0, 5):
                                try:
                                    isAdded = add(token, tokenKey)['success']
                                    break
                                except:
                                    continue
                            if isAdded:
                                print(f"任务{taskName}已完成，领取奖励成功")
                            else:
                                print(f"任务{taskName}已完成，领取奖励失败")
                else:
                    if int(taskStatus) == 1:
                        for k1 in range(0, 5):
                            try:
                                isAdded = add(token, tokenKey)['success']
                                break
                            except:
                                continue
                        if isAdded:
                            print(f"任务{taskName}已完成，领取奖励成功")
                        else:
                            print(f"任务{taskName}已完成，领取奖励失败")

        availableScoreAfter = queryUserPoints(token, tokenKey)['data']['scoreAccountInfo']['availableScore']
        if lotterySwitch == "true":
            activityCode = 'ngrid803'
            accessKey = registerAndLogin(tokenKey, activityCode)
            print(f"抽奖开关开启，开始进行抽奖，抽奖次数{lotteryTimes}次")
            for k2 in range(0, int(lotteryTimes)):
                lottery(token, tokenKey, accessKey, activityCode, '11371', 'andh1603')
                time.sleep(3)

        activityCode = 'subj1602'
        accessKey = registerAndLogin(tokenKey, activityCode)
        subj1602BaseInfo = getBaseInfo(tokenKey, accessKey, activityCode)
        jumpUrl = subj1602BaseInfo['value']['frontend']['page:/'][1]['data']['jumpData']['jumpUrl']
        activityCode = jumpUrl.split('xCubeActivityCode=')[1].split('&')[0]
        accessKey = registerAndLogin(tokenKey, activityCode)
        doEvaluation1_ = doEvaluation1(token, tokenKey, accessKey, activityCode)
        if doEvaluation1_["success"]:
            evaluationId = doEvaluation1_['value']['evaluationId']
            questionCode = doEvaluation1_['value']['questionCode']
            pageUrl = doEvaluation1_['value']['pageUrl']
            questionInfo_ = getBaseInfo(tokenKey, accessKey, activityCode)
            if questionInfo_['success']:
                frontend = questionInfo_['value']['frontend']
                evaluationResult = frontend['page:/evaluationResult']
                realAnsText = None
                for evaluationResult_ in evaluationResult:
                    if 'oldIndex' not in str(evaluationResult_):
                        continue
                    oldIndex = evaluationResult_['oldIndex']
                    if int(oldIndex) == 5:
                        realAnsText = evaluationResult_['data']['text']
                        break
                ansList = frontend[f'{pageUrl}']
                for info_ in ansList:
                    if 'renderTagName' not in str(info_):
                        continue
                    renderTagName = info_['renderTagName']
                    if renderTagName == 'Answer':
                        label = info_['data']['label']
                        if label in realAnsText:
                            optionCode = info_['data']['optionCode']
                            break
                        else:
                            optionCode = info_['data']['optionCode']
                time.sleep(3)
                doEvaluation2_ = doEvaluation2(token, tokenKey, accessKey, activityCode, questionCode, optionCode,
                                               evaluationId)
                time.sleep(3)
                if doEvaluation2_['success']:
                    activityCode = 'turn1802'
                    accessKey = registerAndLogin(tokenKey, activityCode)
                    lottery(token, tokenKey, accessKey, activityCode, '11366', 'subj1602')
        # 农场任务
        print("\n=====开始农场任务======\n")
        farmLogin(tokenKey)
        time.sleep(2)
        farmUserInfo_ = farmUserInfo(tokenKey)
        if farmUserInfo_ is None:
            continue
        try:
            userId = farmUserInfo_['id']
            water = farmUserInfo_['water']
            is_get_water = farmUserInfo_['is_get_water']
            tree_user = farmUserInfo_['tree_user']
            check_user_can_open_box = farmUserInfo_['check_user_can_open_box']
            can_lottery = farmUserInfo_['can_lottery']
            lottery_info = farmUserInfo_['lottery_info']
            show_today_welfare = farmUserInfo_['show_today_welfare']
            if not is_get_water:
                getTodayWater(tokenKey)
                time.sleep(0.5)
            if show_today_welfare:
                for k5 in range(0, 100):
                    wId = getWelfareBox(tokenKey)
                    time.sleep(0.5)
                    if wId is not None:
                        openBox(tokenKey, wId)
                        time.sleep(4)
                    else:
                        break
            farmTaskList_ = farmTaskList(tokenKey)
            if farmTaskList_ is None:
                continue
            for farmTaskInfo in farmTaskList_['taskList']:
                taskId = int(farmTaskInfo['id'])
                can_do = farmTaskInfo['can_do']
                # if can_do:
                taskName = farmTaskInfo['title']
                if taskId == 25 or taskId == 26:
                    try:
                        day_reward_num = int(farmTaskInfo['day_reward_num'])
                        complete_cnt = int(farmTaskInfo['complete_cnt'])
                        if day_reward_num - complete_cnt > 0:
                            getTaskData(tokenKey, taskId)
                            print(f"去完成农场任务：{taskName}")
                            hasSubscribed = 0
                            for k3 in range(0, 20):
                                serviceList = queryAllServiceAccount(tokenKey, k3 + 1)
                                if serviceList is None or len(serviceList) == 0:
                                    break
                                else:
                                    for serviceInfo in serviceList:
                                        serviceId = serviceInfo['id']
                                        isSubscribed = serviceInfo['subscribed']
                                        if not isSubscribed:
                                            isSuccess = subscribed(token, tokenKey, serviceId)
                                            time.sleep(5)
                                            hasSubscribed += 1
                                            getTaskResult(tokenKey)
                                            time.sleep(5)
                                        if hasSubscribed == (day_reward_num - complete_cnt):
                                            break
                                if hasSubscribed == (day_reward_num - complete_cnt):
                                    break
                            if hasSubscribed == (day_reward_num - complete_cnt):
                                completeTask(token, tokenKey, taskId)
                    except Exception as e:
                        print(e)
                else:
                    print(f"去完成农场任务：{taskName}")
                    getTaskData(tokenKey, taskId)
                    completeTask(token, tokenKey, taskId)
            farmUserInfo_ = farmUserInfo(tokenKey)
            if farmUserInfo_ is None:
                continue
            userId = farmUserInfo_['tree_user']['id']
            water = farmUserInfo_['water']
            fertilizer = farmUserInfo_['fertilizer']
            while True:
                if water < 50:
                    break
                try:
                    water, is_upgrade_reward, upgrade_reward_id = toWater(tokenKey, userId)
                    time.sleep(random.randint(6, 10))
                    if is_upgrade_reward:
                        water, w_id = receiveReward(tokenKey, upgrade_reward_id)
                        time.sleep(3)
                        openBox(tokenKey, w_id)
                        time.sleep(3)
                except Exception as e:
                    print("toWater->" + e)

            while True:
                if fertilizer < 10:
                    break
                try:
                    fertilizer, is_upgrade_reward, upgrade_reward_id = toFertilizer(tokenKey, userId)
                    time.sleep(random.randint(6, 10))
                    if is_upgrade_reward:
                        fertilizer, w_id = receiveReward(tokenKey, upgrade_reward_id)
                        time.sleep(3)
                        openBox(tokenKey, w_id)
                        time.sleep(3)
                except Exception as e:
                    pass
        except:
            pass
        print(
            f'\n账号{idx} 当前积分{availableScoreAfter}，本次获取{int(availableScoreAfter) - int(availableScoreBefore)}积分'
            f'\n===================================\n')
        msg += f"账号{idx} 当前积分{availableScoreAfter}，本次获取{int(availableScoreAfter) - int(availableScoreBefore)}积分\n"
        # if availableScoreAfter >= 500:
        #     exchangeReceive_ = exchangeReceive(token, tokenKey, ua)
        #     if exchangeReceive_['success']:
        #         couponId = exchangeReceive_['data']['couponId']
        #         time.sleep(0.6)
        #         queryCouponInfo_ = queryCouponInfo(tokenKey, ua, couponId)
        #         if queryCouponInfo_['success']:
        #             couponCode = queryCouponInfo_['data']['couponInfo']['couponCode']
        #             getECard_ = getECard(tokenKey, ua, couponCode, couponId)
        #             if getECard_['success']:
        #                 eCardPwd = getECard_["data"]["activationCodePw"]
        #                 print(f'获得E卡-卡密：{eCardPwd}')
        #                 msg += f"账号{idx}兑换E卡成功，消耗500积分"
        #                 send('太平通E卡兑换', eCardPwd)
        #         else:
        #             print(queryCouponInfo_['msg'])
        #     else:
        #         print(exchangeReceive_['msg'])

    send("太平通", msg)
