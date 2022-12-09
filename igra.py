import pygame
from config import dis_width, dis_height
from eda import Food
from zmeya import Snake


class Game:
    pass


def new_game(dis_width, dis_height): 
    '''
    функция, создающая новую игру
    в качестве game берем класс game
    в качестве подкласса игры snake берем класс snake
    game.x, game.y - начальное положение змейки
    game.x_change, game.y_change - изменение положения змейки
    в качестве food берем класс food
    '''
    game = Game()
    game.snake = Snake()
    game.over = False
    game.close = False
    game.x = dis_width / 2
    game.y = dis_height / 2
    game.x_change = 0 
    game.y_change = 0
    game.food = Food()
    return game

def check_game(dis,game):
    '''
    функция, проверяющая, не увеличивается ли змейка сама по себе при движении
    игра заканчивается, если тело змейки столкнулось с головой
    '''
   if len(game.snake.list) > game.snake.length:
            del game.snake.list[0]
   for x in game.snake.list[:-1]:
            if x == game.snake.head:
                game.close = True
