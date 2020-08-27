import game
import random

class pictor:
    celebrity = game.create_sprite("戈登拉姆齊.jpg")
    celebrity.x = 400
    celebrity.y = 500
    sentence = []
    index = 0
    
pict = pictor()
pict.sentence = ["aa","bb","ccc","dd"]
pict.index = random.randint(0,len(pict.sentence)-1)
pict.celebrity.hidden = True

pict2 = pictor()
pict2.celebrity = game.create_sprite("愛因斯坦.jpg") #創造角色
pict2.sentence = ["1342","3456","456","124"]
pict2.index = random.randint(0,len(pict.sentence)-1)
def loop():
    # 顯示文字
    drawText(pict2.sentence[pict2.index],10,10,"black",80)
def rand():
    # 產生隨機數
    pict2.index = random.randint(0,len(pict2.sentence)-1)
    
# enter按下偵測
game.on("keydown","enter", rand)
game.forever(loop)
