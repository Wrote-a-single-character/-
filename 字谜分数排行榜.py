import json, os, sys
from pygame.locals import *
def draw_ranking(screen, top10, font):
    screen.fill((0, 0, 0))  # 黑背景
    title = font.render("TOP 10 SCORES", True, (255, 255, 0))
    screen.blit(title, (200, 50))
    y = 120
    for idx, (score, name) in enumerate(top10, start=1):
        line = f"{idx}. {name}  {score}"
        surf = font.render(line, True, (255, 255, 255))
        screen.blit(surf, (150, y))
        y += 40
    
    pygame.display.flip()
    # 等待按任意键返回
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                return
def get_top10_from_scores(data):
    """
    从 {score_str: name} 格式的字典中提取前10名
    返回 [(score, name), ...] 列表，按分数降序
    """
    # 将字符串键转换为整数，并组成 (分数, 名字) 列表
    items = [(int(k), v) for k, v in data.items()]
    # 按分数降序排序
    items.sort(key=lambda x: x[0], reverse=True)
    return items[:10]   # 最多前10名

def print_ranking(top10):
    """打印排行榜表格"""
    print("\n" + "="*35)
    print("        🏆 高分榜 TOP 10 🏆")
    print("="*35)
    print(f"{'排名':<6} {'玩家名':<12} {'分数':>8}")
    print("-"*35)
    for idx, (score, name) in enumerate(top10, start=1):
        print(f"{idx:<6} {name:<12} {score:>8}")
    print("="*35)

# 读取数据（建议只读取一次，不要放在主循环里）
try:
    with open("saves.json", "r", encoding="utf-8") as f:
        save_dt = json.load(f)
        print("原始数据:", save_dt)
        
        # 生成排行榜
        top10 = get_top10_from_scores(save_dt)
        print_ranking(top10)
        
except FileNotFoundError:
    print("saves.json 文件不存在，请先创建")
    top10 = []
except Exception as e:
    print("读取出错:", e)
    top10 = []

# 你的 Pygame 主循环
while True:
    pass