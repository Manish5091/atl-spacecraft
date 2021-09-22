import pygame
import random
import sys 
from pygame.constants import K_1



#pygame.mixer.init()
#pygame.mixer.music.load('walking.mp3')
#pygame.mixer.play()
pygame.init()

#SOURCE CODE OF WELCOME SCREEN:- https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3NYLUt5cTNUMjdKbHZhVHYxSEVWRGtZZmRiQXxBQ3Jtc0tsX2dLY0ROSlE1OTl1dmJVVXNja1RLc2ZmNmRGTU1oZS1UVWtNX1hnTkx6OV9kUkhnZDVVclVzWHFBeWNoUzNKSlNaNE53Y3BEZjZ6ZU9FaWhmTlFOZEw2azFEelZ1YTItU1MwXzNzUDhNdXpEcVVfVQ&q=https%3A%2F%2Fwww.codewithharry.com%2Fvideos%2Fpython-game-development-20
#LOOP VIDEO:- https://youtu.be/8ppKSy8aUZc
#WELCOME SCREEN VIDEO:- https://youtu.be/SbC6ODKPEbA

screen_width = 1350
screen_height = 750
black =0,0,0
# Creating Window
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#Welcome Screen
wlc = pygame.image.load("welcome-screen.jpeg")
pygame.display.update()


#Background Image
bgimg = pygame.image.load("background.jpg")
bgimg = pygame.transform.scale (bgimg, (screen_width, screen_height)).convert_alpha()
sprite = pygame.image.load("spawn.png")
sprite = pygame.transform.scale (sprite, (1350, 800)).convert_alpha()
sprite2 = pygame.image.load("end-place.png")
sprite2 = pygame.transform.scale (sprite2, (1350, 360)).convert_alpha()
sprite3 = pygame.image.load("find-shuttle.png")
sprite3 = pygame.transform.scale (sprite3, (1350, 360)).convert_alpha()

bgimg2 = pygame.image.load("background_2.png")
bgimg2 = pygame.transform.scale (bgimg2, (screen_width, screen_height)).convert_alpha()
astron = pygame.image.load("ASTRON.png")
astron = pygame.transform.scale (astron, (100, 100)).convert_alpha()

pygame.display.update()

sprite_rect = bgimg.get_rect()
pygame.display.set_caption("SPACECRAFT")
pygame.display.update()

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

# Game Specific Variables
exit_game = False 
game_over = False

vel = 2

current_img_x = 0
current_img_y = 0

welcome_screen_visible = True


def welcome():
        print('I am in welcome screen function.')
        gamewindow.fill(black)
        gamewindow.blit(wlc,(0,0))
        text_screen("SPACECRAFT", black, 200, 300)

 #creating mouse movement
#pygame.mouse.get_cursor()
#pygame.display.update       
        
# Game Loop
while not exit_game:
    for event in pygame.event.get () :
        print (event )
        if event.type == pygame.QUIT:
            exit_game = True
    if welcome_screen_visible:
        welcome()
    else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
            
              if current_img_y<screen_height:
               current_img_y +=vel
              else:
                sprite = pygame.image.load("find-water.jpg")
                current_img_y=0

            elif keys[pygame.K_s]:
              if current_img_y<screen_height:
               current_img_y -=vel
              else:
                sprite = pygame.image.load("find-water.jpg")
                current_img_y=0
                gamewindow.fill(black)   
            gamewindow.blit(bgimg,(0,0))
            gamewindow.blit(sprite,(current_img_x,current_img_y))
            gamewindow.blit(sprite2,(current_img_x,current_img_y))
            gamewindow.blit(sprite3,(current_img_x,current_img_y))
            gamewindow.blit(bgimg2,(0,0))
            gamewindow.blit(astron,(0,0))
    
pygame.display.update()    

        



             

pygame.quit()
quit()
welcome()


