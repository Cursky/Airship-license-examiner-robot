# Airship-license-examiner-robot


## 本项目基于PaddleVideo开发，利用手势识别模型完成微信聊天机器人的构建

项目视频链接：
哔哩哔哩：https://www.bilibili.com/video/BV1JU4y177s7
Aistudio：https://aistudio.baidu.com/aistudio/projectdetail/2331262

## 1.1项目实现步骤


1.构建wechaty服务器：
!docker pull wechaty/wechaty:latest

!export WECHATY_LOG="verbose"

!export WECHATY_PUPPET="wechaty-puppet-wechat"

!export WECHATY_PUPPET_SERVER_PORT="8080"

!export WECHATY_TOKEN="puppet_padlocal_xxxxxx" # 这里输入你自己的token

!docker run -ti --name wechaty_puppet_service_token_gateway --rm -e WECHATY_LOG -e WECHATY_PUPPET -e WECHATY_TOKEN -e WECHATY_PUPPET_SERVER_PORT -p "$WECHATY_PUPPET_SERVER_PORT:$WECHATY_PUPPET_SERVER_PORT" wechaty/wechaty:latest


2.git PaddleVideo到本地


3.cd
4.下载训练好的模型到本地


不会训练的可以参考：

https://aistudio.baidu.com/aistudio/projectdetail/2298774


5.修改部分代码 


6.终端运行 sh run.sh
