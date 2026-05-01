import pygame
import sys
import ctypes
import os
import json
import random
import string

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ================== 随机验证码系统 ==================
def generate_random_code(length=10):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def save_code(code):
    with open("code.json", "w", encoding="utf-8") as f:
        json.dump({"code": code}, f, indent=2)

def load_code():
    if not os.path.exists("code.json"):
        return None
    with open("code.json", "r", encoding="utf-8") as f:
        return json.load(f).get("code")
# ======================================================

# ================== 初始化 ==================
pygame.display.set_caption('猜甲骨文 Made by LMF')
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("WZ-甲骨文模式 v-1.0")
clock = pygame.time.Clock()

font_big = pygame.font.Font("jgw/ttf/microsoft black.ttf", 70)
font_small = pygame.font.Font("jgw/ttf/microsoft black.ttf", 20)

name = input("来者何人！敢来挑战我一命速通！")
dev_mode = False
bg = None

if name == "LMF":
    print("===== welcom to Dev_LMF =====")
    cmd = input("Please enter command：")
    
    if cmd == "Dism /install pygame":
        print("✅ command start：正在启动小游戏...")

        try:
            os.startfile("test.py")
        except:
            pass
        pygame.quit()
        sys.exit()
    elif cmd == "Dism \\QWQ":
        print("✅ command start：已触发 Windows11 彩蛋壁纸！")
        bg = pygame.image.load('jgw/Tt/install.jpg').convert()
        bg = pygame.transform.scale(bg, (800, 600))
        try:
            os.startfile(r"jgw/Tt\install.jpg")
        except:
            pass
    else:
        print("command error")
elif name in ["SB", "9178", "2b","7891","78","91","傻逼","sb"]:
    ctypes.windll.user32.MessageBoxW(None,"请勿输入不干净词汇！","警告",0)
    pygame.quit()
    sys.exit()
else:
    print(f"好哇，{name}，你的胆量不小啊")

# ================== 加载背景 ==================
try:
    images = [
        {
            "img": pygame.image.load("jgw/Tt/虎.jpeg").convert_alpha(),
            "answer": "虎",
            "options": ["A.龙", "B.虎", "C.山", "D.舞"]
        },
        {
            "img": pygame.image.load("jgw/Tt/龙.jpeg").convert_alpha(),
            "answer": "龙",
            "options": ["A.高", "B.中", "C.舞", "D.龙"]
        },
        {
            "img": pygame.image.load("jgw/Tt/高.jpeg").convert_alpha(),
            "answer": "高",
            "options": ["A.山", "B.高", "C.中", "D.虎"]
        },
        {
            "img": pygame.image.load("jgw/Tt/舞.jpeg").convert_alpha(),
            "answer": "舞",
            "options": ["A.龙", "B.山", "C.舞", "D.中"]
        },
        {
            "img": pygame.image.load("jgw/Tt/山.jpeg").convert_alpha(),
            "answer": "山",
            "options": ["A.虎", "B.龙", "C.山", "D.高"]
        },
        {
            "img": pygame.image.load("jgw/Tt/中.jpeg").convert_alpha(),
            "answer": "中",
            "options": ["A.舞", "B.高", "C.中", "D.龙"]
        },
        {
            "img": pygame.image.load("jgw/Tt/力.webp").convert_alpha(),
            "answer": "力",
            "options": ["A.功", "B.力", "C.男", "D.动"]
        },
        {
            "img": pygame.image.load("jgw/Tt/木.jpg").convert_alpha(),
            "answer": "木",
            "options": ["A.林", "B.森", "C.木", "D.禾"]
        },
        {
            "img": pygame.image.load("jgw/Tt/罪.jpg").convert_alpha(),
            "answer": "罪",
            "options": ["A.网", "B.罪", "C.非", "D.罚"]
        },
        {
            "img": pygame.image.load("jgw/Tt/屋.webp").convert_alpha(),
            "answer": "宀",
            "options": ["A.宀", "B.入", "C.山", "D.人"]
        },
        {
            "img": pygame.image.load("jgw/Tt/吴.jpg").convert_alpha(),
            "answer": "吴",
            "options": ["A.天", "B.口", "C.吴", "D.夫"]
        },
        {
            "img": pygame.image.load("jgw/Tt/鱼.webp").convert_alpha(),
            "answer": "鱼",
            "options": ["A.鸟", "B.贝", "C.虫", "D.鱼"]
        },
        {
            "img": pygame.image.load("jgw/Tt/元旦.png").convert_alpha(),
            "answer": "元旦",
            "options": ["A.元宵", "B.清明", "C.元旦", "D.中秋"]
        },
        {
            "img": pygame.image.load("jgw/Tt/水.png").convert_alpha(),
            "answer": "水",
            "options": ["A.火", "B.木", "C.水", "D.山"]
        },
        {
            "img": pygame.image.load("jgw/Tt/汤.png").convert_alpha(),
            "answer": "汤",
            "options": ["A.水", "B.阳", "C.温", "D.汤"]
        },
        {
            "img": pygame.image.load("jgw/Tt/天.png").convert_alpha(),
            "answer":"天",
            "options": ["A.人", "B.大", "C.我", "D.天"]
        },
        {
            "img": pygame.image.load("jgw/Tt/鹿.jpg").convert_alpha(),
            "answer":"鹿",
            "options": ["A.鹿", "B.虎", "C.马", "D.牛"]
        },
        {
            "img":pygame.image.load("jgw/Tt/林.webp").convert_alpha(),
            "answer":"林",
            "options": ["A.木", "B.森", "C.林", "D.树"]
        },
        {
            "img":pygame.image.load("jgw/Tt/马.webp").convert_alpha(),
            "answer":"马",
            "options": ["A.马", "B.冯", "C.猪", "D.牛"]
        },
        {
            "img":pygame.image.load("jgw/Tt/犬.webp").convert_alpha(),
            "answer":"犬",
            "options": ["A.猪", "B.羊", "C.狗", "D.犬"]
        },
        {
            "img":pygame.image.load("jgw/Tt/牛.jpeg").convert_alpha(),
            "answer":"牛",
            "options": ["A.羊", "B.牛", "C.卷", "D.角"]
        },
        {
            "img":pygame.image.load("jgw/Tt/羊.jpeg").convert_alpha(),
            "answer":"羊",
            "options": ["A.羊", "B.基", "C.斯", "D.流"]
        }
    ]

    for item in images:
        item["img"] = pygame.transform.scale(item["img"], (300, 300))

    if bg is None:
        bg = pygame.image.load("jgw/Tt/bj.png").convert()

