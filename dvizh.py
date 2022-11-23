import random
import pygame
from config import *
from interface import message, Your_score
from zmeya import our_snake, Snake

class Game:
    pass

def new_game(dis_width, dis_height):
    game = Game()
    game.snake = Snake()
    game.over = False
    game.close = False
    game.x = dis_width / 2
    game.y = dis_height / 2
    game.x_change = 0
    game.y_change = 0
    game.foodx = round(random.randrange(0, dis_width - game.snake.block) / 10.0) * 10.0
    game.foody = round(random.randrange(0, dis_height - game.snake.block) / 10.0) * 10.0
    return game
    

def gameLoop(dis):
    clock = pygame.time.Clock()
    game = new_game(dis_width, dis_height)
    while not game.over:
        while game.close == True:
            dis.fill(blue)
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
        dis.fill(blue)
        pygame.draw.rect(dis, green, [game.foodx, game.foody, game.snake.block, game.snake.block])

        game.snake.head = [game.x, game.y]
        game.snake.list.append(game.snake.head)

        our_snake(dis, game.snake)
        Your_score(dis, game.snake.length - 1)

        if len(game.snake.list) > game.snake.length:
            del game.snake.list[0]
        for x in game.snake.list[:-1]:
            if x == game.snake.head:
                game.close = True
        pygame.display.update()
        if game.x == game.foodx and game.y == game.foody:
            game.foodx = round(random.randrange(0, dis_width - game.snake.block) / 10.0) * 10.0
            game.foody = round(random.randrange(0, dis_height - game.snake.block) / 10.0) * 10.0
            game.snake.length += 1
        clock.tick(game.snake.speed)
    pygame.quit()
    quit()
