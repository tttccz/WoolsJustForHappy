/*
[task_local]
# 爱平阳-APP
cron:9 9,19 * * * 
ydwx.js, tag=爱平阳-APP, enabled=true
填写环境变量 XW_COMMON_USER 格式 用户名;密码;/api/zbtxz/login接口的X-SESSION-ID 多账号换行分割 
*/
const $ = new Env('爱平阳-APP');
const notify = $.isNode() ? require('./sendNotifySp') : '';
const moment = require('moment');
const commonUtil = require('./commonUtil')
const encryptUtil = require('./encryptUtil')
var publicKeyRSA = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD6XO7e9YeAOs+cFqwa7ETJ+WXizPqQeXv68i5v
qw9pFREsrqiBTRcg7wB0RIp3rJkDpaeVJLsZqYm5TW7FWx/iOiXFc+zCPvaKZric2dXCw27EvlH5
rq+zwIPDAJHGAfnn1nmQH7wR3PCatEIb8pz5GFlTHMlluw4ZYmnOwg+thwIDAQAB
-----END PUBLIC KEY-----`
let sid = 35
let clientId = 51
let channelId = '5dbbdb441b011b790a33c652'
if (process.env.XW_COMMON_USER) {
    if (process.env.XW_COMMON_USER.indexOf('\n') > -1) {
        cookieArr = process.env.XW_COMMON_USER.split('\n');
    } else {
        cookieArr = [process.env.XW_COMMON_USER];
    }
} else {
    console.log('未发现有效Cookie，请填写XW_COMMON_USER !')
    return
}
console.log(`\n==========共发现${cookieArr.length}个账号==========\n`)
$.message = ''
!(async () => {
    for (let i = 0; i < cookieArr.length; i++) {
        console.log(`\n🎯 开始运行第${i + 1}个账号\n`)
        let cookie = cookieArr[i]
        let phone = cookie.split(';')[0]
        let pwd = cookie.split(';')[1]
        let sessionId = cookie.split(';').length > 2 ? cookie.split(';')[2] : commonUtil.randomStr(false, 24)
        if (cookie.split(';').length == 2) {
            console.log(`⌚ 随机生成的sessionId为 ${sessionId}`)
        }
        let authResp = await credential_auth(phone, pwd)
        if (authResp.statusCode != 200) {
            console.log(`账号【${phone}】登陆失败！`)
            console.log(authResp)
            $.message += `账号【${phone}】登陆失败\n`
            continue
        }
        let authCode = ''
        if (JSON.parse(authResp.body).code == 0) {
            authCode = JSON.parse(authResp.body).data.authorization_code.code
        } else {
            console.log(`账号【${phone}】${JSON.parse(authResp.body).message}！`)
            $.message += `账号【${phone}】${JSON.parse(authResp.body).message}\n`
            continue
        }

        let loginResp = await login(authCode, sessionId)
        if (JSON.parse(loginResp.body).code != 0) {
            console.log(`账号【${phone}】登陆失败！`)
            console.log(authResp)
            $.message += `账号【${phone}】登陆失败\n`
            continue
        }
        sessionId = JSON.parse(loginResp.body).data.session.id
        await client_id(sessionId)
        await $.wait(parseInt(Math.random() * 2000 + 3000))
        let userInfoResp = await userInfo(sessionId)
        await $.wait(parseInt(Math.random() * 2000 + 3000))
        let taskListResp = await taskList(sessionId)
        let taskListData = JSON.parse(taskListResp.body).data
        await $.wait(parseInt(Math.random() * 2000 + 3000))
        await sign(sessionId)
        await $.wait(parseInt(Math.random() * 2000 + 3000))
        let taskInfos = taskListData.rst.user_task_list
        // console.log(JSON.stringify(taskInfos))
        let isfinished = true
        let localTaskFinished = true
        $.readTime = 0
        for (let taskInfo of taskInfos) {
            let taskName = taskInfo.name
            let finish_times = taskInfo.finish_times
            let frequency = taskInfo.frequency
            let type = taskInfo.member_task_type
            if (finish_times >= frequency) {
                console.log(`    ${taskName} 任务已完成！`)
            } else {
                console.log(`    ${taskName} 任务进度：${finish_times}/${frequency}`)
                if (type <= 5) {
                    isfinished = false
                    $.readTime = Math.max($.readTime, frequency - finish_times)
                }
                if (type == 6) {
                    localTaskFinished = false
                }
            }
        }
        if (!isfinished) {
            let articlesResp = await getArticles(sessionId)
            let articleData = JSON.parse(articlesResp.body).data
            let articleList = articleData.article_list
            console.log(`🎯 本次阅读${Math.min(10, $.readTime)}篇文章`)
            for (let j = 0; j < Math.min(10, $.readTime); j++) {
                let articleId = articleList[j].id
                let articleName = articleList[j].doc_title
                console.log(`🎯 ${articleName}`)
                await read(sessionId, articleId)
                await $.wait(parseInt(Math.random() * 2000 + 10000))
                await like(sessionId, articleId)
                await $.wait(parseInt(Math.random() * 2000 + 5000))
                let commentTxt = ''
                try {
                    let txtResp = await getComment()
                    commentTxt = JSON.parse(txtResp.body).hitokoto
                } catch {
                    commentTxt = `这篇${articleName}文章写的很好，支持！`
                }
                console.log(`🎉 ${commentTxt}`)
                await comment(sessionId, articleId, commentTxt)
                await $.wait(parseInt(Math.random() * 2000 + 5000))
                await share(sessionId, 3, articleId)
                await $.wait(parseInt(Math.random() * 2000 + 10000))
            }
        }
        if (!localTaskFinished) {
            await localLife(sessionId, 6)
            await $.wait(parseInt(Math.random() * 2000 + 5000))
        }
        let commentListResp = await getCommentList(sessionId)
        let commentList = JSON.parse(commentListResp.body).data.comment_list
        if (commentList.length > 0) {
            for (let commentInfo of commentList) {
                let commentId = commentInfo.id
                let content = commentInfo.content
                console.log(`🎯 ${content}`)
                await deleteComment(sessionId, commentId)
                await $.wait(parseInt(Math.random() * 2000 + 5000))
            }
        }
        taskListResp = await taskList(sessionId)
        taskListData = JSON.parse(taskListResp.body).data
        let userName = taskListData.rst.nick_name
        let score = taskListData.rst.total_integral
        console.log(`\n🎉 账号【${phone}】当前积分 ${score}`)
        $.message += `账号【${phone}】当前积分 ${score}\n`
    }

    if ($.message) {
        console.log(`\n==========运行完成==========\n`)
        console.log($.message)
        await notify.sendNotify("爱平阳-APP", $.message)
    }
})()
    .finally(() => {
        $.done();
    })

function credential_auth(phone, pwd) {
    let requestId = generateRequestId()
    let url = "https://passport.tmuyun.com/web/oauth/credential_auth"
    let headers = {
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "passport.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    let encryptPwd = encryptUtil.rsaEncryptByPublicKey(pwd, publicKeyRSA)
    let body = `client_id=${clientId}&password=${encodeURIComponent(encryptPwd)}&phone_number=${phone}`
    let postRequest = {
        url: url,
        method: "POST",
        headers: headers,
        body: body,
        timeout: 30000
    }
    return new Promise(async resolve => {
        $.post(postRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    // console.log(JSON.parse(data))
                } else {
                    console.log(`credential_auth接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function login(authCode, sessionId) {
    let path = '/api/zbtxz/login'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `check_token=9ca17ae2e6fbcda170e2e6eed7f244aeaba3ccf058edb68aa2d15f878e9bb7e54a9094c099f87e82e9f7b7cb72e2f4ee83a132e2a7a895eb44b78baaabb77c839b8fa6c14e96ba8facd340ba9b8dafd2618ee886c300&code=${authCode}&token=&type=-1&union_id=`
    let postRequest = {
        url: url,
        method: "POST",
        headers: headers,
        body: body,
        timeout: 30000
    }
    return new Promise(async resolve => {
        $.post(postRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    console.log('✅ 用户登陆成功！')
                } else {
                    console.log(`credential_auth接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function client_id(sessionId) {
    let path = '/api/account/client_id'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `client_id=`
    let postRequest = {
        url: url,
        method: "POST",
        headers: headers,
        body: body,
        timeout: 30000
    }
    return new Promise(async resolve => {
        $.post(postRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    // console.log('✅ client_id接口调用成功！')
                } else {
                    console.log(`client_id接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function userInfo(sessionId) {
    let path = '/api/user_mumber/account_detail'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let getRequest = {
        "url": url,
        "headers": headers
    }
    return new Promise(async resolve => {
        $.get(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    console.log(`✅ 用户信息获取成功！`)
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function taskList(sessionId) {
    let path = '/api/user_mumber/numberCenter'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}?is_new=1`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let getRequest = {
        "url": url,
        "headers": headers
    }
    return new Promise(async resolve => {
        $.get(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {

                } else {
                    console.log(`获取任务列表失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function sign(sessionId) {
    let path = '/api/user_mumber/sign'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}?is_new=1`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let getRequest = {
        "url": url,
        "headers": headers
    }
    return new Promise(async resolve => {
        $.get(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 签到成功：${res.data.signCommonInfo.date}，获得${res.data.signExperience}积分`)
                    } else {
                        console.log(`签到失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function getArticles(sessionId) {
    let path = '/api/article/channel_list'
    let requestId = generateRequestId().toUpperCase()
    $.list_count = 40
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}?channel_id=${channelId}&is_new=1&list_count=${$.list_count}&size=10&start=${moment().valueOf()}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let getRequest = {
        "url": url,
        "headers": headers
    }
    return new Promise(async resolve => {
        $.get(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    if (res.code == 0) {
                        console.log(`✅ 获取文章列表成功`)
                    } else {
                        console.log(`获取文章失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function read(sessionId, articleId) {
    let path = '/api/article/detail'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}?id=${articleId}&tenantId=${sid}&url_Path=/webDetails/news`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let getRequest = {
        "url": url,
        "headers": headers
    }
    return new Promise(async resolve => {
        $.get(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 阅读成功`)
                    } else {
                        console.log(`阅读文章失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function getCommentList(sessionId) {
    let path = '/api/account_comment/comment_list'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}?ZMC_CommunityRequest=0&size=10`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let getRequest = {
        "url": url,
        "headers": headers
    }
    return new Promise(async resolve => {
        $.get(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 获取评论列表成功`)
                    } else {
                        console.log(`获取评论列表失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function deleteComment(sessionId, commentId) {
    let path = '/api/comment/delete'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `ZMC_CommunityRequest=0&comment_id=${commentId}`
    let getRequest = {
        "url": url,
        "headers": headers,
        "body": body,
        "method": "POST"
    }
    return new Promise(async resolve => {
        $.post(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 删除评论成功`)
                    } else {
                        console.log(` 删除评论失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function like(sessionId, articleId) {
    let path = '/api/favorite/like'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `action=1&id=${articleId}`
    let getRequest = {
        "url": url,
        "headers": headers,
        "body": body,
        "method": "POST"
    }
    return new Promise(async resolve => {
        $.post(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 点赞成功`)
                    } else {
                        console.log(`点赞文章失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function comment(sessionId, articleId, txt) {
    let path = '/api/comment/create'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `channel_article_id=${articleId}&content=${encodeURIComponent(txt)}&video_rel_id=`
    let getRequest = {
        "url": url,
        "headers": headers,
        "body": body,
        "method": "POST"
    }
    return new Promise(async resolve => {
        $.post(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 评论成功`)
                    } else {
                        console.log(`评论文章失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function share(sessionId, member_type, articleId) {
    let path = '/api/user_mumber/doTask'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `member_type=${member_type}&target_id=${articleId}`
    let getRequest = {
        "url": url,
        "headers": headers,
        "body": body,
        "method": "POST"
    }
    return new Promise(async resolve => {
        $.post(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 分享成功`)
                    } else {
                        console.log(`评论文章失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function localLife(sessionId, member_type) {
    let path = '/api/user_mumber/doTask'
    let requestId = generateRequestId().toUpperCase()
    let now = moment().valueOf()
    let raw = `${path}&&${sessionId}&&${requestId}&&${now}&&FR*r!isE5W&&${sid}`
    let sign = encryptUtil.sha256Decrypt(raw)
    let url = `https://vapp.tmuyun.com${path}`
    let headers = {
        "X-SESSION-ID": sessionId,
        "User-Agent": "ANDROID;10;62;5.0.0;1.0;null;Redmi Note 7 Pro",
        "X-REQUEST-ID": requestId,
        "X-SIGNATURE": sign,
        "X-TIMESTAMP": now,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Host": "vapp.tmuyun.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "X-TENANT-ID": sid
    }
    let body = `member_type=${member_type}`
    let getRequest = {
        "url": url,
        "headers": headers,
        "body": body,
        "method": "POST"
    }
    return new Promise(async resolve => {
        $.post(getRequest, (err, resp, data) => {
            try {
                if (resp.statusCode == 200) {
                    let res = JSON.parse(resp.body)
                    // console.log(res)
                    if (res.code == 0) {
                        console.log(`✅ 本地生活任务完成`)
                    } else {
                        console.log(`本地生活任务失败!`)
                    }
                } else {
                    console.log(`查询用户信息接口调用失败：${err}`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function getComment() {
    let options = {
        method: 'GET',
        url: 'https://v1.hitokoto.cn/',
        qs: { c: 'd' },
        headers: { 'content-type': 'multipart/form-data; boundary=---011000010111000001101001' }
    };
    //console.log(options);
    return new Promise(async resolve => {
        $.get(options, (err, resp, data) => {
            try {
                if (JSON.parse(resp.body).id) {
                    console.log(`🎉 获取评论成功！`)
                }
            } catch (e) {
                // console.log(data);
                console.log(e, resp)
            } finally {
                resolve(resp);
            }
        })
    })
}

function generateRequestId() {

    return `${commonUtil.randomStr(false, 8)}-${commonUtil.randomStr(false, 4)}-${commonUtil.randomStr(false, 4)}-${commonUtil.randomStr(false, 4)}-${commonUtil.randomStr(false, 12)}`
}

function getPostRequestJson(url, body, userSession, method = "POST") {
    let headers = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": " okhttp-okgo/jeasonlzy",
        "resouce": "OleApp",
        "channel": "ios",
        "Tenant": " VGDT",
        "Touch-Point": "APP_IOS",
        "Tenant-Channel": "OLE",
        "Content-Type": "application/json;charset=utf-8",
        "Host": "ole-app.crvole.com.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    if (userSession) {
        headers['sessionId'] = userSession
        headers['Cookie'] = `isid=${userSession}`
    }
    // console.log(JSON.stringify(body))
    return { url: url, method: method, headers: headers, body: JSON.stringify(body), timeout: 30000 };
}

function getPostRequestFormUrlLencoded(url,
    body,
    hearder = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": 'app.mixcapp.com',
        "User-Agent": $.UA || 'okhttp/3.12.12',
        "X-Requested-With": "XMLHttpRequest"
    },
    method = "POST") {
    let headers = hearder
    return { url: url, method: method, headers: headers, body: body, timeout: 30000 };
}

// prettier-ignore
function Env(t, e) { "undefined" != typeof process && JSON.stringify(process.env).indexOf("GITHUB") > -1 && process.exit(0); class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return "POST" === e && (s = this.post), new Promise((e, i) => { s.call(this, t, (t, s, r) => { t ? i(t) : e(s) }) }) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new class { constructor(t, e) { this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `🔔${this.name}, 开始!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } isSurge() { return "undefined" != typeof $httpClient && "undefined" == typeof $loon } isLoon() { return "undefined" != typeof $loon } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const i = this.getdata(t); if (i) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise(e => { this.get({ url: t }, (t, s, i) => e(i)) }) } runScript(t, e) { return new Promise(s => { let i = this.getdata("@chavy_boxjs_userCfgs.httpapi"); i = i ? i.replace(/\n/g, "").trim() : i; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r; const [o, h] = i.split("@"), n = { url: `http://${h}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": o, Accept: "*/*" } }; this.post(n, (t, e, i) => s(i)) }).catch(t => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e); if (!s && !i) return {}; { const i = s ? t : e; try { return JSON.parse(this.fs.readFileSync(i)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path"); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), i = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const i = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of i) if (r = Object(r)[t], void 0 === r) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, i, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}"; try { const e = JSON.parse(h); this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i) } catch (e) { const o = {}; this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i) } } else s = this.setval(t, e); return s } getval(t) { return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null } setval(t, e) { return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null } initGotEnv(t) { this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = (() => { })) { t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar } } catch (t) { this.logErr(t) } }).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) })) } post(t, e = (() => { })) { if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.post(t, (t, s, i) => { !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i) }); else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => e(t)); else if (this.isNode()) { this.initGotEnv(t); const { url: s, ...i } = t; this.got.post(s, i).then(t => { const { statusCode: s, statusCode: i, headers: r, body: o } = t; e(null, { status: s, statusCode: i, headers: r, body: o }, o) }, t => { const { message: s, response: i } = t; e(s, i, i && i.body) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date; let i = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds() }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in i) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? i[e] : ("00" + i[e]).substr(("" + i[e]).length))); return t } msg(e = t, s = "", i = "", r) { const o = t => { if (!t) return t; if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? { "open-url": t } : this.isSurge() ? { url: t } : void 0; if ("object" == typeof t) { if (this.isLoon()) { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } if (this.isQuanX()) { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl; return { "open-url": e, "media-url": s } } if (this.isSurge()) { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } } }; if (this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r))), !this.isMuteLog) { let t = ["", "==============📣系统通知📣=============="]; t.push(e), s && t.push(s), i && t.push(i), console.log(t.join("\n")), this.logs = this.logs.concat(t) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { const s = !this.isSurge() && !this.isQuanX() && !this.isLoon(); s ? this.log("", `❗️${this.name}, 错误!`, t.stack) : this.log("", `❗️${this.name}, 错误!`, t) } wait(t) { return new Promise(e => setTimeout(e, t)) } done(t = {}) { const e = (new Date).getTime(), s = (e - this.startTime) / 1e3; this.log("", `🔔${this.name}, 结束! 🕛 ${s} 秒`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t) } }(t, e) }
