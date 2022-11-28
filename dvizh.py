import random
import pygame
from config import *
from interface import message, Your_score
from zmeya import draw_snake, Snake
from igra import Game, new_game, check_game

from eda import *


    

def gameLoop(dis): 
    '''создаем функцию, в которой записан основной алгоритм игры'''
    clock = pygame.time.Clock()
    game = new_game(dis_width, dis_height)
    while not game.over:
        while game.close == True:
            dis.fill(purple)
            message(dis, "Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
            Your_score(dis, game.snake.length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game.over = True
                        game.close = False
                    if event.key == pygame.K_c:
                        game = new_game(dis_width, dis_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.x_change = -game.snake.block
                    game.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    game.x_change = game.snake.block
                    game.y_change = 0
                elif event.key == pygame.K_UP:
                    game.y_change = -game.snake.block
                    game.x_change = 0
                elif event.key == pygame.K_DOWN:
                    game.y_change = game.snake.block
                    game.x_change = 0
        if game.x >= dis_width or game.x < 0 or game.y >= dis_height or game.y < 0:
            game.close = True
        game.x += game.x_change
        game.y += game.y_change
        dis.fill(purple)
        pygame.draw.rect(dis, green, [game.food.x, game.food.y, game.snake.block, game.snake.block])

        game.snake.head = [game.x, game.y]
        game.snake.list.append(game.snake.head)

        draw_snake(dis, game.snake)
        Your_score(dis, game.snake.length - 1)

        check_game(dis, game)
        pygame.display.update()
        eat_food(dis, game)
        clock.tick(game.snake.speed)
    pygame.quit()
    quit()
