import pygame
from config import *


def get_display():
   dis = pygame.display.set_mode((dis_width, dis_height))
   pygame.display.set_caption('Змейка от алычы')
   return dis
 
def Your_score(dis, score):
   value = score_font.render("Ваш счёт: " + str(score), True, yellow)
   dis.blit(value, [0, 0])
 

 
def message(dis, msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 6, dis_height / 3])