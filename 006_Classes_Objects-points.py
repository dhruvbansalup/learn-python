# Classes & Objects

# Using Coordinates
class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    def translate(self,deltaX,deltaY):
        self.x+=deltaX
        self.y=deltaY
    def Odistance(self):
        import math
        d=math.sqrt(self.x*self.x+self.y*self.y)
        return d
    
    def __str__(self):
        return('('+str(self.x)+','+str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x+p.x,self.y+p.y))

# a=Point(2,3)
# b=Point(5,6)
# c=a+b
# print(c)

# Polar Form
import math
class Point:
    def __init__(self,a=0,b=0):
        self.r=math.sqrt(a*a+b*b)
        if a==0:
            self.theta=math.pi/2
        else:
            self.theta=math.atan(b/a)
        
    def Odistance(self):
        return(self.r)
    
    def translate(self,deltaX,deltaY):
        x=self.r*math.cos(self.theta)
        y=self.r*math.sin(self.theta)
        x+=deltaX
        y==deltaY

        self.r=math.sqrt(x*x+y*y)
        if x==0:
            self.theta=math.pi/2
        else:
            self.theta=math.atan(y/x)
    
    def __str__(self):
        return('r: '+str(self.r)+'\n'+'theta: '+str(self.theta)+' radian')
    
    
# z=Point(1,2)
# print(z)