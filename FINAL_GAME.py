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
white = 255,255,255
# Creating Window
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#Welcome Screen
wlc = pygame.image.load("welcome-screen.jpeg")
wlc = pygame.transform.scale(wlc, (1350, 750))
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

font = pygame.font.SysFont('Corbel', 55)
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

smallfont = pygame.font.SysFont('Corbel',35)
  
# rendering a text written in
# this font
# white color
color = (255,255,255)
# light shade of the button
color_light = (170,170,170)
# dark shade of the button
color_dark = (100,100,100)


buttons = {'play':{'x':48,'y':100,'text':smallfont.render('Play' , True , color)}
,'instructions':{'x':48,'y':180,'text':smallfont.render('Instructions' , True , color)}
,'quit':{'x':48,'y':260,'text':smallfont.render('Quit' , True , color)}}

def drawButton(text,x,y,button_width=140,button_height=40):
    mouse = pygame.mouse.get_pos()
    button_width = text.get_width()+32
    button_height = text.get_height()+32
    cursorHovered = x <= mouse[0] <= x+button_width and y <= mouse[1] <= y+button_height
   
    pygame.draw.rect(gamewindow,color_light if cursorHovered else color_dark,[x,y,button_width,button_height])  
   

    gamewindow.blit(text , (x+16,y+16))

def whichButtonClicked():
    mouse = pygame.mouse.get_pos()
    buttonToReturn = None
    for key in buttons:
        button = buttons[key]
        text = button['text']
        button_width = text.get_width()+32
        button_height = text.get_height()+32
        if(button['x'] <= mouse[0] <= button['x']+button_width and button['y'] <= mouse[1] <= button['y']+button_height):buttonToReturn = key
    return buttonToReturn

def welcome():
        gamewindow.fill(black)
        gamewindow.blit(wlc,(0,0))
        text_screen("SPACECRAFT", white, 16,16)
        for key in buttons:
            button = buttons[key]
            drawButton(button['text'],button['x'],button['y'])


 #creating mouse movement
#pygame.mouse.get_cursor()
#pygame.display.update       
        
# Game Loop
while not exit_game:
    if welcome_screen_visible:
        welcome()
    for event in pygame.event.get () :
        if event.type == pygame.QUIT:
            exit_game = True
    
          
        keys = pygame.key.get_pressed()
        if not welcome_screen_visible:
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
        elif welcome_screen_visible: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = whichButtonClicked()
                if(button=='play'):welcome_screen_visible = False
                elif(button=='quit'):exit_game = True
                elif(button=='instructions'):print('Instuctions button clicked')

               
    
    pygame.display.update()    

        
pygame.quit()
quit()


