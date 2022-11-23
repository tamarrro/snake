from config import *

class Snake:
    head = []
    length = 1
    list = []
    block = 10
    speed = 15
    

def our_snake(dis, snake):
   for x in snake.list:
       pygame.draw.rect(dis, black, [x[0], x[1], snake.block, snake.block])