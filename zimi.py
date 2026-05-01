# -*- coding: utf-8 -*-
import pygame, random, os, time, json
from colorama import init, Fore, Style
from pygame.locals import *
pygame.init()
init(autoreset=True)
#=======================================================================================================================
COLOR = {
    "forest": Fore.GREEN,
    "castle": Fore.LIGHTBLACK_EX,
    "space": Fore.LIGHTBLUE_EX,
    "danger": Fore.RED,
    "save": Fore.YELLOW,
    "end": Fore.YELLOW,
    "input_prompt": Fore.LIGHTYELLOW_EX,
    "normal": Fore.WHITE,
    "sky": Fore.BLUE
}
#=======================================================================================================================
def print_slow(text, delay=0.1, color=COLOR["normal"]):
    for char in text:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)
#=======================================================================================================================
window1 = pygame.display.set_mode(size=(700, 800))
font = pygame.font.Font('microsoft black.ttf', 36)
bg = pygame.image.load('img/caimiyu.png')
menu = "题"
HP = 3
score = 0
kaifa = False
kaifazhe = [90, 88, 72, 76, 77, 70, 70, 90, 75]
shang = False
Yesscore = 0
CD1 = "windows11"
CD2 = "banqun"
CD3 = "laoshi"
print_slow("来将可留姓名？", 0.1, color=COLOR["space"])
minzi = input()
print_slow(f"这{minzi}有力气......", 0.1, color=COLOR["space"])
#=======================================================================================================================
try:
    with open('admin.json', 'r', encoding='utf-8') as f:
        kfz = json.load(f)
    with open('admin2.json', 'r', encoding='utf-8') as f:
        kfz2 = json.load(f)
except:
    kfz = "admin"
    kfz2 = "vip"
#=======================================================================================================================
if minzi == "paihang":
    print_slow("已开启排行",0.2,color=COLOR["space"])
    os.system("排行.bat")
    quit()
if minzi == "chengxiaodian" or minzi == "CXD":
    bg = pygame.image.load('img/bg.png')
    minzi = Fore.YELLOW + "【程小典】" + Fore.WHITE + "程小典"
if minzi == 'ZXH_MC' or minzi == 'FZK_MC' or minzi == 'LMF':
    minzi = Fore.LIGHTBLUE_EX + "【开发】" + Fore.WHITE + minzi
if minzi == kfz or minzi == kfz2:
    print_slow("进入开发者模式!", 0.05, color=COLOR["space"])
    for i in range(0, 9):
        pwd_input = input(Fore.LIGHTBLUE_EX + "输入密码qwq:" + Fore.BLUE)
        if kaifazhe[i] == ord(pwd_input):
            os.system("cls")
            print_slow("密码正确", 0.05, color=COLOR["space"])
        else:
            print_slow("密码错误", 0.05, color=COLOR["space"])
            time.sleep(1)
            quit()
    kaifa = True
if kaifa:
    print_slow("请输入你想要的score", 0.1, color=COLOR["sky"])
    score = int(input())
    print_slow("请输入你想要的HP", 0.1, color=COLOR["sky"])
    HP = int(input())
    print_slow("请输入你想要的BG(数字)", 0.1, color=COLOR["sky"])
    bgsum = int(input())
    minzi = "某个开发者或VIP"
    if bgsum == 1:
        bg = pygame.image.load('img/qwq.png')
    if bgsum == 2:
        bg = pygame.image.load('好东西/班级群邀请图片2.jpg')
    if bgsum == 3:
        bg = pygame.image.load('img/bg.png')
elif minzi == CD1:
    bg = pygame.image.load('img/qwq.png')
    score = 0
elif minzi == CD2:
    bg = pygame.image.load('好东西/班级群邀请图片2.jpg')
    score = 0
elif minzi == CD3:
    print_slow('真的是老师吗？（是请输入yes）',0.05,color=COLOR["space"])
    laoshi = input()
    if "yes" == laoshi :
        print_slow("敢问老师姓氏？qwq",0.05,color=COLOR["space"])
        minzi = Fore.RED + "【老师】" +Fore.WHITE + input() + "老师"
        print_slow("欢迎"+minzi+"来玩,不过既然是老师,自然难度要提升qwq",0.05,color=COLOR["space"])
        HP = 1
    else:
        print_slow("不是老师，请同学重输",0.05,color=COLOR["space"])
        minzi = input()
        if minzi == CD3:
            print_slow("还有第二关？",0.05,color=COLOR["space"])
            time.sleep(1)
            quit()
