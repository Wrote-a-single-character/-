import pygame, os
import random as r
from pygame.locals import *

pygame.init()
window1 = pygame.display.set_mode(size=(700, 800))
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.display.set_caption('文了个字 Made by MinecraftZXH')

# ================== 加载图片 ==================

W = pygame.image.load('img/无标题.png')
ccy = pygame.image.load('img/ico.png')
begin = pygame.image.load('img/BEGIN.png')
g1_1 = pygame.image.load('img/1-1.png')
g1_2 = pygame.image.load('img/1-2.png')
g1_3 = pygame.image.load('img/1-3.png')
g1_4 = pygame.image.load('img/1-4.png')
g1_5 = pygame.image.load("img/1-5.png")
g1_6 = pygame.image.load("img/1-6.png")
g1_7 = pygame.image.load("img/1-7.png")

qwq = pygame.image.load('img/？.png')
W1 = pygame.image.load('img/W1.png')
lose = pygame.image.load('img/lose.png')
bh1 = pygame.image.load('img/bh1.png')
bh2 = pygame.image.load('img/bh2.png')
bh3 = pygame.image.load('img/bh3.png')
bh4 = pygame.image.load('img/bh4.png')
bh5 = pygame.image.load('img/bh5.png')
bh6 = pygame.image.load('img/bh6.png')
bh7 = pygame.image.load('img/bh7.png')
caimi = pygame.image.load('img/字谜.png')
jgw = pygame.image.load('jgw/ico_64x64.png')
# ---------- 第一关资源（bh1） ----------
# 标点
ju = pygame.image.load('img/bh1/。.png')
wenq = pygame.image.load('img/bh1/？.png')
# 汉字双变体
dao1 = pygame.image.load('img/bh1/道1.png')
dao2 = pygame.image.load('img/bh1/道2.png')
ge1 = pygame.image.load('img/bh1/个1.png')
ge2 = pygame.image.load('img/bh1/个2.png')
ma1 = pygame.image.load('img/bh1/吗1.png')
ma2 = pygame.image.load('img/bh1/吗2.png')
men1 = pygame.image.load('img/bh1/们1.png')
men2 = pygame.image.load('img/bh1/们2.png')
ni1 = pygame.image.load('img/bh1/你1.png')
ni2 = pygame.image.load('img/bh1/你2.png')
qi1 = pygame.image.load('img/bh1/其1.png')
qi2 = pygame.image.load('img/bh1/其2.png')
shi1 = pygame.image.load('img/bh1/实1.png')
shi2 = pygame.image.load('img/bh1/实2.png')
shi01 = pygame.image.load('img/bh1/是1.png')
shi02 = pygame.image.load('img/bh1/是2.png')
wen01 = pygame.image.load('img/bh1/文1.png')
wen02 = pygame.image.load('img/bh1/文2.png')
xi1 = pygame.image.load('img/bh1/戏1.png')
xi2 = pygame.image.load('img/bh1/戏2.png')
you1 = pygame.image.load('img/bh1/游1.png')
you2 = pygame.image.load('img/bh1/游2.png')
zhe1 = pygame.image.load('img/bh1/这1.png')
zhe2 = pygame.image.load('img/bh1/这2.png')
zhi1 = pygame.image.load('img/bh1/知1.png')
zhi2 = pygame.image.load('img/bh1/知2.png')
zi1 = pygame.image.load('img/bh1/字1.png')
zi2 = pygame.image.load('img/bh1/字2.png')
# 完整字
dao = pygame.image.load('img/bh1/道.png')
ge = pygame.image.load('img/bh1/个.png')
ma = pygame.image.load('img/bh1/吗.png')
men = pygame.image.load('img/bh1/们.png')
ni = pygame.image.load('img/bh1/你.png')
qi = pygame.image.load('img/bh1/其.png')
shi = pygame.image.load('img/bh1/实.png')
shi0 = pygame.image.load('img/bh1/是.png')
wen0 = pygame.image.load('img/bh1/文.png')
xi = pygame.image.load('img/bh1/戏.png')
you = pygame.image.load('img/bh1/游.png')
zhe = pygame.image.load('img/bh1/这.png')
zhi = pygame.image.load('img/bh1/知.png')
zi = pygame.image.load('img/bh1/字.png')

