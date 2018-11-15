import os
path = os.getcwd() + "/"

class Tile:
    def __init__(self,r,c,v):
        self.r = r
        self.c = c
        self.v = v
        self.img = loadImage(path + "images/" + str(self.v)+".png")

    def display(self):
        if self.v != 15:
            image(self.img, self.c * 200, self.r * 200)
            noFill()
            stroke(0)
            strokeWeight(5)
            rect(self.c * 200, self.r * 200, 200, 200)
        
        
        
def setup():
    size(800,800)
    background(0)

tiles = []
cnt = 0
for r in range(4):
    for c in range(4):
        tiles.append(Tile(r,c,cnt))
        cnt += 1
        
def draw():
    for t in tiles:
        t.display()
    
    
    
