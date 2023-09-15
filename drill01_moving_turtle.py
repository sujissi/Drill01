import turtle

def move_right():
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50)

def move_left():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)

def move_up():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def move_down():
    turtle.setheading(270)
    turtle.stamp()
    turtle.forward(50)
    
def restart():
    turtle.reset()
    
turtle.shape('turtle')
turtle.onkey(move_right,'d')
turtle.onkey(move_right,'a')
turtle.onkey(move_right,'w')
turtle.onkey(move_right,'s')
turtle.onkey(restart,'Escape')

turtle.listen()