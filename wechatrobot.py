##微信证件照助手 利用paddleseg进行图像分割来完成背景换底

import os
import asyncio
from predict import hands_predict#导入手势识别预测代码


from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)
robot_state = 0 #机器人状态


async def on_message(msg: Message):
    talker = msg.talker()
    global robot_state
    if msg.text() == 'ding':
        await msg.say('这是自动回复: dong dong dong')
    if msg.text() == 'hi' or msg.text() == '你好':
        await talker.say('考生你好，欢迎来到飞船驾照考试中心，本次考试科目为：自动挡星际飞船科目三，我将引导你完成考试，祝你获得一个好成绩！')
        await talker.say('自动挡星际飞船为新一代无操控台飞船，为迎合银河系绿色出行理念，飞船全部由手势动作完成操纵，祝您好运，再您做好准备后请对我说“开始考试”')
    if msg.text() == '开始考试':
        await talker.say('考试已开始，目前考核科目为3-1')
        await talker.say('考试内容为：做出点击手势，击碎眼前障碍物，为飞船疏通航道')
        file_box_final_result = FileBox.from_file('./game_img/test1_1.png')
        robot_state=1
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")

    if msg.text() == '开始科目3-2考试':
        await talker.say('考试已开始，目前考核科目为3-2')
        await talker.say('考试内容为：做出放大手势，放大飞船体积，利用体积威慑前来的星际海盗')
        file_box_final_result = FileBox.from_file('./game_img/test2_1.png')
        robot_state=2
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")
    if msg.text() == '开始科目3-3考试':
        await talker.say('考试已开始，目前考核科目为3-3')
        await talker.say('考试内容为：控制飞船左转，请做出左转手势')
        file_box_final_result = FileBox.from_file('./game_img/test3_1.png')
        robot_state = 3
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")
    if msg.text() == '开始科目3-4考试':
        await talker.say('考试已开始，目前考核科目为3-4')
        await talker.say('考试内容为：控制飞船右转，请做出右转手势')
        file_box_final_result = FileBox.from_file('./game_img/test4_1.png')
        robot_state = 4
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")
    if msg.text() == '开始科目3-5考试':
        await talker.say('考试已开始，目前考核科目为3-5')
        await talker.say('考试内容为：为保证飞船虫洞跳跃中行驶过程安全，请做出缩小手势，缩小飞船进行跳跃')
        file_box_final_result = FileBox.from_file('./game_img/test5_1.png')
        robot_state = 5
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")
    if msg.text() == '开始科目3-6考试':
        await talker.say('考试已开始，目前考核科目为3-6')
        await talker.say('考试内容为：进入虫洞后遇到旋转时空涡流，请做出旋转手势控制飞船旋转')
        file_box_final_result = FileBox.from_file('./game_img/test6_1.png')
        robot_state = 6
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")
    if msg.text() == '开始科目3-7考试':
        await talker.say('考试已开始，目前考核科目为3-7')
        await talker.say('考试内容为：航行途中会遇到各种稀有矿物，做出抓取手势让飞船对矿物进行抓取')
        file_box_final_result = FileBox.from_file('./game_img/test7_1.png')
        robot_state = 7
        await talker.say(file_box_final_result)#发送预先准备好的考试图片
        await talker.say("请考生发送考试视频")
    if msg.text() == '视频':
        robot_state = 3
        await talker.say('请发送视频')
    if msg.text() == 'test':
        robot_state = 4
        await talker.say('请发送视频')

     
    if robot_state == 1 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
        #  测试
        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 0:#识别为点击动作
            
            file_box_final_result = FileBox.from_file('./game_img/test1_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜完成，请开始下一阶段考试，对我说“开始科目3-2考试”')
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")
    
    if robot_state == 2 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:

        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 1:#识别为放大动作
            
            file_box_final_result = FileBox.from_file('./game_img/test2_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜完成，请开始下一阶段考试，对我说“开始科目3-3考试”')
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")
    if robot_state == 3 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
  
        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 2:#识别为左滑动作
            
            file_box_final_result = FileBox.from_file('./game_img/test3_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜完成，请开始下一阶段考试，对我说“开始科目3-4考试”')
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")
    if robot_state == 4 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
  
        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 3:#识别为右滑动作
            
            file_box_final_result = FileBox.from_file('./game_img/test4_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜完成，请开始下一阶段考试，对我说“开始科目3-5考试”')
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")


    if robot_state == 5 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
  
        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 4:#识别为缩小动作
            
            file_box_final_result = FileBox.from_file('./game_img/test5_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜完成，请开始下一阶段考试，对我说“开始科目3-6考试”')
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")


    if robot_state == 6 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
  
        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 5:#识别为旋转动作
            
            file_box_final_result = FileBox.from_file('./game_img/test6_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜完成，请开始下一阶段考试，对我说“开始科目3-7考试”')
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")

    if robot_state == 7 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
  
        await talker.say('已收到考试视频，开始评判中')
        # 将Message转换为FileBox
        file_box_user_video = await msg.to_file_box()
    
        # 获取视频名
        video_name = file_box_user_video.name
    
        # 视频保存的路径
        video_path = './video_predict/' + video_name
    
        # 将视频保存为本地文件
        await file_box_user_video.to_file(file_path=video_path)
        
        hands_result=hands_predict(video_path)#获取预测结果

        if hands_result == 6:#识别为抓取动作
            
            file_box_final_result = FileBox.from_file('./game_img/test7_2.png')
            robot_state = 0
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
            await talker.say('恭喜你，完成了驾照考试！”')
            file_box_final_result = FileBox.from_file('./game_img/test7_3.png')
            await talker.say(file_box_final_result)#发送预先准备好的考试图片
        else:
            robot_state = 0
            await talker.say("动作错误或不规范，未能通过，为了银河系的交通安全，请您重新开始考试。")
    # if robot_state == 4 and msg.type() == Message.Type.MESSAGE_TYPE_VIDEO:
    #     #  测试
    #     await talker.say('已收到图像，开始更换中')
    #     # 将Message转换为FileBox
    #     file_box_user_image = await msg.to_file_box()
    
    #     # 获取图片名
    #     img_name = file_box_user_image.name
    
    #     # 图片保存的路径
    #     img_path = './video_predict/' + img_name
    
    #     # 将图片保存为本地文件
    #     await file_box_user_image.to_file(file_path=img_path)



    

async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    print(user)


async def main():
    # 确保我们在环境变量中设置了WECHATY_PUPPET_SERVICE_TOKEN
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan',      on_scan)
    bot.on('login',     on_login)
    bot.on('message',   on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())