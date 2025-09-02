import pygame as py
import map
import settings

screen_w =  settings.sqaure_size * map.cols
screen_h =  settings.sqaure_size * map.rows


screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("snake ") 
clock  = py.time.Clock()




class Player:
    def __init__(self, position, direction, last_position, size):

        #idea for movement: 
            #store head pos in position
            #have rest of the body in a array called last_posisitons


        self.position = list(position)
        self.direction = list(direction)  #gotta conv to list bc you cant assign values to tuples which is dumb
        self.last_position = last_position 
        self.size = size
        self.body_positions = []




    def move(self):


        #wrap around the screen when going too far left, right, up , down

        if self.position[0] >= map.cols * settings.sqaure_size:
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = (map.cols - 1) * settings.sqaure_size

        if self.position[1] >= map.rows * settings.sqaure_size:
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = (map.rows - 1) * settings.sqaure_size
      


    #update head pos                                      

        prev_position = self.position.copy()
                                             #* tile size to lock to map
        self.position[0] += self.direction[0] * settings.sqaure_size
        self.position[1] += self.direction[1] * settings.sqaure_size



    #update body
        if self.size > 1:
            self.body_positions.insert(0, prev_position)  # add old head
            if len(self.body_positions) > self.size - 1:  # trim tail
                self.body_positions.pop()







    def draw(self):
        #draw head
        py.draw.rect(screen, (0,250,0), (self.position[0], self.position[1], settings.sqaure_size, settings.sqaure_size))


        #draw body

        for body in self.body_positions:
            py.draw.rect(screen, (0, 200, 0),(body[0], body[1],settings.sqaure_size, settings.sqaure_size))

        print(f" Pos: {self.position[0]} , {self.position[1]}")
        print(f" Dir : {self.direction[0]} , {self.direction[1]}")








player = Player((250,250), (0,1), [0], 3)












def spawn_food():
    pass







running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False


        #key interupts 
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                player.direction = (0,-1)
            if event.key == py.K_s:
                player.direction = (0,1)      

            if event.key == py.K_a:
                player.direction = (-1,0)
            if event.key == py.K_d:
                player.direction = (1,0)               



    screen.fill((0, 0, 0)) 
    player.draw()
    player.move()
   

    py.display.flip() 
    clock.tick(5)