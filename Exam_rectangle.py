
# 5. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

# գրիր կլաս, Rectangle անունով, որը կազմված է երկարությունից և լայնությունից , իսկ մեթոդը պետք է հաշվի ուղղանկյան մակերեսը


length=int(input("What is the length of your screen in cm?"))
width=int(input("What is the width of your screen in cm?"))
class Rectangle:
        def area(self):
                area=length*width
                return area
print(Rectangle().area())