except Exception as e:
    print("⚠️ 图片找不到！错误：", e)
    pygame.quit()
    sys.exit()

# ================== 音乐 ==================
try:
    pygame.mixer.music.load("jgw/music/LMF.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except:
    print("🎵 音乐未找到")

# ================== 游戏主循环 ==================
current_index = 0
msg = ""
msg_time = 0

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()

    if msg and current_time - msg_time > 2000:
        msg = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_index >= len(images):
                continue
            
            current_item = images[current_index]
            option_rects = []
            y = 400
            for _ in current_item["options"]:
                rect = pygame.Rect(200, y, 300, 35)
                option_rects.append(rect)
                y += 40

            for i, rect in enumerate(option_rects):
                if rect.collidepoint(mouse_pos):
                    selected_option = current_item["options"][i]
                    selected_answer = selected_option.split(".")[1]
                    if selected_answer == current_item["answer"]:
                        msg = "答对啦！下一题"
                        msg_time = current_time
                        current_index += 1
                        if current_index >= len(images):
                            msg = "全部通关！游戏结束"
                            random_code = generate_random_code()
                            save_code(random_code)
                            ctypes.windll.user32.MessageBoxW(None,f"🎉 恭喜通关！\n本次随机验证码：{random_code}\n\nLMF","恭喜通关",0)
                            pygame.quit()
                            sys.exit()
                    else:
                        ctypes.windll.user32.MessageBoxW(None,"错了？受着！是一命速通！LFG","人机",0)
                        pygame.quit()
                        sys.exit()

    if current_index < len(images):
        current_item = images[current_index]
        img_rect = current_item["img"].get_rect(center=(400, 250))
        screen.blit(current_item["img"], img_rect)

        y = 400
        for option in current_item["options"]:
            rect = pygame.Rect(200, y, 300, 35)
            pygame.draw.rect(screen, (50, 50, 50), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            text = font_small.render(option, True, (255,255,255))
            screen.blit(text, (210, y + 5))
            y += 40

    if msg:
        msg_surf = font_big.render(msg, True, (0,255,0))
        screen.blit(msg_surf, (200, 500))

    pygame.display.flip()