
import pygame
import random
from config import dis_width, dis_height

class Food:
   '''создаем класс функций, отвечающий за еду, задаем ее размер'''
   x = 10
   y = 10 
   


food = Food()
''' теперь любое упоминание еды будет переносить нас в класс'''

def eat_food(dis, game):  
    '''
    при столкновении змеи с едой (если совпадают координаты game.x и game.food.x и game.y и game.food.y, 
    создается новая еда, а длина змеи увеличивается на единицу
    новые координаты еды определяются случайным образом
    '''
    if game.x == game.food.x and game.y == game.food.y:
         game.food.x = round(random.randrange(0, dis_width - game.snake.block) / 10.0) * 10.0
         game.food.y = round(random.randrange(0, dis_height - game.snake.block) / 10.0) * 10.0
         game.snake.length += 1

