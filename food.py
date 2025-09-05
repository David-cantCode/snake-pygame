import settings
import pygame as py


class Food:

    def __init__(self, position, screen):
        self.position =position 
        self.screen = screen



    
    def draw(self):
        py.draw.rect(self.screen, (250,0,0), (self.position[0], self.position[1], settings.sqaure_size, settings.sqaure_size))


    def eaten_check(self, player_position):
            print(self.position)

            if player_position[0] == self.position[0] and player_position[1] == self.position[1]:
                return True
            return False





