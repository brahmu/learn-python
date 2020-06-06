print("hello python");
if 2>1 :
    print("2 is grater than 1")
else :
    print("1 is grater than 2")
import math
def area_circle(radius):
    area = 2 * math.pi * radius
    return "The area of circle radius {} is {}".format(radius, area)
print(area_circle(4))

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Welcome {}!".format(self.name))
p1 = Person("deepak");
p1.greet();