# ---------- 第二关资源（bh2） ----------
# 标点
ju2 = pygame.image.load('img/bh2/。.png')       # 句号（本关不用，但保留）
# 汉字双变体
wen11 = pygame.image.load('img/bh2/文1.png')
wen12 = pygame.image.load('img/bh2/文2.png')
le1 = pygame.image.load('img/bh2/了1.png')
le2 = pygame.image.load('img/bh2/了2.png')
ge21 = pygame.image.load('img/bh2/个1.png')
ge22 = pygame.image.load('img/bh2/个2.png')
zi011 = pygame.image.load('img/bh2/字1.png')
zi012 = pygame.image.load('img/bh2/字2.png')
hai1 = pygame.image.load('img/bh2/还1.png')
hai2 = pygame.image.load('img/bh2/还2.png')
you011 = pygame.image.load('img/bh2/有1.png')
you012 = pygame.image.load('img/bh2/有2.png')
hen11 = pygame.image.load('img/bh2/很1.png')
hen12 = pygame.image.load('img/bh2/很2.png')
duo1 = pygame.image.load('img/bh2/多1.png')
duo2 = pygame.image.load('img/bh2/多2.png')
yan1 = pygame.image.load('img/bh2/衍1.png')
yan2 = pygame.image.load('img/bh2/衍2.png')
sheng1 = pygame.image.load('img/bh2/生1.png')
sheng2 = pygame.image.load('img/bh2/生2.png')
you02 = pygame.image.load('img/bh2/游1.png')    # 游1
you03 = pygame.image.load('img/bh2/游2.png')    # 游2
xi011 = pygame.image.load('img/bh2/戏1.png')
xi012 = pygame.image.load('img/bh2/戏2.png')
# 完整字
wen1 = pygame.image.load('img/bh2/文.png')
le = pygame.image.load('img/bh2/了.png')
ge = pygame.image.load('img/bh2/个.png')
zi01 = pygame.image.load('img/bh2/字.png')
hai = pygame.image.load('img/bh2/还.png')
you3 = pygame.image.load('img/bh2/有.png')
hen1 = pygame.image.load('img/bh2/很.png')
duo = pygame.image.load('img/bh2/多.png')
yan = pygame.image.load('img/bh2/衍.png')
sheng = pygame.image.load('img/bh2/生.png')
you4 = pygame.image.load('img/bh2/游.png')
xi01 = pygame.image.load('img/bh2/戏.png')

# ---------- 第三关资源（bh3） ----------
# 标点
# 汉字双变体
wan1 = pygame.image.load('img/bh3/玩1.png')
wan2 = pygame.image.load('img/bh3/玩2.png')
de1 = pygame.image.load('img/bh3/的1.png')
de2 = pygame.image.load('img/bh3/的2.png')
shi011 = pygame.image.load('img/bh3/时1.png')
shi011 = pygame.image.load('img/bh3/时2.png')
hou1 = pygame.image.load('img/bh3/候1.png')
hou2 = pygame.image.load('img/bh3/候2.png')
ke1 = pygame.image.load('img/bh3/可1.png')
ke2 = pygame.image.load('img/bh3/可2.png')
neng1 = pygame.image.load('img/bh3/能1.png')
neng2 = pygame.image.load('img/bh3/能2.png')
hui1 = pygame.image.load('img/bh3/会1.png')
hui2 = pygame.image.load('img/bh3/会2.png')
kan1 = pygame.image.load('img/bh3/看1.png')
kan2 = pygame.image.load('img/bh3/看2.png')
dao01 = pygame.image.load('img/bh3/到1.png')
dao02 = pygame.image.load('img/bh3/到2.png')
cai1 = pygame.image.load('img/bh3/彩1.png')
cai2 = pygame.image.load('img/bh3/彩2.png')
dan1 = pygame.image.load('img/bh3/蛋1.png')
dan2 = pygame.image.load('img/bh3/蛋2.png')
ti1 = pygame.image.load('img/bh3/提1.png')
ti2 = pygame.image.load('img/bh3/提2.png')
shi001 = pygame.image.load('img/bh3/示1.png')
shi002 = pygame.image.load('img/bh3/示2.png')
o1 = pygame.image.load('img/bh3/哦1.png')
o2 = pygame.image.load('img/bh3/哦2.png')
# 完整字
wan = pygame.image.load('img/bh3/玩.png')
de = pygame.image.load('img/bh3/的.png')
shi0 = pygame.image.load('img/bh3/时.png')
hou = pygame.image.load('img/bh3/候.png')
ke = pygame.image.load('img/bh3/可.png')
neng = pygame.image.load('img/bh3/能.png')
hui = pygame.image.load('img/bh3/会.png')
kan = pygame.image.load('img/bh3/看.png')
dao0 = pygame.image.load('img/bh3/到.png')
cai = pygame.image.load('img/bh3/彩.png')
dan = pygame.image.load('img/bh3/蛋.png')
ti = pygame.image.load('img/bh3/提.png')
shi00 = pygame.image.load('img/bh3/示.png')
o = pygame.image.load('img/bh3/哦.png')

