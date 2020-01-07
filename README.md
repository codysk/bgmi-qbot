# BGmi-qbot

基于[python-aiocqhttp](https://github.com/richardchien/python-aiocqhttp) 的BGmi QQ机器人
目前实现的功能
+ BGmi 站点的番组出现更新时的QQ通知
+ 管理(增/删)通知发往讨论组/群
+ 其他的还没想好做啥。。(

## 环境要求

由于使用了二进制分发的coolq所以对CPU架构有要求
其他的需要的依赖基本上都可以在docker里完成
+ Docker环境
+ X86_64CPU架构（由于依赖的coolq的程序需要运行于X86_64之上）
+ docker-composer (建议，用于编排容器)

## 部署安装

建议使用docker-composer进行容器编排

一个docker-compose.yml的例子
```
version: '3'
services:
  bgmi-qbot:
    build:
      context: .
    environment:
      - admin_qq=<Admin QQ Account>
      - log_level=ERROR
      - bgmi_api=<bgmi index api address>
    volumes:
      - ./data:/data

  cqhttp:
    image: richardchien/cqhttp
    environment:
      - VNC_PASSWD=<vncpassword>
      - COOLQ_ACCOUNT=<Bot QQ Account>
      - CQHTTP_SERVE_DATA_FILES=true
      - CQHTTP_USE_HTTP=false
      - CQHTTP_USE_WS_REVERSE=true
      - CQHTTP_WS_REVERSE_URL=ws://bgmi-qbot:8080/ws/
    volumes:
      - ./.coolq:/home/user/coolq
    ports:
      - 9000:9000
```

有几个环境变量需要在docker-compose配置文件中指定

| 变量名 | 含义 | 必须 | 默认值 |
| ------ | ------ | ------ | ------ |
| api_root | CoolQHttpApi的url |  | False |
| enable_http_post | 是否启用CoolQHttpApi（不启用是使用websocket反向连接） |  | False |
| access_token | CoolQ Access_Token |  | False |
| secret | CoolQ secret |  | False |
| admin_qq | 管理员的Q号 | * | None |
| enable_public_command | 公共指令的开放等级(Always总是开放/Subscriber对订阅的群与讨论组开放/Never永不) | | Always |
| log_level | 日志等级(ERROR/WARNING/INFO/DEBUG) |  | ERROR |
| bgmi_api | BGmi首页api的url |  | http://127.0.0.1/api/index |
| VNC_PASSWD | CoolQ容器的noVNC服务密码 | * | 见richardchien/cqhttp项目 |
| COOLQ_ACCOUNT | QQ机器人的Q号 | * | 见richardchien/cqhttp项目 |
| CQHTTP_SERVE_DATA_FILES | 与示例保持一致 | * | 见richardchien/cqhttp项目 |
| CQHTTP_USE_WS_REVERSE | 与示例保持一致 | * | 见richardchien/cqhttp项目 |
| CQHTTP_WS_REVERSE_URL | 与示例保持一致 | * | 见richardchien/cqhttp项目 |

做好docker-compose.yml配置文件后
```
docker-compose up -d
```
启动服务 启动时可以通过`docker-compose logs`查看启动日志

启动完成后访问http://<部署服务器ip>:9000访问coolq的noVNC服务完成QQ登录

## 使用方式

用管理员账号私聊机器人 或在将机器人加入讨论组/群 均可使用管理指令
### 管理员指令
+ `/set` 将当前 讨论组/群 加入到番组更新的通知列表中
+ `/getlist` 获取当前所有接受通知的 讨论组/群
+ `/remove <discuss/group> <id> [<id>...]` 从通知列表中删除 讨论组/群
+ 待更新

### 用户指令
+ `/ping` 返回pong 用来确认机器人程序是否在线
+ `/status` 获取当前订阅的番剧的更新状态
+ 待更新


