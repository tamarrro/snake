from config import *

class Snake:
    '''
    класс функций, отвечающий за змейку
    head - координаты головы
    lenght - начальная длина
    list - пустой лист
    block - размер блока
    speed - скорость
    '''
    head = []
    length = 1
    list = []
    block = 10
    speed = 15
    

def draw_snake(dis, snake):
    '''
    функция, рисующая змейку
    dis - экран
    snake - змея
    blue - цвет змеи
    x[0] и x[1] - новые координаты змеи
    snake.block - длина и ширина новых блоков (берем из класса змеи)
    '''
    for x in snake.list:
       pygame.draw.rect(dis, blue, [x[0], x[1], snake.block, snake.block])
      
