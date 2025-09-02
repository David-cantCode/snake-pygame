import pygame as py
import map
import settings

screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows


screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("snake ") 
clock  = py.time.Clock()




class Player:
    def __init__(self,position, direction):
        self.position = position
        self.direction = direction







    def move(self):
        if self.position[0] > map.cols: self.position[0] = 0
        if self.position[0] < 0: self.position[0] = map.cols

        if self.position[1] > map.rows: self.position[1] = 0
        if self.position[1] < 0: self.position[1] = map.rows 

        #self.position += direction

            #Note: what the fuck does this even mean
            #what was i thinking when i wrote this shit lmao



    def draw(self):
        py.draw.rect(screen, (0,250,0), (self.position[0], self.position[1], settings.sqaure_size, settings.sqaure_size))
     









player = Player((250,250), (0,0))












def spawn_food():
    pass







running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False

        screen.fill((0, 0, 0)) 
        player.draw()
        
   

    py.display.flip() 
    clock.tick(30)