# ---------- 第四关资源（bh4） ----------
# 标点
# 汉字双变体
zai1 = pygame.image.load('img/bh4/在1.png')
zai2 = pygame.image.load('img/bh4/在2.png')
zi01 = pygame.image.load('img/bh4/字1.png')
zi02 = pygame.image.load('img/bh4/字2.png')
mi1 = pygame.image.load('img/bh4/谜1.png')
mi2 = pygame.image.load('img/bh4/谜2.png')
you001 = pygame.image.load('img/bh4/游1.png')
you002 = pygame.image.load('img/bh4/游2.png')
xi01 = pygame.image.load('img/bh4/戏2.png')
xi02 = pygame.image.load('img/bh4/戏2.png')
zhong1 = pygame.image.load('img/bh4/中1.png')
zhong2 = pygame.image.load('img/bh4/中2.png')
shu1 = pygame.image.load('img/bh4/输1.png')
shu2 = pygame.image.load('img/bh4/输2.png')
ru1 = pygame.image.load('img/bh4/入1.png')
ru2 = pygame.image.load('img/bh4/入2.png')
zuo01 = pygame.image.load('img/bh4/作1.png')
zuo02 = pygame.image.load('img/bh4/作2.png')
zhe01 = pygame.image.load('img/bh4/者1.png')
zhe02 = pygame.image.load('img/bh4/者2.png')
cao1 = pygame.image.load('img/bh4/操1.png')
cao2 = pygame.image.load('img/bh4/操2.png')
zuo1 = pygame.image.load('img/bh4/作1.png')
zuo2 = pygame.image.load('img/bh4/作2.png')
xi001 = pygame.image.load('img/bh4/系1.png')
xi002 = pygame.image.load('img/bh4/系2.png')
tong1 = pygame.image.load('img/bh4/统1.png')
tong2 = pygame.image.load('img/bh4/统2.png')
ba1 = pygame.image.load('img/bh4/吧1.png')
ba2 = pygame.image.load('img/bh4/吧2.png')
# 完整字
zai = pygame.image.load('img/bh4/在.png')
zi0 = pygame.image.load('img/bh4/字.png')
mi = pygame.image.load('img/bh4/谜.png')
you000 = pygame.image.load('img/bh4/游.png')
xi0 = pygame.image.load('img/bh4/戏.png')
zhong = pygame.image.load('img/bh4/中.png')
shu = pygame.image.load('img/bh4/输.png')
ru = pygame.image.load('img/bh4/入.png')
zuo = pygame.image.load('img/bh4/作.png')
zhe0 = pygame.image.load('img/bh4/者.png')
cao = pygame.image.load('img/bh4/操.png')
zuo0 = pygame.image.load('img/bh4/作.png')
xi00 = pygame.image.load('img/bh4/系.png')
tong = pygame.image.load('img/bh4/统.png')
ba = pygame.image.load('img/bh4/吧.png')
# ---------- 第五关资源（bh5） ----------
# 标点
wenq5 = pygame.image.load('img/bh5/？.png')
# 汉字双变体
xiang1 = pygame.image.load('img/bh5/想1.png')
xiang2 = pygame.image.load('img/bh5/想2.png')
zhi1 = pygame.image.load('img/bh5/知1.png')
zhi2 = pygame.image.load('img/bh5/知2.png')
dao1 = pygame.image.load('img/bh5/道1.png')
dao2 = pygame.image.load('img/bh5/道2.png')
kai1 = pygame.image.load('img/bh5/开1.png')
kai2 = pygame.image.load('img/bh5/开2.png')
fa1 = pygame.image.load('img/bh5/发1.png')
fa2 = pygame.image.load('img/bh5/发2.png')
zhe5_1 = pygame.image.load('img/bh5/者1.png')
zhe5_2 = pygame.image.load('img/bh5/者2.png')
mo1 = pygame.image.load('img/bh5/模1.png')
mo2 = pygame.image.load('img/bh5/模2.png')
shi5_1 = pygame.image.load('img/bh5/式1.png')
shi5_2 = pygame.image.load('img/bh5/式2.png')
de5_1 = pygame.image.load('img/bh5/的1.png')
de5_2 = pygame.image.load('img/bh5/的2.png')
mi5_1 = pygame.image.load('img/bh5/密1.png')
mi5_2 = pygame.image.load('img/bh5/密2.png')
ma5_1 = pygame.image.load('img/bh5/码1.png')
ma5_2 = pygame.image.load('img/bh5/码2.png')
ma5_q = pygame.image.load('img/bh5/吗1.png')
ma5_q2 = pygame.image.load('img/bh5/吗2.png')
# 完整字
xiang = pygame.image.load('img/bh5/想.png')
zhi = pygame.image.load('img/bh5/知.png')
dao = pygame.image.load('img/bh5/道.png')
kai = pygame.image.load('img/bh5/开.png')
fa = pygame.image.load('img/bh5/发.png')
zhe5 = pygame.image.load('img/bh5/者.png')
mo = pygame.image.load('img/bh5/模.png')
shi5 = pygame.image.load('img/bh5/式.png')
de5 = pygame.image.load('img/bh5/的.png')
mi5 = pygame.image.load('img/bh5/密.png')
ma5 = pygame.image.load('img/bh5/码.png')
ma5_full = pygame.image.load('img/bh5/吗.png')
wenq5_full = pygame.image.load('img/bh5/？.png')

