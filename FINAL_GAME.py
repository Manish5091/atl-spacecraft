import pygame
import random

from pygame.constants import K_1

#pygame.mixer.init()
#pygame.mixer.music.load('')
#pygame.mixer.music.play()
pygame.init()


screen_width = 1350
screen_height = 750
black =0,0,0
# Creating Window
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#Welcome Screen
wlc = pygame.image.load("1.jpeg")
pygame.display.update()

#Background Image
bgimg = pygame.image.load("BACKGROUND.jpg")
bgimg = pygame.transform.scale (bgimg, (screen_width, screen_height)).convert_alpha()
sprite = pygame.image.load("2.png")
sprite = pygame.transform.scale (sprite, (1350, 800)).convert_alpha()
pygame.display.update()

sprite_rect = bgimg.get_rect()
pygame.display.set_caption("SPACECRAFT")
pygame.display.update()
  
# Game Specific Variables
exit_game = False 
game_over = False

vel = 2
current_img_x = 0
current_img_y = 0
# Game Loop
while not exit_game:
    for event in pygame.event.get () :
        print (event )
        if event.type == pygame.QUIT:
            exit_game = True

            keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if current_img_y<screen_height:
               current_img_y +=vel
            else:
                bgimg = pygame.image.load("finding-water.jpg")
                current_img_y=0

    gamewindow.fill(black)   
    gamewindow.blit(bgimg,(0,0))
    gamewindow.blit(sprite,(current_img_x,current_img_y))
    pygame.display.update()     

pygame.quit()
quit()
