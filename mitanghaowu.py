# -*- coding:utf-8 -*-
"""
const $ = new Env("蜜糖好物签到");
cron: 0 12 7,12,16 * * *
desc: 蜜糖好物小程序，购买商品后直接返利，里面有100-20的话费充值商品，签满7天后，选择去发货，话费立刻到账
      小程序（复制到微信打开）：#小程序://蜜堂好物/YhMVF8IKGGc94jD
      抓包 api.mitangwl.cn 域名下，请求头里的 authorization，填到系统变量 MTHW_USER
"""
import json
import os
import sys
import time

import requests

from notify import send

mitangCks = os.environ.get("MTHW_USER") if os.environ.get(
    "MTHW_USER") else ""
mitangList = mitangCks.split("\n")
if len(mitangList) == 0 or mitangList == '':
    print('未填写蜜糖好物签到环境变量：MTHW_USER')
    sys.exit()


def sign(authorization, appointmentId):
    url = "https://api.mitangwl.cn/app/my/appointmentSign"
    payload = json.dumps({
        "appointmentId": appointmentId,
        "loc": 0
    })
    headers = {
        'authorization': authorization,
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252f) NetType/WIFI Language/zh_CN',
        'Host': 'api.mitangwl.cn',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


def queryMyApprointmentList(authorization):
    url = "https://api.mitangwl.cn/app/my/queryMyApprointmentList"
    payload = json.dumps({
        "pageNum": 1,
        "pageSize": 10
    })
    headers = {
        'authorization': authorization,
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x1800252f) NetType/WIFI Language/zh_CN',
        'Host': 'api.mitangwl.cn',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res


if __name__ == '__main__':
    global msg
    msg = ''
    num = 0
    for authorization in mitangList:
        num += 1
        print(f"\n====开始账号{num}运行任务======\n")
        queryMyApprointmentList_ = queryMyApprointmentList(authorization)
        if queryMyApprointmentList_['code'] == 200:
            myApprointmentList = queryMyApprointmentList_['data']['list']
            for myApprointment in myApprointmentList:
                productName = myApprointment['productName']
                signState = int(myApprointment['signState'])
                signDays = int(myApprointment['signDays'])
                totalDays = int(myApprointment['totalDays'])
                for userList_ in myApprointment['userList']:
                    appointmentOrderId = userList_['appointmentOrderId']
                    if signState != 4:
                        print(f"账号{num} 去签到商品-{productName}")
                        sign_ = sign(authorization, appointmentOrderId)
                        if sign_['code'] == 200:
                            print(f"账号{num} 签到成功，商品名称-{productName}，签到状态{signDays + 1}/{totalDays}天\n")
                            msg += f"账号{num} 签到成功，商品名称-{productName}，签到状态{signDays + 1}/{totalDays}天\n"
                            break
                        else:
                            print(f"账号{num} {sign_['msg']}")
                            if '异常' in sign_['msg']:
                                time.sleep(3)
                                continue
                            msg += f"账号{num} {sign_['msg']}\n"
                            break
                    else:
                        print(f"账号{num} 本日已签到，商品名称-{productName}，签到状态{signDays}/{totalDays}天\n")
                        msg += f"账号{num} 本日已签到，商品名称-{productName}，签到状态{signDays}/{totalDays}天\n"
                        break
                time.sleep(2)
        else:
            msg += f"账号{num} token已过期！\n"
        time.sleep(2)

    send('蜜糖好物签到', msg)
