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
        t = self.getTile(r,c)
        for n in [[-1,0], [1,0], [0,-1], [0,1]]:
            nT = self.getTile(r+n[0], c+n[1])
            if nT != False and nT.v == 15:
                self.swapTiles(t, nT)
        
        
    def getTile(self,r,c):
        for t in self.tiles:
            if t.r == r and t.c == c:
                return t
        return False
           
    def swapTiles(self,t1, t2):
        tmp1 = t1.v
        tmp2 = t1.img
        t1.v = t2.v
        t1.img = t2.img
        t2.v = tmp1
        t2.img = tmp2
        
          
                        
p = Puzzle(4,4)        

def setup():
    size(800,800)
    background(0)

def draw():
    background(0)
    p.display()

def mouseClicked():
    p.clicked()
   
    
    
