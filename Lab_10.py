#Purpose: Lab 10
#   Program Name:RECTANGLE CALCULATOR
#   Exercise:
#   Create an object-oriented program that performs calculations on a rectangle
#
#   Author: Kiara Lindsey
#   Date: November 12, 2020

class Rectangle:
def __init__(self, height, width):
       # / *your code  to initialize class properties goes here * /
    self.height = height
    self.width = width
def getPerimeter(self):
        #/ *your code to calculate perimeter using class properties goes here * /
        2 * self.height + 2 * self.width
return perimeter


def getArea(self):
    #/ *your code to  calculate area using class properties goes here * /
    self.height * self.width
return area


def getStr(self):
    #/ *your code to calculate representation of the rectangle goes
#here – hint, use self.width and self.height to build a multi - line string variables that consists of asterisk characters * /
        for i in range(self.height-2)
            print("*" * self.width)
        for j in range(self.width-2)
            print("*"+ '')
return self


def main():
    print("Rectangle Calculator")
    print()

    while True:
        height = int(input("Height:    "))
        width = int(input("Width:     "))

        #/ *your code to create instance  of Rectangle object goes here * /

#/ *your code to call getPerimeter, getArea, and getStr of newly - created object instance and print those results goes here * /
    rectangle = ( getPerimeter(2 * self.height + 2 * self.width),getArea(self.height * self.width),getStr(("*" *(self.height -2))
    ("""""" *(self.width -2)))
again = input("Continue? (y/n): ").lower()
print()
if again != "y":
    break

print("Bye!")

if __name__ == "__main__":
    main()

