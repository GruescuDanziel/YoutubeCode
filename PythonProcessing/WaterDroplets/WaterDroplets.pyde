from dropClass import Drop

drops = [Drop(250,250)]

def setup():
    size(500, 500)
    
def mouseClicked():
    global drops
    drops.append(Drop(mouseX,mouseY))    

def draw():
    global drops
    background(0)
    stroke(255)
    noFill()
    strokeWeight(1)
    for drop in drops:
        drop.drawCircle()
