import game
import random

class pictor:
    celebrity = game.create_sprite("戈登拉姆齊.jpg")
    celebrity.x = 400
    celebrity.y = 500
    sentence = []
    index = 0
    
pict = pictor()
pict.sentence = ["我就爛~~","曾子睿","","124"]
pict.index = random.randint(0,len(pict.sentence)-1)

def loop():
    # 顯示文字
    drawText(pict.sentence[pict.index],10,10,"black",80)
def rand():
    # 產生隨機數
    pict.index = random.randint(0,len(pict.sentence)-1)
    
# enter按下偵測
game.on("keydown","enter", rand)
game.forever(loop)
