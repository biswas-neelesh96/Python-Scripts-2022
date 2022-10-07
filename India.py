import turtle as tu  

tu.bgcolor("#ffb3b3")   
tu.speed(1)
tu.penup()
tu.goto(-200,200)
tu.pendown()

def rect(x,y):
    tu.begin_fill()
    tu.forward(x)
    tu.left(90)
    tu.forward(y)
    tu.left(90)
    tu.forward(x)
    tu.left(90)
    tu.forward(y)
    tu.penup()
    tu.forward(y)
    tu.pendown()
    tu.end_fill()
    tu.left(90)    

tu.color("#FF9933")
rect(450,100)
tu.color("#FFFFFF")
rect(450,100)
tu.color("#138808")
rect(450,100)
tu.penup()
tu.goto(0,100)
tu.pendown()

tu.pensize(4)
tu.color("#000080")
r = 50
tu.circle(r)

for i in range(24):
    tu.pensize(2)
    tu.penup()
    tu.goto(0,150)
    tu.pendown()
    tu.forward(50)
    tu.left(15)

tu.hideturtle()
