import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (self.radius**2)*math.pi
    def perimeter(self):
        return self.radius*2*math.pi
    
c1=Circle(5)
print(f'面积是{c1.area():.3f}')
print(f'周长是{c1.perimeter():.3f}')
