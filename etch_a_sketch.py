import turtle as t
from turtle import Screen
tim=t.Turtle()
screen=Screen()

tim.speed("fastest")
def move_Forward():
    tim.forward(50)

def move_right():
    tim.right(10)
    # tim.forward(50)
    

def move_left():
    tim.left(10)
    # tim.forward(50)
    
def move_back():
    tim.backward(20)
    
def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=move_Forward)#here we are passing the function as aninput so we only pass the name without the () at the end
screen.onkey(key="s",fun=move_back)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="c",fun=clear)


screen.exitonclick()