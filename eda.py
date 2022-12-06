
import pygame
import random
from config import dis_width, dis_height

class Food:
   '''создаем класс функций, отвечающий за еду'''
   x = 10
   y = 10
   '''размеры еды'''


food = Food()
''' теперь любое упоминание еды будет переносить нас в класс'''

def eat_food(dis, game):  
    '''при столкновении змеи с едой создается новая еда, а длина змеи увеличивается на единицу'''
    if game.x == game.food.x and game.y == game.food.y:
    ''' если координаты змеи совпадают с координатами еды'''
         game.food.x = round(random.randrange(0, dis_width - game.snake.block) / 10.0) * 10.0
        ''' теперь координаты еды становятся рандомными'''
         game.food.y = round(random.randrange(0, dis_height - game.snake.block) / 10.0) * 10.0
         game.snake.length += 1
         ''' змейка растет'''

