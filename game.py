import pygame
import random
import math
from pygame.locals import *

from models.snake import Snake
from models.cube import Cube

pygame.init()

class MainGame:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.rows = 20
        self.window = pygame.display.set_mode((self.width, self.height))
        self.caption = 'SnaPy'
        self.player = Snake((255,0,0), (10,10))
        self.menu_font =  pygame.font.Font('fonts/menu_font.ttf', 24)
        self.name_font = pygame.font.Font('fonts/name_font.ttf', 30)
        self.cre_by = pygame.font.Font('fonts/menu_font.ttf', 14)
        self.score_font =  pygame.font.Font('fonts/menu_font.ttf', 12)
        self.snack = Cube(self.randomSnack(), color=(0,255,0))
        self.score = 0

    def drawScore(self):
        textobj = self.score_font.render('Score: {0}'.format(self.score), 1, (0,0,0))
        textreact = textobj.get_rect()
        textreact.topleft = (10, 10)
        self.window.blit(textobj, textreact) 

    def drawText(self, text, color, x, y, font):
        textobj = font.render(text, 1, color)
        textreact = textobj.get_rect()
        textreact.topleft = (x, y)
        self.window.blit(textobj, textreact) 

    def redrawGameWindow(self):
        self.window.fill((255,255,255))
        self.player.draw(self.window)
        self.snack.draw(self.window)
        self.drawScore()
        pygame.display.update()

    def redrawMenuWindow(self):
        self.window.fill((255,255,255))
        self.drawText('SnaPy', (0,0,0), 165, 50, self.name_font)
        self.drawText('Press SPACE to start', (0,0,0), 115, 200, self.menu_font)
        self.drawText('Move: WASD/keys', (0,0,0), 130, 250, self.menu_font)
        self.drawText('Created by Wultes', (0,0,0), 330, 450, self.cre_by)
        pygame.display.update()

    def randomSnack(self):
        positions = self.player.body

        while True:
            x = random.randrange(self.rows)
            y = random.randrange(self.rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                continue
            else:
                break
        
        return(x, y)

    def menuGame(self):
        try:
            pygame.display.set_caption(self.caption)
            print('Created by Wultes - https://github.com/wultes/')
            run = True

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.runGame()

                self.redrawMenuWindow()
        except:
            pass

    def runGame(self):
        try:
            pygame.display.set_caption(self.caption)
            run = True

            clock = pygame.time.Clock()

            while run:
                pygame.time.delay(50)
                clock.tick(15)
                self.player.move()
                if self.player.body[0].pos == self.snack.pos:
                    self.score += 1
                    self.player.addCube()
                    self.snack = Cube(self.randomSnack(), color=(0,255,0))
                
                for x in range(len(self.player.body)):
                    if self.player.body[x].pos in list(map(lambda z:z.pos, self.player.body[x+1:])):
                        print('Your score: ', len(self.player.body))
                        self.score = 0
                        self.player.reset((10, 10))
                        break
                
                self.redrawGameWindow()
        except:
            pass
            