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

class Puzzle:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.tiles = []
        cnt = 0
        for r in range(4):
            for c in range(4):
                self.tiles.append(Tile(r,c,cnt))
                cnt += 1
    
    def display(self):
        for t in self.tiles:
            t.display()
    
        r = mouseY//200
        c = mouseX//200
        stroke(0,255,0)
        noFill()
        rect(c*200, r*200, 200, 200)
    
    def clicked(self):
        r = mouseY//200
        c = mouseX//200
        
p = Puzzle(4,4)        

def setup():
    size(800,800)
    background(0)

def draw():
    background(0)
    p.display()

# def mouseClicked():
   
    
    
