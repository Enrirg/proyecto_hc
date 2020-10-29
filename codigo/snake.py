from turtle import *
from random import randrange
from freegames import square, vector
from random import randint 



food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
col2 = 0

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    col = 0
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:

        col = randint(1,4)
        if col == 1:
            square(head.x, head.y, 9,color="blue")
            update()

        elif col == 2:
            square(head.x, head.y, 9,color="green")
            update()


        elif col == 3:
            square(head.x, head.y, 9,color="yellow")
            update()
        
        elif col == 4:
            square(head.x, head.y, 9,color="black")
            update()



        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        col2= randint(1,4)
        

        if col == 1:
            square(body.x, body.y, 9, 'black')
            update()

        elif col == 2:
            square(body.x, body.y, 9,color="green")
            update()


        elif col == 3:
            square(body.x, body.y, 9,color="yellow")
            update()

        elif col == 4:
            square(body.x, body.y, 9,color="black")
            update()


    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, randint(1, 100))



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
