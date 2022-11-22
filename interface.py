white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))


pygame.display.set_caption('Змейка от алычы')




 
def Your_score(score):
   value = score_font.render("Ваш счёт: " + str(score), True, yellow)
   dis.blit(value, [0, 0])
 

 
def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 6, dis_height / 3])