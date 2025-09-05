import pygame as py
import map
import settings
import player as p
import food as f
import random as rn

screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows


screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("snake ") 
clock  = py.time.Clock()

active_food = False #if there is food on the map true 





#              ini_position   ini_dir    size 
player = p.Player((250,250),   (0,1),     2,      screen)

food = 0



def get_food():

    global active_food

    #check to positions of player so we dont spawn food on him 
    all_positions = [(x * settings.sqaure_size + 10, y * settings.sqaure_size + 10) for x in range(map.cols) for y in range(map.rows)]
    player_positions = player.get_positions()


    valid_positions = [pos for pos in all_positions if pos not in player_positions]

    if not valid_positions: settings.game_over = true


    active_food = True
            
    return f.Food(rn.choice(valid_positions), screen)







def reset_game():
    pass









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




    if not active_food: food = get_food()
    if settings.game_over: reset_game() 

    food.draw()





    if food.eaten_check(player.position) == True: player.size += 1; active_food = False
   



    py.display.flip() 
    clock.tick(settings.fps)