# ---------- 第六关资源（bh6） ----------
# 汉字双变体（请确保 img/bh6/ 下有对应图片）
kai1_6 = pygame.image.load('img/bh6/开1.png')
kai2_6 = pygame.image.load('img/bh6/开2.png')
fa1_6 = pygame.image.load('img/bh6/发1.png')
fa2_6 = pygame.image.load('img/bh6/发2.png')
zhe1_6 = pygame.image.load('img/bh6/者1.png')
zhe2_6 = pygame.image.load('img/bh6/者2.png')
mo1_6 = pygame.image.load('img/bh6/模1.png')
mo2_6 = pygame.image.load('img/bh6/模2.png')
shi1_6 = pygame.image.load('img/bh6/式1.png')
shi2_6 = pygame.image.load('img/bh6/式2.png')
de1_6 = pygame.image.load('img/bh6/的1.png')
de2_6 = pygame.image.load('img/bh6/的2.png')
mi1_6 = pygame.image.load('img/bh6/密1.png')
mi2_6 = pygame.image.load('img/bh6/密2.png')
ma1_6 = pygame.image.load('img/bh6/码1.png')
ma2_6 = pygame.image.load('img/bh6/码2.png')
yu1_6 = pygame.image.load('img/bh6/与1.png')
yu2_6 = pygame.image.load('img/bh6/与2.png')
you1_6 = pygame.image.load('img/bh6/有1.png')
you2_6 = pygame.image.load('img/bh6/有2.png')
guan1_6 = pygame.image.load('img/bh6/关1.png')
guan2_6 = pygame.image.load('img/bh6/关2.png')
o_full1_6 = pygame.image.load('img/bh6/哦1.png')
o_full2_6 = pygame.image.load('img/bh6/哦2.png')
# 完整字图片
kai_full_6 = pygame.image.load('img/bh6/开.png')
fa_full_6 = pygame.image.load('img/bh6/发.png')
zhe_full_6 = pygame.image.load('img/bh6/者.png')
mo_full_6 = pygame.image.load('img/bh6/模.png')
shi_full_6 = pygame.image.load('img/bh6/式.png')
de_full_6 = pygame.image.load('img/bh6/的.png')
mi_full_6 = pygame.image.load('img/bh6/密.png')
ma_full_6 = pygame.image.load('img/bh6/码.png')
yu_full_6 = pygame.image.load('img/bh6/与.png')
you_full_6 = pygame.image.load('img/bh6/有.png')
guan_full_6 = pygame.image.load('img/bh6/关.png')
o_full_6 = pygame.image.load('img/bh6/哦.png')
# 第五关数据（句子：想知道开发者模式的密码吗？）
# ================== 关卡数据定义 ==================
# 第一关数据
target_sentence_chars1_1 = ["你", "们", "知", "道", "吗", "？", "这", "其", "实", "是", "个", "文", "字", "游", "戏", "。"]
hanzi_list1_1 = ["你", "们", "知", "道", "吗", "这", "其", "实", "是", "个", "文", "字", "游", "戏"]
punct_list1_1 = ["？", "。"]
char_to_variants1_1 = {
    "你": {1: ni1, 2: ni2},
    "们": {1: men1, 2: men2},
    "知": {1: zhi1, 2: zhi2},
    "道": {1: dao1, 2: dao2},
    "吗": {1: ma1, 2: ma2},
    "这": {1: zhe1, 2: zhe2},
    "其": {1: qi1, 2: qi2},
    "实": {1: shi1, 2: shi2},
    "是": {1: shi01, 2: shi02},
    "个": {1: ge1, 2: ge2},
    "文": {1: wen01, 2: wen02},
    "字": {1: zi1, 2: zi2},
    "游": {1: you1, 2: you2},
    "戏": {1: xi1, 2: xi2},
    "？": {None: wenq},
    "。": {None: ju}
}
char_to_full1_1 = {
    "你": ni, "们": men, "知": zhi, "道": dao, "吗": ma,
    "这": zhe, "其": qi, "实": shi, "是": shi0, "个": ge,
    "文": wen0, "字": zi, "游": you, "戏": xi,
    "？": wenq, "。": ju
}

