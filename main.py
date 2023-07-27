from turtle import Turtle, Screen

terry = Turtle()
screen = Screen()

### alterado
## mais uma alteração
def move_forward():
    terry.forward(10)
#comment

def move_backwards():
    terry.backward(10)


def turn_right():
    terry.right(10)


def turn_lef():
    terry.left(10)


def clear():
    terry.penup()
    terry.home()
    terry.clear()
    terry.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_lef)
screen.onkey(key="c", fun=clear)


screen.exitonclick()

