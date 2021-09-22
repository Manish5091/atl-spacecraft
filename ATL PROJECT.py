import pygame

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
bg_rect = bgimg.get_rect()
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
    gamewindow.blit(bgimg,(current_img_x,current_img_y))
    pygame.display.update()     

pygame.quit()
quit()