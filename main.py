from turtle import Turtle, Screen
snake = Turtle()
Screen().setup(width=500, height=500)
Screen().bgcolor("black")
Screen().title("Snake Game")
isOn = False


def start():
    global isOn
    isOn = True
    on()


size = 3
snake.turtlesize(0.5, size)
snake.shape("square")
snake.color("white")
Screen().listen()
Screen().onkey(key="space", fun=start)


def left():
    # snake.left(90)
    snake.setheading(snake.heading() + 30)


def right():
    # snake.right(90)
    snake.setheading(snake.heading() - 30)


def out():
    global isOn
    snake.clear()
    isOn = False


def on():
    while isOn:
        snake.penup()
        snake.forward(2)
        Screen().onkey(key="a", fun=left)
        Screen().onkey(key="d", fun=right)
        Screen().onkey(key="c", fun=out)


scr = Screen()
scr.exitonclick()
if __name__ == '__main__':
    print('PyCharm')


