import random
import pygame
from config import *
from interface import message, Your_score
from zmeya import draw_snake, Snake
from igra import Game, new_game, check_game

from eda import *


    

def gameLoop(dis): 
    ''' 
    функция, включающая основной алгоритм игры
    в класс game задаются параметры экрана - dis.widht (ширина) и dis_height (высота)
    '''
    clock = pygame.time.Clock()
    game = new_game(dis_width, dis_height)
    while not game.over:
        while game.close == True:
            ''' 
            при завершении игры экран заполняется фиолетовым, 
            на экран выводится сообщение и отображается счет игрока
            '''
            dis.fill(purple)
            message(dis, "Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
            Your_score(dis, game.snake.length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.over = True
                    game.close = False'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #если нажата клавиша Q, игра заканчивается
                        game.over = True
                        game.close = False
                    if event.key == pygame.K_c:
                        #если нажата клавиша "C", игра начинается снова
                        game = new_game(dis_width, dis_height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.over = True
            if event.type == pygame.KEYDOWN:
                if game.y_change == 0 and game.x_change == 0:
                    game.x_change = game.snake.block
                    game.y_change = 0
                if event.key == pygame.K_LEFT and game.y_change != 0:
                    game.x_change = -game.snake.block
                    game.y_change = 0

                elif event.key == pygame.K_RIGHT and game.y_change != 0:
                    game.x_change = game.snake.block
                    game.y_change = 0
                    
                elif event.key == pygame.K_UP and game.x_change != 0:
                    game.x_change = 0
                    game.y_change = -game.snake.block
                    
                elif event.key == pygame.K_DOWN and game.x_change != 0:
                    game.x_change = 0
                    game.y_change = game.snake.block
        if game.x >= dis_width or game.x < 0 or game.y >= dis_height or game.y < 0:
            game.close = True
            #если положение змеи вышло за края экрана, игра заканчивается
        game.x += game.x_change
        game.y += game.y_change
        dis.fill(purple)
        pygame.draw.rect(dis, green, [game.food.x, game.food.y, game.snake.block, game.snake.block])
        #генерация новых объектов еды
        game.snake.head = [game.x, game.y]
        game.snake.list.append(game.snake.head)
        #длина змеи увеличивается на 1, если она съела еду
        draw_snake(dis, game.snake)
        Your_score(dis, game.snake.length - 1)
        check_game(dis, game)
        pygame.display.update()
        eat_food(dis, game)
        clock.tick(game.snake.speed)
    pygame.quit()
    quit()
