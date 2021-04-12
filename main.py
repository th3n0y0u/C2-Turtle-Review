'''

4/12/2021

Review

1. import turtle libary
import turtle # top of page

2. declare turtle
variable1 = turtle.turtle()

3. declare screen(option)
variable2 = turtle.Screen()

4. movements
  a. forward
  variable1.forward(DISTANCE)
  variable.fd(DISTANCE)

  b. backward
  variable1.backward(DISTANCE)
  variable.bk(DISTANCE)

  c. turn right
  variable1.right(ANGLE)

  d. turn left
  variable.left(ANGLE)

5. pen features
  penup
  variable1.penup()

  pendown
  variable1.pendown()

  move to a point
  variable1.goto(x, y)

  move to the origin
  variable1.home()

  color
  variable1.color(rgb)

  shape(arrow, turtle, circle, square)
  variable1.shape("SHAPE")

  speed
  variable1.speed()

  write
  variable1.write(TEXT, MOVE, ALIGN, FONT)

  width(1,10)
  variable1.width()
  
  circle
  variable.circle(RADIUS)

  fill color
  variable1.fill("COLOR")
  variable1.begin_fill()
  # SHAPE
  variable1.end_fill()

'''
import turtle

artist = turtle.Turtle()
artist.shape("turtle")
artist.speed(3)

# Exercise 1: Drawing a star
def drawStar(l):
  for i in range(5):
    artist.forward(l) 
    artist.right(144) 

drawStar(int(input("LENGTH: ")))

# Exercise 2: Draw a Shape with circle()
def drawShape(r, s):
  for i in range(s):
    artist.circle(r, 360, s)
  
drawShape(float(input("Radius:")), int(input("Number of Sides:")))

# Exercise 3: Draw a Spiral
colors = ["yellow", "blue", "green", "orange", "red",  "pink"]
def drawSpiral():
  for i in range(40):
    artist.color(colors[i % 6])
    artist.width(i / 5 + 1)
    artist.forward(i)
    artist.left(20)
drawSpiral()