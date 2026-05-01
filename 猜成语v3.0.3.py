import easygui,random,os,time,pygame
# 初始化pygame
pygame.init()

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

TOTAL_TIME = 200
xue = 3
nnnn = 0
pai = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706"
easygui.msgbox("欢迎来到猜成语游戏，作者丰子恺")
pdsfks = easygui.msgbox("你只有200秒的时间答对所有猜成语的题，good luck!!!!!!!")
nmnmn = easygui.msgbox("你有3次机会，每次机会你可以猜10个成语")
easygui.msgbox("用英文输拼音也行！！！")
easygui.msgbox("这是v3.0.3版本，更新了许多彩蛋与猜成语图片，欢迎play！")
bcnb = easygui.enterbox("来将可留姓名？")
if bcnb == "ZXH" or bcnb == "FZK" or bcnb == "LMF":
    psd = easygui.enterbox("请输入password(圆周率的后98位全部数字(包含3)):")
    if psd == "SBSN" or psd == "YBSB" or psd == pai:
        xue = int(easygui.enterbox("54灯神，我可以实现你two个愿望，请输入你想要的血量:"))
        nnnn = int(easygui.enterbox("请输入你想要的分数:"))
    else:
        easygui.msgbox("来将可留生命？")
        exit()
elif bcnb == "傻逼" or bcnb == "智障" or bcnb == "shabi" or bcnb == "zhizhang":
        easygui.msgbox("你是一个傻逼或智障啊，那么...你就只有一条命")
        xue = 1
elif bcnb == "人机" or bcnb == "renji":
        easygui.msgbox("你是一个人机，那么...你就没有血量")
        xue = 0
elif bcnb == "黑客" or bcnb == "heike":
        easygui.msgbox("黑客是吧，恭喜你，你可以滚了")
        exit()
elif bcnb == "恭喜你发财" or bcnb == "gongxinifacai":
        easygui.msgbox("恭喜你发财,恭喜你精彩")
        easygui.msgbox("恭喜你，你被我恭喜了，恭喜你，恭喜你，恭喜你，恭喜你，")
        easygui.msgbox("好运留下来了，另外你也可以滚了bye!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()
elif bcnb == "牛逼" or bcnb == "niubi":
        easygui.msgbox("来将可留生命")
        exit()
if pdsfks == 'OK':
    easygui.msgbox("猜成语开始")
    start_time = time.time()
shuzu = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png","11.jpg","12.jpg","13.jpg","14.jpg","15.jpg","16.jpg","17.jpg","18.jpg","19.jpg","20.jpg"]
da = ["一泻千里","一帆风顺","归心似箭","风和日丽","虎头蛇尾","手足同心","翻山越岭","三令五申","只手遮天","血口喷人","是非不分","茅塞顿开","井底之蛙","雕虫小技","四脚朝天","鬼话连篇","百年树人","扬眉吐气","能屈能伸","爱恨分明"]
da2 = ["yixieqianli","yifanfengshun","guixinsijian","fengherili","hutoushewei","shouzutongxin","fanshanyueling","sanlingwushen","zhishouzhetian","xuekoupenren","shifeibufen","maosedunkai","jingdizhiwa","diaochongxiaoji","sijiaochaotian","guihualianpian","bainianshuren","yangmeituqi","nengqunengshen","aihenfenming"]
while True:
    for i in range(12):
        if xue == 0:
            easygui.msgbox("你输了！")
            exit()
        nm = random.randint(0, len(shuzu)-1)
        image_path = os.path.join(script_dir, "好东西", shuzu[nm])
        if not os.path.exists(image_path):
            easygui.msgbox(f"文件不存在: {image_path}\n脚本目录: {script_dir}")
            continue
        easygui.msgbox("请猜下面的成语", image=image_path)
        zc = easygui.enterbox("这是什么成语呢？")
        if zc is None:
            zc = "我不知道"

        if zc == "我不知道":
            easygui.msgbox("不知道？不知道受着呗")
            xue -= 1
        elif zc == da[nm] or zc == da2[nm]:
            easygui.msgbox("你猜对了")
            # 使用pygame播放录音.mp3
            audio_path = os.path.join(script_dir, "好东西", "真棒.mp3")
            if os.path.exists(audio_path):
                try:
                    pygame.mixer.music.load(audio_path)
                    pygame.mixer.music.play()
                except:
                    pass
            nnnn += 10
            if nnnn == 60:
                sbs54 = easygui.msgbox("你是5.4班的人吗？")
                if sbs54 == 'OK':
                    class_image_path = os.path.join(script_dir, "好东西", "班级群邀请图片.jpg")
                    os.system(f"start {class_image_path}")
                    easygui.msgbox("这是班群，你可以加入")
                    xue += 1
                    TOTAL_TIME += 60
                    nnnn += 10
                else:
                    win10_path = os.path.join(script_dir, "好东西", "win10.png")
                    os.system(f"start {win10_path}")
                    easygui.msgbox("继续答题！！！争取猜对所有题")
                    xue += 1
                    TOTAL_TIME += 60
                continue
        else:
            easygui.msgbox("你猜错了")
            xue -= 1
            continue
        if i == 9:
            break
    easygui.msgbox("你猜对了猜成语v3.0.3终极版中的所有题，你胜利了！！！")
    exit()
