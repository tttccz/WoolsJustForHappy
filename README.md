# WoolsJustForHappy

![GitHub issues](https://img.shields.io/github/issues/KD-happy/KDCheckin?logo=github) ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/KD-happy/KDCheckin?logo=github) ![GitHub forks](https://img.shields.io/github/forks/KD-happy/KDCheckin?logo=github) ![GitHub Repo stars](https://img.shields.io/github/stars/KD-happy/KDCheckin?logo=github)

![GitHub last commit](https://img.shields.io/github/last-commit/KD-happy/KDCheckin?logo=github) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/KD-happy/KDCheckin?logo=github) ![GitHub repo size](https://img.shields.io/github/repo-size/KD-happy/KDCheckin?logo=github)

## 免责声明

- 本仓库发的任何脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
- 本人无法100%保证使用本项目之后不会造成账号异常问题，若出现任何账号异常问题本人概不负责，请根据情况自行判断再下载执行！否则请勿下载运行！
- 如果任何单位或个人认为该项目的脚本可能涉及侵犯其权利，则应及时通知并提供相关证明，我将在收到认证文件后删除相关脚本。
- 任何以任何方式查看此项目的人或直接或间接使用本项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或本项目的规则，则视为您已接受此免责声明。

> 您使用或者复制了本仓库且本人制作的任何脚本，则视为 `已接受` 此声明，请仔细阅读

##  简单的操作

拉取本库
```shell
ql repo https://github.com/tttccz/WoolsJustForHappy "" "" "notify|sendNotify" main
```

## 详细操作

**1.安装 docer**

[可以看一下](https://zhuanlan.zhihu.com/p/387337954)

更新 yum, 确保 yum 包更新到最新
``` shell
sudo yum update
```

安装的yum工具集
```shell
yum install -y yum-utils
```

安装docker-ce的yum源:
```shell
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```
[可以看一下](https://blog.csdn.net/weixin_46152207/article/details/111354882)

安装docker-ce
```shell
dnf install docker-ce
```
或者yum安装
```shell
yum install docker-ce
```

查看docker服务状态
```shell
systemctl status docker.service
```

开启自启动
```shell
systemctl enable docker.service
```

开启服务
```shell
systemctl start docker.service
```

**2.安装**

拉取镜像文件
```shell
docker pull whyour/qinglong:latest
```

创建容器
```shell
docker run -dit \
  -v $pwd/ql:/ql/data \
  -p 5700:5700 \
  --name qinglong \
  --hostname qinglong \
  --restart unless-stopped \
  whyour/qinglong:latest
```

创建第二个容器
```shell
docker run -dit \
  -v $PWD/ql:/ql/data \
  -p 5800:5700 \
  --name qinglong \
  --hostname qinglong \
  --restart unless-stopped \
  whyour/qinglong:latest
```

## 本仓库的文件列表

<details>
<summary>文件说明</summary>

```
│  apy.js              # 爱平阳
│  bsys.py             # 步数有赏
│  djjs.js             # 多娇江山
│  hlbs.py             # 欢乐步数
│  lc.js               # 仑传
│  lkrd.py             # 乐看热点
│  qmzljb.py           # 全民走路计步
│  ttzlpro.py          # 天天走路pro
│  xsgjz.py            # 小时工记账
│  ydkc.js             # 运动柯城
│  ylw.js              # 悦龙湾
│  zslc.js             # 掌上鹿城
│  zsyk.js             # 掌上永康
```

</details>

## 推送配置

[企业微信应用通知粗略教程](http://note.youdao.com/noteshare?id=874fe7233f8cec295bb3d01d38296727&sub=16035CD41B844F179DA230AB9FC531D4)

[企业微信推送设置](http://note.youdao.com/noteshare?id=b7322046a431975dff59c75025e1d2f3&sub=9A27E09849CB414890CBC094B43A43EF)

[获取钉钉自定义机器人webhook](http://note.youdao.com/noteshare?id=25d15ba93ca80a29cfbf550078d096a8&sub=78340C89F0BB4295A4E559E12ED2EC83)

## 支持脚本

🟢: 正常运行 🔴: 脚本暂不可用 🔵: 可以执行(需更新) 🟡: 待测试 🟤: 看脸
| 名称         | 备注        | 方式         | 备注     | 当前状态 |
| ------------ | ----------- | ------------ | -------- | -------- |
| 爱平阳       | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢️        |
| 步数有赏     | 签到+做任务 | cookie       | 每天1元  | 🟢️        |
| 多娇江山     | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢️        |
| 欢乐步数     | 签到+做任务 | cookie       | 每天1元  | 🟢️        |
| 仑传         | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢        |
| 乐看热点     | 签到+做任务 | cookie       | 每天1元  | 🟢️        |
| 全民走路计步 | 签到+做任务 | cookie       | 积分兑换 | 🟢        |
| 天天走路pro  | 签到+做任务 | cookie       | 攒分提现 | 🟢        |
| 小时工记账   | 签到+做任务 | cookie       | 攒分提现 | 🟢        |
| 运动柯城     | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢        |
| 悦龙湾       | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢        |
| 掌上鹿城     | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢        |
| 掌上永康     | 签到+做任务 | 手机号、密码 | 积分兑换 | 🟢        |

## 已下架

🟢: 正常运行 🔴: 脚本暂不可用 🔵: 可以执行(需更新) 🟡: 待测试 🟤: 看脸
| 名称 | 备注 | 签到方式 | 来源 | 当前状态 |
| ---- | ---- | -------- | ---- | -------- |
| 无   |      |          |      |          |

## 特别说明

无