# 第二关数据（句子：文了个字还有很多衍生游戏）
target_sentence_chars1_2 = ["文", "了", "个", "字", "还", "有", "很", "多", "衍", "生", "游", "戏"]
hanzi_list1_2 = ["文", "了", "个", "字", "还", "有", "很", "多", "衍", "生", "游", "戏"]
punct_list1_2 = []   # 本关没有标点

char_to_variants1_2 = {
    "文": {1: wen11, 2: wen12},
    "了": {1: le1, 2: le2},
    "个": {1: ge21, 2: ge22},
    "字": {1: zi011, 2: zi012},
    "还": {1: hai1, 2: hai2},
    "有": {1: you011, 2: you012},
    "很": {1: hen11, 2: hen12},
    "多": {1: duo1, 2: duo2},
    "衍": {1: yan1, 2: yan2},
    "生": {1: sheng1, 2: sheng2},
    "游": {1: you02, 2: you03},
    "戏": {1: xi011, 2: xi012}
}
char_to_full1_2 = {
    "文": wen1,
    "了": le,
    "个": ge2,
    "字": zi01,
    "还": hai,
    "有": you3,
    "很": hen1,
    "多": duo,
    "衍": yan,
    "生": sheng,
    "游": you4,
    "戏": xi01
}
#第三关数据
target_sentence_chars1_3 = ['玩','的','时','候','可','能','会','看','到','彩','蛋','提','示','哦']
hanzi_list1_3 = ['玩','的','时','候','可','能','会','看','到','彩','蛋','提','示','哦']
punct_list1_3 = []   # 本关没有标点

char_to_variants1_3 = {
    '玩': {1: wan1, 2: wan2},
    "的": {1: de1, 2: de2},
    "时": {1: shi01, 2: shi02},
    "候": {1: hou1, 2: hou2},
    "可": {1: ke1, 2: ke2},
    "能": {1: neng1, 2: neng2},
    "会": {1: hui1, 2: hui2},
    "看": {1: kan1, 2: kan2},
    "到": {1: dao01, 2: dao02},
    "彩": {1: cai1, 2: cai2},
    "蛋": {1: dan1, 2: dan2},
    "提": {1: ti1, 2: ti2},
    "示": {1: shi1, 2: shi2},
    "哦": {1: o1, 2: o2}
}
char_to_full1_3 = {
    '玩': wan,
    "的": de,
    "时": shi0,
    "候": hou,
    "可": ke,
    "能": neng,
    "会": hui,
    "看": kan,
    "到": dao0,
    "彩": cai,
    "蛋": dan,
    "提": ti,
    "示": shi,
    "哦": o
}
#第四关数据
target_sentence_chars1_4 = ['在','字','谜','游','戏','中','输','入','作','者','操','作','系','统','吧']
hanzi_list1_4 = ['在','字','谜','游','戏','中','输','入','作','者','操','作','系','统','吧']
punct_list1_4 = []   # 本关没有标点

char_to_variants1_4 = {
    '在': {1: zai1, 2: zai2},
    "字": {1: zi01, 2: zi02},
    "谜": {1: mi1, 2: mi2},
    "游": {1: you1, 2: you2},
    "戏": {1: xi01, 2: xi02},
    "中": {1: zhong1, 2: zhong2},
    "输": {1: shu1, 2: shu2},
    "入": {1: ru1, 2: ru2},
    "作": {1: zuo01, 2: zuo02},
    "者": {1: zhe1, 2: zhe2},
    "操": {1: cao1, 2: cao2},
    "作": {1: zuo1, 2: zuo2},
    "系": {1: xi001, 2: xi002},
    "统": {1: tong1, 2: tong2},
    "吧": {1: ba1, 2:ba2}
}
char_to_full1_4 = {
    '在': zai,
    "字": zi0,
    "谜": mi,
    "游": you,
    "戏": xi0,
    "中": zhong,
    "输": shu,
    "入": ru,
    "作": zuo0,
    "者": zhe,
    "操": cao,
    "作": zuo,
    "系": xi00,
    "统": tong,
    "吧": ba
}
target_sentence_chars1_5 = ["想", "知", "道", "开", "发", "者", "模", "式", "的", "密", "码", "吗", "？"]
hanzi_list1_5 = ["想", "知", "道", "开", "发", "者", "模", "式", "的", "密", "码", "吗"]
punct_list1_5 = ["？"]

