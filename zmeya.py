from config import *

class Snake:
    '''создаем класс функций, отвечающий за змейку, заносим туда основные параметры змеи'''
    head = []
    length = 1
    list = []
    block = 10
    speed = 15
    

def draw_snake(dis, snake):
    '''создаем функцию, которая рисует нашу змейку'''
    for x in snake.list:
       pygame.draw.rect(dis, blue, [x[0], x[1], snake.block, snake.block])
       ''' вначале координаты, потом длина и ширина (их мы берем из класса змеи)'''
