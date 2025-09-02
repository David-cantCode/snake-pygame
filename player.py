import pygame as py
import settings 
import map

class Player:
    def __init__(self, position, direction, size, screen):


        self.position = list(position)
        self.direction = list(direction)  #gotta conv to list bc you cant assign values to tuples which is dumb
        self.last_position = 0 
        self.size = size
        self.body_positions = []

        self.screen = screen

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
        py.draw.rect(self.screen, (0,250,0), (self.position[0], self.position[1], settings.sqaure_size, settings.sqaure_size))


        #draw body

        for body in self.body_positions:
            py.draw.rect(self.screen, (0, 200, 0),(body[0], body[1],settings.sqaure_size, settings.sqaure_size))

        print(f" Pos: {self.position[0]} , {self.position[1]}")
        print(f" Dir : {self.direction[0]} , {self.direction[1]}")



    def get_positions(self):
        #ret all pos of head and all of body
        return [tuple(self.position)] + [tuple(pos) for pos in self.body_positions]
