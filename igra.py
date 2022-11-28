import pygame
from config import dis_width, dis_height
from eda import Food
from zmeya import Snake


class Game:
    pass
'''создаем класс функций, отвечающий за игру'''


def new_game(dis_width, dis_height): 
    '''функция, создающая новую игру'''
    game = Game()
    game.snake = Snake()
    game.over = False
    game.close = False
    game.x = dis_width / 2
    '''начальное положение змейки по осям'''
    game.y = dis_height / 2
    game.x_change = 0 
    '''изменение положения змейки по осям'''
    game.y_change = 0
    game.food = Food()
    return game

def check_game(dis,game):
   if len(game.snake.list) > game.snake.length:
            del game.snake.list[0]
   '''эта функция проверяет, что змейка не увеличивается сама по себе при движении'''
   for x in game.snake.list[:-1]:
            if x == game.snake.head:
                game.close = True
   '''эта функция заканчивает игру, если тело змейки столкнулось с головой'''