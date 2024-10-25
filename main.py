from turtle import Screen , Turtle
from snake import Snake
from food import Food

import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
snake = Snake()
food = Food()

screen.listen()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.title('Snake Game')
screen.tracer(0)
'''
positions = [(0,0),(-20,0),(-40,0)]
segments = []
for i in range(3):
    segment = Turtle('square')
    segment.color('white')
    segment.penup()
    segment.goto(positions[i])
    segments.append(segment)
'''

game_on = True
while game_on:
     screen.update()
     time.sleep(0.15)
     snake.move()

     #detect collision
     if snake.head.distance(food)<15:
         food.refresh()
         snake.extend()
     if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
         game_on = False
         res = Turtle()
         res.color("white")
         res.write("GAME OVER",font = (36))
         res.penup()

         res.goto(-20,0)
     for segment in snake.segments:
         if segment == snake.head:
             pass
         elif snake.head.distance(segment)<10:
             game_on = False
             res = Turtle()
             res.color("white")
             res.write("GAME OVER",font = (36))
             res.penup()






screen.exitonclick()