import game
import random #載入產生隨機數的套件

# 建立角色
bg = game.create_sprite("bg.png") #創造角色
player = game.create_sprite("player.png") #創造角色
hint = game.create_sprite("hint.png") #創造角

vy = 0 #墜落速度
level = 0 #分數
initY = 450 #最新產生的障礙物位置
is_start = False #是否開始遊戲

# player.layer = 1
# hint.scale = 1.5

game.create_sound('bgm.ogg', True)

# 建立泡泡
bubbles = []
    
for i in range(30):
    b = game.create_sprite("bubble.png") #創造角色
    b.x = i * 30
    bubbles.append(b)
# 建立岩石(障礙物)
rocks = []
    
for i in range(17):
    r = game.create_sprite("b0.png","b1.png","b2.png","b3.png","b4.png","b5.png","b6.png","b7.png","b8.png","b9.png","b10.png") #創造角色
    r.x = i * 75
    rocks.append(r)
#遊戲主迴圈
def loop ():
    global level, initY, is_start, vy
    
    # 岩石往後移動
        
    for r in rocks:
        r.x -= 8
        if r.x < -30:
            r.x += 1275
            if is_start:
                level += 1
                initY += random.randint(-60,60)
            if initY < 300:
                initY = 300
            if initY > 600:
                initY = 600
            r.y = initY
            # 場景變化
            if level < 30:
                r.costume_id = 0
            elif level < 60:
                r.costume_id = 1
            elif level < 90:
                r.costume_id = 2
            elif level < 120:
                r.costume_id = 3
            elif level < 150:
                r.costume_id = 4
            elif level < 180:
                r.costume_id = 5
            elif level < 210:
                r.costume_id = 6
            elif level < 240:
                r.costume_id = 7
            elif level < 270:
                r.costume_id = 8
            elif level > 270:
                r.costume_id = 9

    # 潛艇控制(空白鍵按下)
    if key.space:
        vy -= 0.6
        is_start = True
    # 遊戲開始
    if is_start:
        vy += 0.3
        player.y += vy
        player.direction = 90 + vy * 5
        hint.hidden = True
    
    if player.touched(rocks):
        stop()
    
    # 泡泡
    for b in bubbles:
        b.x -= 7
        b.y -= 2
        b.scale = b.x / 600
        b.opacity = b.x / 600
        if b.x < -10:
            b.x = player.x - random.random() * 20 - 60
            b.y = player.y + random.random() * 20
    # 背景變化
    bg.x -= 0.3
    if bg.x < -1200:
        bg.x += 2400
    # 顯示Level
    drawText(level,10,10,"white",50)
game.forever(loop) #重複不斷執行遊戲迴圈

