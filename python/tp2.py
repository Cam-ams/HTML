import sys
import math
import matplotlib.pyplot as plt # type: ignore

DRAW_NSTEPS = 10240

class Paint:
    def __init__(self, width=1000, height=1000): 
        self.canvas = []
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append([255, 255, 255])
            self.canvas.append(line_data)

    def set_pixel(self, x, y, r=0, g=0, b=0):
        if x < 0 or y < 0:
            return
        if y >= len(self.canvas):
            return
        if x >= len(self.canvas[y]):
            return

        self.canvas[y][x] = [r, g, b]

    def show(self):
        plt.gca().invert_yaxis()
        plt.imshow(self.canvas)
        plt.show()
        sys.exit(0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, autre):
        s =  (autre.x - self.x) ** 2
        s += (autre.y  - self.y) ** 2
        return math.sqrt(s)

    def draw(self, paint):
        paint.set_pixel(self.x, self.y)

class Ligne:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_length(self):
        return self.a.dist(self.b)

    def draw(self, paint):
        dx = (self.b.x - self.a.x) / DRAW_NSTEPS
        dy = (self.b.y - self.a.y) / DRAW_NSTEPS

        x = float(self.a.x)
        y = float(self.a.y)
        for step in range(DRAW_NSTEPS):
            paint.set_pixel(int(round(x, 0)), int(round(y, 0)))
            x += dx
            y += dy

paint = Paint()

#### Début du sujet
### Geometric objects here

###


class Parallelogramme ():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

        d_x=c.x+ (b.x-a.x)
        d_y=c.y + ( b.y - a.y)
        self.d=Point(d_x , d_y)
        d=self.d

        self.ab=Ligne(a, b)
        self.ac=Ligne(a, c)
        self.bc=Ligne(b, c)
        self.bd=Ligne(b, d)
    
    def draw(self, paint):
        self.ab.draw(paint)
        self.ac.draw(paint)
        self.bc.draw(paint)
        self.bd.draw(paint)




class rectangle(Parallelogramme):
    def __init__(self, a, b, ac):

        ab=a.dist(b)
        delta_x=b.x-a.x
        delta_y=b.y-a.y


        c_x = a.x + ac* (delta_x / ab)
        c_y=a.x+ac*(delta_x/ab)

        c=Point(c_x, c_y)
        Parallelogramme.__init__(self,a, b, c)

r=rectangle(Point(100,100), Point(200,400), 200)
    


class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c


        self.ab=Ligne(a, b)
        self.ac=Ligne(a, c)
        self.bc=Ligne(b, c)
        
    
    def draw(self, paint):
        self.ab.draw(paint)
        self.ac.draw(paint)
        self.bc.draw(paint)


class TriangleRectangle(Triangle):
    def __init__(self, a, b,teta):
     
     ab=a.dist(b)
     ac=math.cos(teta)*ab
     
     c_x=a.x
     c_y=a.y+ac*((b.x-a.x)/ab)
     
     c=Point(c_x, c_y)

     Triangle.__init__(self,a,b,c)





t=TriangleRectangle(Point(100,400),Point(200,600),90)


t.draw(paint)
paint.show()
        
        

        