char_to_variants1_5 = {
    "想": {1: xiang1, 2: xiang2},
    "知": {1: zhi1, 2: zhi2},
    "道": {1: dao1, 2: dao2},
    "开": {1: kai1, 2: kai2},
    "发": {1: fa1, 2: fa2},
    "者": {1: zhe5_1, 2: zhe5_2},
    "模": {1: mo1, 2: mo2},
    "式": {1: shi5_1, 2: shi5_2},
    "的": {1: de5_1, 2: de5_2},
    "密": {1: mi5_1, 2: mi5_2},
    "码": {1: ma5_1, 2: ma5_2},
    "吗": {1: ma5_q, 2: ma5_q2},
    "？": {None: wenq5}
}
char_to_full1_5 = {
    "想": xiang,
    "知": zhi,
    "道": dao,
    "开": kai,
    "发": fa,
    "者": zhe5,
    "模": mo,
    "式": shi5,
    "的": de5,
    "密": mi5,
    "码": ma5,
    "吗": ma5_full,
    "？": wenq5_full
}
# 第六关数据
target_sentence_chars1_6 = ["开", "发", "者", "模", "式", "的", "密", "码", "与", "开", "发", "者", "有", "关"]
hanzi_list1_6 = ["开", "发", "者", "模", "式", "的", "密", "码", "与", "开", "发", "者", "有", "关"]
punct_list1_6 = []   # 无标点

char_to_variants1_6 = {
    "开": {1: kai1_6, 2: kai2_6},
    "发": {1: fa1_6, 2: fa2_6},
    "者": {1: zhe1_6, 2: zhe2_6},
    "模": {1: mo1_6, 2: mo2_6},
    "式": {1: shi1_6, 2: shi2_6},
    "的": {1: de1_6, 2: de2_6},
    "密": {1: mi1_6, 2: mi2_6},
    "码": {1: ma1_6, 2: ma2_6},
    "与": {1: yu1_6, 2: yu2_6},
    "有": {1: you1_6, 2: you2_6},
    "关": {1: guan1_6, 2: guan2_6,
    "哦": {1: o_full1_6}, 2: o_full2_6},
}
char_to_full1_6 = {
    "开": kai_full_6,
    "发": fa_full_6,
    "者": zhe_full_6,
    "模": mo_full_6,
    "式": shi_full_6,
    "的": de_full_6,
    "密": mi_full_6,
    "码": ma_full_6,
    "与": yu_full_6,
    "有": you_full_6,
    "关": guan_full_6,
    "哦": o_full_6
}
# 当前关卡数据（动态切换）
current_target_sentence = target_sentence_chars1_1
current_hanzi_list = hanzi_list1_1
current_punct_list = punct_list1_1
current_char_to_variants = char_to_variants1_1
current_char_to_full = char_to_full1_1
current_level = 1

# 游戏状态
game_state = 'menu'          # 'menu', 'select', 'play', 'lose'
blocks = []
BLOCK_SIZE = 50
basket = [None, None, None]
sentence_progress = []

# 背景和音乐相关
current_bg = W
current_bgm = None

# 计时相关
start_ticks = 0
time_left = 120

# ================== 工具函数 ==================
def generate_blocks():
    global blocks
    blocks = []
    parts = []
    for ch in current_hanzi_list:
        parts.append((ch, 1))
        parts.append((ch, 2))
    for p in current_punct_list:
        parts.append((p, None))
    all_possible = []
    for ch in current_hanzi_list:
        all_possible.append((ch, 1))
        all_possible.append((ch, 2))
    for p in current_punct_list:
        all_possible.append((p, None))
    # 计算还需要补充多少个部件以达到36个（6x6）
    need = 36 - len(parts)
    if need > 0:
        extra = r.choices(all_possible, k=need)
        parts.extend(extra)
    r.shuffle(parts)

    start_x, start_y = 200, 200
    idx = 0
    for row in range(6):
        for col in range(6):
            x = start_x + col * BLOCK_SIZE
            y = start_y + row * BLOCK_SIZE
            ch, var = parts[idx]
            img = current_char_to_variants[ch][var] if var is not None else current_char_to_variants[ch][None]
            blocks.append([x, y, True, ch, var, img])
            idx += 1

def add_to_sentence_by_order(char, img):
    for idx, needed in enumerate(current_target_sentence):
        if sentence_progress[idx] is None:
            if needed == char:
                sentence_progress[idx] = img
                return True
            else:
                return False
    return False