#=======================================================================================================================
else:
    score = 0
miyu = [
'正字少一横不作止字猜','田中','休要丢人现眼','多一半','箭在弦','旭日东升','有心得志','有目共睹','山上还有山','十张口一颗心','说它小下边大说它大上边小','一只黑狗不叫不吼','差一点六斤','家中添一口','自小在一起目前少联系','一人一张口下面长只手','四面都是山山山都相连','种花要除草一人来一刀','存心不让出大门你说烦人不烦人','一只狗两个口谁遇它谁发愁','皇帝新衣','格外大方','需要一半留下一半','一月一日非今天','综合门市','守门员','有人偷车','半青半紫','身残心不残','千里丢一百里丢一','一人在内','一人腰上挂把弓','一口吃掉牛尾巴','一口咬定','一大二小','一个人搬两个土','一个礼拜','一家十一口','一只狗四个口','一边是红一边是绿一边怕风一边怕雨','七人头上长了草','九只鸟','九号','九辆车','人不在其位','人有他则变大','人无信不立','刀出鞘','十一个读书人','十日十月','十个哥哥','三口重叠莫把品字猜','三张纸','上下串通','雷不雨','大丈夫不得出头','雨落在横山上','小姑娘','山上复山','不要讲话','互吻','五十对耳朵','五口之家旁种一树','公而忘私','反比','天上无二合去一口家家都有','天天','夫人何处去','太阳西边下月儿东边挂','心如刀刺','手提包','文武两全','日复一日','十字架下三个人','一大二小','一人在内','一人一口','半取半送','出多一半','半个月亮','有声有色','上气接下气','牛走独木桥','说话带京腔','石头砸中皮','床前明月光','大王头上有一人','秀才进门把门关','蝴蝶虫跑水来伴','传旁人去车来换','“山”底上一亩田','三人一日去观景','厂里有个白小子','两个先生捡贝壳','口里吃个大玉米','心里想着耍赖皮','一位先生要走了','今天心里很高兴','一只小手拔萝卜','大米青菜一起吞','半放红梅','一只小帆船，载着一粒米，向东又向西，不知道到哪里','一字生得巧，四面八只脚','一大二小','一口咬去多半截','一口吃掉牛尾巴','一加一不是二','一斗米','一月七日','一夜又一夜','一只狗，站在门口，吃没吃，口水流','一人在内','一人一口','一人一张口，口下长只手','一人腰上挂把弓','一个礼拜','一家十一口','一只狗四个口','七人头上长了草','九只鸟','九号','九辆车','人不在其位','人有他则变大','人无信不立','刀出鞘','十一个读书人','十日十月（武昌起义）','十个哥哥','三口重叠，莫把品字猜','三张纸','上下串通','大丈夫不得出头','小土堆','山连山','工厂联合','弓长','日照中心','水落石出','半部春秋','半青半紫','半推半就','兄有债','四方来合作，贡献大一点','左十八，右十八','左有十八，右有十八，中间二四，全国统查','生日','打破砂锅问到底','古时候的月亮','禾苗着火','刘邦笑，刘备哭','池里无水，地里无土','上下合','木材行','千言万语','大米青菜一起吞','耳朵长在门里','自大一点','舌头上打青','朱元璋称帝','米粮满仓','没有木材','良家妇女','秀才遇到兵','告示贴出无人看','两人力大冲破天','大小头','半途而废','半新半旧','半真半假','半硬半软','半湿半干','半放红梅','半推半就','半吞半吐','半吃半拿','半文半白','半生半熟','半死半活','半信半疑','半明半暗','半梦半醒','半工半读','半农半医']
daan = [
'步','十','相','夕','引','九','士','者','出','思','尖','默','兵','豪','省','拿','田','化','闷','哭','袭','回','雷','明','闹','闪','输','素','息','伯','肉','夷','告','交','奈','佳','旨','吉','器','秋','花','鸠','旭','轨','立','一','言','力','仕','朝','克','目','顺','卡','田','天','雪','妙','岳','吻','吕','陌','梧','八','北','人','晦','二','明','必','抱','斌','昌','来','奈','肉','合','联','岁','胖','请','乞','生','谅','破','旷','全','闭','湖','转','画','春','原','赞','国','懒','选','念','扑','精','繁','迷','井','奈','名','告','王','料','脂','多','吠','肉','合','拿','夷','旨','吉','器','花','鸠','旭','轨','立','一','言','力','仕','朝','克','目','顺','卡','天','尘','出','左','张','申','泵','秦','素','扰','歌','器','林','森','星','瓦','胡','秋','翠','也','卡','材','够','精','闻','臭','适','明','囤','才','娘','斌','靠','夫','尖','余','昕','值','砍','汗','繁','扰','吕','拿','刘','孙','歹','誉','阳','寐','讲','伊']
print(f"谜面数量: {len(miyu)}, 答案数量: {len(daan)}")
if len(miyu) != len(daan):
    print("\n最后5组对照：")
    for i in range(min(5, len(miyu), len(daan))):
        print(f"倒数第{5 - i}组: 谜面：{miyu[-(5 - i)]} -> 答案：{daan[-(5 - i)]}")
