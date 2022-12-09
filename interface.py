import pygame
from config import *


def get_display():
   '''
   функция, отвечающая за игровое поле
   задает размер игрового поля (dis)
   добавляет название игры
   '''
   dis = pygame.display.set_mode((dis_width, dis_height))
   pygame.display.set_caption('Змейка от алычы')
   return dis
   
def Your_score(dis, score): 
   ''' 
   функция, выводящая на экран количество очков
   ( с помощью функции render создает поверхность, на которой будет написан текст, 
   а blit отрисовывает дополнительные поверхности на value с определенными координатами
   '''
   value = score_font.render("Ваш счёт: " + str(score), True, pink)
   dis.blit(value, [0, 550])

 
def message(dis, msg, color): 
   '''
   функция, выводящая сообщение mesg на экран
   '''
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 12, dis_height / 2])
