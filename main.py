import pygame as py
import map
import settings
import player as p

screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows


screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("snake ") 
clock  = py.time.Clock()








#              ini_position   ini_dir    size 
player = p.Player((250,250),   (0,1),     2,      screen)









running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False


        #key interupts sorry for all the if statements
        if event.type == py.KEYDOWN:

            if event.key == py.K_w: 
                if player.direction != (0, 1):   #prevent snake from going into itself
                    player.direction = (0, -1)

            if event.key == py.K_s:  
                if player.direction != (0, -1):  
                    player.direction = (0, 1)

            if event.key == py.K_a:  
                if player.direction != (1, 0):   
                    player.direction = (-1, 0)

            if event.key == py.K_d:  
                if player.direction != (-1, 0):  
                    player.direction = (1, 0)
                







    screen.fill((0, 0, 0)) 
    player.draw()
    player.move()
   

   

    py.display.flip() 
    clock.tick(5)