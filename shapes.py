from cmath import pi
import math


class Circle:
    pi=math.pi
    def __init__(self,radius):
        self.radius=radius
       
    def area(self):
        Area=pi*(self.radius**2)     
        return Area  
    
    def circumference(self):
        Circumference=(pi*2)+(self.radius*2)
        return Circumference
    
class Square:
    def __init__(self,side):
        self.side=side
        
    def area(self):
        Area=(self.side**2)    
        return Area
    
    def perimeter(self):
        Perimeter=(self.side*2)+(self.side*2)  
        return Perimeter
    
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
    def area(self):
        Area=(self.width*self.height)
        return Area
    
    def perimeter(self):
        Perimeter=(self.width*2)+(self.height*2)
        return Perimeter    
      
class Sphere:
    def __init__(self,radius):
        self.radius=radius
        
    def surface_area(self):
        Surface_area=4*(pi*(self.radius**2))    
        return Surface_area  
    
    def volume(self):
        Volume=4/3*(pi*(self.radius**3))    
        return Volume   
        