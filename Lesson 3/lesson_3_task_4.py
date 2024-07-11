from turtle import *

t = Turtle()

my_turtle = Turtle()
my_turtle.screen.setup(800, 800)

t.speed(200)
t.screen.bgcolor("yellow")

#голова():
t.circle(90)
t.up()
t.circle(90,110)
t.down()

#уши():
t.right(30)
t.forward(120)
t.right(230)
t.forward(120)
t.right(70)
t.forward(110)
t.right(230)
t.forward(125)

#левый глаз:
t.left(90)
t.up()
t.forward(40)
t.down()
t.circle(10)

#правый глаз:
t.up()
t.forward(80)
t.down()
t.circle(10)

#правый ус:
t.right(90)
t.up()
t.forward(40)
t.down()
t.left(110)
t.forward(90)
t.right(110)
t.up()
t.forward(30)
t.down()
t.right(90)
t.forward(85)
t.right(210)
t.forward(100)

#левый ус:
t.right(150)
t.up()
t.forward(250)
t.down()
t.left(210)
t.forward(95)
t.left(150)
t.forward(95)    
t.right(90)
t.up()
t.forward(35)
t.down()
t.right(110)
t.forward(100)

#рот :
t.up()
t.forward(80)
t.down()
t.left(135)
t.circle(15,120)
t.circle(-10,110)
t.circle(15,120)

t.circle(15,115)
t.forward(40)
t.circle(15,115)

my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()