def check_combination():
    global basket
    changed = True
    while changed:
        changed = False
        for i in range(3):
            if basket[i] is None:
                continue
            ch, var, img = basket[i]
            if var is None:   # 标点
                if add_to_sentence_by_order(ch, img):
                    basket[i] = None
                    changed = True
                    break
                else:
                    continue
            for j in range(i+1, 3):
                if basket[j] is None:
                    continue
                ch2, var2, img2 = basket[j]
                if ch2 is None:
                    continue
                if ch == ch2 and var != var2:
                    full_img = current_char_to_full[ch]
                    if add_to_sentence_by_order(ch, full_img):
                        basket[i] = None
                        basket[j] = None
                        changed = True
                        break
            if changed:
                break

def reset_game(level):
    global game_state, current_bg, current_bgm, start_ticks, time_left
    global current_target_sentence, current_hanzi_list, current_punct_list
    global current_char_to_variants, current_char_to_full, current_level
    global blocks, basket, sentence_progress

    # 根据关卡设置数据
    if level == 1:
        current_target_sentence = target_sentence_chars1_1
        current_hanzi_list = hanzi_list1_1
        current_punct_list = punct_list1_1
        current_char_to_variants = char_to_variants1_1
        current_char_to_full = char_to_full1_1
        current_bg = bh1
        current_level = 1
    elif level == 2:
        current_target_sentence = target_sentence_chars1_2
        current_hanzi_list = hanzi_list1_2
        current_punct_list = punct_list1_2
        current_char_to_variants = char_to_variants1_2
        current_char_to_full = char_to_full1_2
        current_bg = bh2
        current_level = 2
    elif level == 3:
        current_target_sentence = target_sentence_chars1_3
        current_hanzi_list = hanzi_list1_3
        current_punct_list = punct_list1_3
        current_char_to_variants = char_to_variants1_3
        current_char_to_full = char_to_full1_3
        current_bg = bh3
        current_level = 3
    elif level == 4:
        current_target_sentence = target_sentence_chars1_4
        current_hanzi_list = hanzi_list1_4
        current_punct_list = punct_list1_4
        current_char_to_variants = char_to_variants1_4
        current_char_to_full = char_to_full1_4
        current_bg = bh4
        current_level = 4
    elif level == 5:
        current_target_sentence = target_sentence_chars1_5
        current_hanzi_list = hanzi_list1_5
        current_punct_list = punct_list1_5
        current_char_to_variants = char_to_variants1_5
        current_char_to_full = char_to_full1_5
        current_bg = bh5
        current_level = 5
    elif level == 6:
        current_target_sentence = target_sentence_chars1_6
        current_hanzi_list = hanzi_list1_6
        current_punct_list = punct_list1_6
        current_char_to_variants = char_to_variants1_6
        current_char_to_full = char_to_full1_6
        current_bg = bh6
        current_level = 6
    elif level == 7:
        current_target_sentence = target_sentence_chars1_4
        current_hanzi_list = hanzi_list1_4
        current_punct_list = punct_list1_4
        current_char_to_variants = char_to_variants1_4
        current_char_to_full = char_to_full1_4
        current_bg = bh6
        current_level = 7

    generate_blocks()
    basket = [None, None, None]
    sentence_progress = [None] * len(current_target_sentence)

    # 背景音乐
    current_bgm = 'music/msc.mp3'
    if current_bgm:
        pygame.mixer.music.load(current_bgm)
        pygame.mixer.music.play(-1)

    game_state = 'play'
    start_ticks = pygame.time.get_ticks()
    time_left = 120

def stop_music():
    pygame.mixer.music.stop()

