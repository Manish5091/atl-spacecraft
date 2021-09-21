import pygame
import random

#pygame.mixer.init()
#pygame.mixer.music.load('')
#pygame.mixer.music.play()
pygame.init()


screen_width = 1200
screen_height = 600
black =0,0,0
# Creating Window
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bgimg = pygame.image.load("Spawn.jpg")
bgimg = pygame.transform.scale (bgimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("SPACECRAFT")
pygame.display.update()
  
# Game Specific Variables
exit_game = False 
game_over = False

# Game Loop
while not exit_game:
    for event in pygame.event.get () :
        print (event )
        if event.type == pygame.QUIT:
            exit_game = True



    gamewindow.fill(black)   
    gamewindow.blit(bgimg,(0,0))
    pygame.display.update()     

pygame.quit()
quit()

