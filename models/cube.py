import pygame
import math

class Cube:
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = dirny
        self.color = color
        self.width = 500
        self.rows = 20
    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self, window, eyes=False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(window, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(window, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(window, (0,0,0), circleMiddle2, radius)