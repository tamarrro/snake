import pygame
from config import *


def get_display():
   dis = pygame.display.set_mode((dis_width, dis_height))
   ''' задаем размер игрового поля'''
   pygame.display.set_caption('Змейка от алычы')
   ''' добавляем название игры'''
   return dis
 
def Your_score(dis, score): 
   ''' создаем функцию, которая выводит на экран количество очков'''
   value = score_font.render("Ваш счёт: " + str(score), True, pink)
   dis.blit(value, [0, 550])
 

 
def message(dis, msg, color): 
   '''создаем функцию, которая выводит сообщение на экран'''
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 12, dis_height / 2])