else:
    print(f"字谜加载成功，共 {len(miyu)} 组。")
#=======================================================================================================================
current_options = ["", "", ""]
correct_pos = 0
current_x = 0
def qwq():
    global menu, HP, score, current_options, correct_pos, current_x
    if menu == "题":
        current_x = random.randint(0, len(miyu) - 1)
        correct_answer = daan[current_x]
        wrong_answers = []
        while len(wrong_answers) < 2:
            rand_idx = random.randint(0, len(daan) - 1)
            cand = daan[rand_idx]
            if cand != correct_answer and cand not in wrong_answers:
                wrong_answers.append(cand)
        correct_pos = random.randint(0, 2)
        options = ["", "", ""]
        options[correct_pos] = correct_answer
        fill_pos = 0
        for i in range(3):
            if options[i] == "":
                options[i] = wrong_answers[fill_pos]
                fill_pos += 1
        current_options = options
        menu = "答"
    elif menu == "错":
        global HP
        HP -= 1
        if HP > 0:
            menu = "题"
        else:
            menu = "end"
#=======================================================================================================================

def main():
    global menu, HP, score, shang, Yesscore, minzi
    clock = pygame.time.Clock()
    while True:
        window1.blit(bg, (-50, 0))

        if score % 32 == 0 and score != 0:
            if os.path.exists("奖励.bat"):
                os.system("奖励.bat")
            shang = True
            score += 1
            Yesscore += 1
        if shang:
            jiang = font.render(f"你获得过{Yesscore}个奖励！", True, (255, 0, 0))
            window1.blit(jiang, (300, 10))

        d_HP = font.render(f"命: {HP}", True, (255, 0, 0))
        window1.blit(d_HP, (200, 10))
        score_surface = font.render(f"Score: {score}", True, (0, 100, 50))
        window1.blit(score_surface, (10, 10))

        if menu == "答" and HP > 0:
            miyuxianshi = font.render(f"请听题: {miyu[current_x]}", True, (20, 70, 200))
            window1.blit(miyuxianshi, (50, 100))
            A_surf = font.render(f"A: {current_options[0]}", True, (10, 0, 180))
            B_surf = font.render(f"B: {current_options[1]}", True, (10, 0, 180))
            C_surf = font.render(f"C: {current_options[2]}", True, (10, 0, 180))
            window1.blit(A_surf, (180, 200))
            window1.blit(B_surf, (280, 200))
            window1.blit(C_surf, (380, 200))
        elif menu == "end":
            over_text = font.render(f"恭喜你：{minzi}", True, (255, 0, 0))
            window1.blit(over_text, (200, 300))
            over_text = font.render(f"游戏结束！最终得分: {score}", True, (255, 0, 0))
            window1.blit(over_text, (150, 400))
            exit_text = font.render("按 Q 键存档并退出", True, (200, 200, 200))
            window1.blit(exit_text, (270, 600))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if menu == "end" and event.type == KEYDOWN and event.key == K_q:
                if not kaifa:
                    try:
                        with open('saves.json', 'r', encoding='utf-8') as f:
                            save_data = json.load(f)
                    except (FileNotFoundError, json.JSONDecodeError):
                        save_data = {}
                    save = {score: minzi}
                    save_data.update(save)
                    with open('saves.json', 'w', encoding='utf-8') as f:
                        json.dump(save_data, f)
                pygame.quit()
                exit()
            if menu == "答" and HP > 0:
                if event.type == KEYDOWN:
                    choice = None
                    if event.key == K_a:
                        choice = 0
                    elif event.key == K_b:
                        choice = 1
                    elif event.key == K_c:
                        choice = 2
                    if choice is not None:
                        if choice == correct_pos:
                            score += 1
                            menu = "题"
                        else:
                            menu = "错"
        qwq()
        pygame.display.flip()
        clock.tick(60)
#=======================================================================================================================
if __name__ == "__main__":
    main()