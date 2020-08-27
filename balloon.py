import game
import random
import time

bg_1 = game.create_sprite('bg_1.png')
bg_2 = createSprite('bg_2.png')
# 建立準星
target = game.create_sprite("target.png") 
reward = game.create_sprite('r0.png','r1.png','r2.png','r3.png','r4.png','r5.png','r6.png','r7.png','r8.png','r9.png','r10.png')
number = game.create_sprite('n0.png','n1.png','n2.png','n3.png','n4.png','n5.png')
game.create_sound('bgm.mp3')

number.opacity = 0.7
bg_1.layer = 1
number.layer = 2
target.layer = 3
reward.layer = 4
reward.hidden = True
number.hidden = True

clock = 0
scores = 0
balloons = []
end_time = time.time() + 15

def loop ():
    global clock, scores, ballons,end_time
    
    # 準星跟著滑鼠
    target.move_to(cursor.x,cursor.y)
    # 建立氣球
    clock += 1
    if clock % 10 == 0:
        b = game.create_sprite("a.png","b.png","c.png","d.png","e.png","g.png","f.png") #創造角色
        b.costume_id = random.randint(0,6)
        b.y = 1000
        b.x = random.random() * 1000 + 100
        balloons.append(b)
        
    # 氣球上升
    for b in balloons:
        if b.costume_id == 0:
            b.y -= 3
        if b.costume_id == 1:
            b.y -= 5
        if b.costume_id == 2:
            b.y -= 7
        if b.costume_id == 3:
            b.y -= 8
        if b.costume_id == 4:
            b.y -= 8
        if b.costume_id == 5:
            b.y -= 7
        if b.costume_id == 6:
            b.y -= 6
        # 射擊及計分
        if cursor.is_down and b.touched(cursor):
            if b.costume_id == 0:
                scores += 1 
            if b.costume_id == 1:
                scores += 10 
            if b.costume_id == 2:
                scores += 5 
            if b.costume_id == 3:
                scores *= 2 
            if b.costume_id == 4:
                scores /= 2 
            if b.costume_id == 5:
                end_time += 3
            if b.costume_id == 6:
                end_time = time.time()
            b.destroy()
            sound.play('shot.mp3')
    drawText(scores,60,20,"white",20)
    # 時間倒數
    t = end_time - time.time()
    print(t)
    if t <= 5:
        number.hidden = False
    if t <= 0:
        number.costume_id = 0
    elif t <= 1:
        number.costume_id = 1
    elif t <= 2:
        number.costume_id = 2
    elif t <= 3:
        number.costume_id = 3
    elif t <= 4:
        number.costume_id = 4
    elif t <= 5:
        number.costume_id = 5
    # 遊玩結果
    if t < -1:
        number.hidden = True
        if scores > 10000000000:
            reward.costume_id = 0
        elif scores > 1000000000:
            reward.costume_id = 1
        elif scores > 100000000:
            reward.costume_id = 2
        elif scores > 10000000:
            reward.costume_id = 3
        elif scores > 1000000:
            reward.costume_id = 4
        elif scores > 100000:
            reward.costume_id = 5
        elif scores > 10000:
            reward.costume_id = 6
        elif scores > 1000:
            reward.costume_id = 7
        elif scores > 100:
            reward.costume_id = 8
        elif scores > 10:
            reward.costume_id = 9
        elif scores > 0:
            reward.costume_id = 10
        reward.hidden = False
        stop()
    
    
game.forever(loop)