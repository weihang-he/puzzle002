import os
path = os.getcwd() + "/"

class Tile:
    def __init__(self,r,c,v):
        self.r = r
        self.c = c
        self.v = v
        self.img = loadImage(path + "images/" + str(self.v)+".png")

    def display(self):
        image(self.img, self.c * 200, self.r * 200)
        
def setup():
    size(800,800)
    background(0)

t0 = Tile(0,0,0)
t1 = Tile(0,1,1)

def draw():
    t0.display()
    t1.display()
    