# ================== EVENT处理 ==================
def Event():
    global game_state, current_bg
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            if game_state == 'menu':
                begin_rect = begin.get_rect(topleft=(225, 650))
                if begin_rect.collidepoint(x, y):
                    game_state = 'select'
                    current_bg = W
                    print("进入选择界面")
                ccy_rect = ccy.get_rect(topleft=(0, 228))
                if ccy_rect.collidepoint(x, y):
                    os.system("ccy.bat")
                    quit()
                caimi_rect = caimi.get_rect(topleft=(0, 165))
                if caimi_rect.collidepoint(x, y):
                    os.system("zimi.bat")
                    quit()
                jgw_rect = jgw.get_rect(topleft=(0, 292))
                if jgw_rect.collidepoint(x, y):
                    os.system("jgw.bat")
                    quit()
            elif game_state == 'select':
                g1_1_rect = g1_1.get_rect(topleft=(20, 100))
                if g1_1_rect.collidepoint(x, y):
                    reset_game(1)
                    print("进入游戏 - 关卡1")
                g1_2_rect = g1_2.get_rect(topleft=(120, 100))
                if g1_2_rect.collidepoint(x, y):
                    reset_game(2)
                    print("进入游戏 - 关卡2")
                g1_3_rect = g1_3.get_rect(topleft=(220, 100))
                if g1_3_rect.collidepoint(x, y):
                    reset_game(3)
                    print("进入游戏 - 关卡3")
                g1_4_rect = g1_4.get_rect(topleft=(320, 100))
                if g1_4_rect.collidepoint(x, y):
                    reset_game(4)
                    print("进入游戏 - 关卡4")
                g1_5_rect = g1_5.get_rect(topleft=(420, 100))
                if g1_5_rect.collidepoint(x, y):
                    reset_game(5)
                    print("进入游戏 - 关卡5")
                g1_6_rect = g1_6.get_rect(topleft=(520, 100))
                if g1_6_rect.collidepoint(x, y):
                    reset_game(6)
                    print("进入游戏 - 关卡6")
                g1_7_rect = g1_7.get_rect(topleft=(620, 100))
                if g1_7_rect.collidepoint(x, y):
                    reset_game(7)
                    print("进入游戏 - 关卡7")


            elif game_state == 'play':
                for block in blocks:
                    if block[2]:
                        rect = pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
                        if rect.collidepoint(x, y):
                            for i in range(3):
                                if basket[i] is None:
                                    basket[i] = (block[3], block[4], block[5])
                                    block[2] = False
                                    print(f"放入篮子槽{i}: {block[3]}{block[4]}")
                                    break
                            else:
                                print("篮子已满，游戏失败")
                                game_state = 'lose'
                                stop_music()
                                return
                            check_combination()
                            break
            elif game_state == 'lose':
                game_state = 'menu'
                current_bg = W

# ================== 主循环 ==================
while True:
    Event()
    window1.blit(current_bg, (-60, 0))

    if game_state == 'menu':
        window1.blit(begin, (225, 650))
        window1.blit(qwq, (0, 100))
        window1.blit(caimi, (0, 164))
        window1.blit(ccy, (0, 228))
        window1.blit(jgw, (0, 292))

    elif game_state == 'select':
        window1.blit(g1_1, (20 ,  100))
        window1.blit(g1_2, (120, 100))
        window1.blit(g1_3, (220, 100))
        window1.blit(g1_4, (320, 100))
        window1.blit(g1_5, (420, 100))
        window1.blit(g1_6, (520, 100))
        window1.blit(g1_7, (620, 100))

    elif game_state == 'play':
        elapsed = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = max(0, 120 - elapsed)
        if time_left <= 0:
            game_state = 'lose'
            stop_music()
            continue

        # 绘制方块
        for block in blocks:
            if block[2]:
                window1.blit(W1, (block[0], block[1]))
                img = block[5]
                rect = img.get_rect(center=(block[0] + BLOCK_SIZE//2, block[1] + BLOCK_SIZE//2))
                window1.blit(img, rect)

        # 绘制句子区域
        start_x, start_y = 50, 20
        for idx, img in enumerate(sentence_progress):
            if img is not None:
                window1.blit(img, (start_x + idx * 40, start_y))

        # 绘制篮子
        basket_x, basket_y = 250, 700
        for i in range(3):
            pygame.draw.rect(window1, (200, 200, 200), (basket_x + i*60, basket_y, 50, 50), 2)
            if basket[i] is not None:
                window1.blit(basket[i][2], (basket_x + i*60, basket_y))

        # 绘制倒计时文本
        font = pygame.font.Font(None, 36)
        minutes = int(time_left) // 60
        seconds = int(time_left) % 60
        #显示时间
        
        timer_surf = font.render(f"{minutes:02d}:{seconds:02d}", True, (0, 0, 0))
        window1.blit(timer_surf, (580, 20))

        # 胜利检测
        if all(img is not None for img in sentence_progress):
            font_big = pygame.font.Font(None, 74)
            win_text = font_big.render("胜利!", True, (255, 0, 0))
            window1.blit(win_text, (250, 400))
            game_state = 'menu'
            current_bg = W
            stop_music()
            os.system('cls')

    elif game_state == 'lose':
        window1.blit(lose, (-60, 0))
        font = pygame.font.Font(None, 36)
        tip = font.render("点击任意位置返回主菜单", True, (255, 255, 255))
        window1.blit(tip, (200, 700))
        os.system('cls')
    pygame.display.update()
    clock.tick(60)