#Roxana Villagomez
#Date 3/4/2022

#Module 7 Lab Activities

#Problem 1:

import math

radius = float(input("Enter the radius of the circle:"))

area=math.pi*radius*radius

print("Area of the Circle is: {0}".format(area))


#Problem 2:


number= int(input('Enter a number to check in range(1,10):'))

if number >=1 and number <=10:
    print('The number is in range(1,10)')

else:
    print('The number is not in range(1,10)')

#Problem 3:


mylist=[5,2,7,-1]

listsum=sum(mylist)

print('\nsum of the list is ',listsum)

#Problem 4:

def my_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(my_list([1, 3, 3, 3, 6, 2, 3, 5]))

#Problem 5:


import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color('blue')
side = 20
width = 10
for squares in range(5):
    drawSquare(alex,side)
    alex.penup()
    alex.back(width)
    alex.right(90)
    alex.forward(width)
    alex.left(90)
    alex.pendown()
    side+=2*width
wn.exitonclick()


#Problem 6:

import turtle


def drawFlower(d,p,n):
    angle=360/n
    for i in range(p):
        for count in range(n):
            turtle.fd(d)
            turtle.lt(angle)
        turtle.lt(360/p)


drawFlower(100,10,6)
turtle.getscreen()._root.mainloop()

