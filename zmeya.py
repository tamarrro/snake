snake_block = 10
snake_speed = 15


def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])