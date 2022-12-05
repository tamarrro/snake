import pygame
from config import *


def get_display():
   dis = pygame.display.set_mode((dis_width, dis_height))
   ''' задаем размер игрового поля'''
   pygame.display.set_caption('Змейка от алычы')
   ''' добавляем название игры (caption - подпись)'''
   return dis
   ''' нам вовзращают экран со всеми этими параметрами'''

def Your_score(dis, score): 
   ''' создаем функцию, которая выводит на экран количество очков'''
   value = score_font.render("Ваш счёт: " + str(score), True, pink)
   dis.blit(value, [0, 550])
   ''' render создает поверхность, на которой написан текст
   blit отрисовывает дополнительные поверхности на value, с координатами определенными'''

 
def message(dis, msg, color): 
   '''создаем функцию, которая выводит сообщение на экран'''
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 12, dis_height / 2])
