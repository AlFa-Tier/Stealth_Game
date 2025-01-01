import pygame
from sys import exit

from Inputs import Inputs

width,height = 1000,600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stealth Mini-game')
# pygame.display.set_icon(icon)
framerate = pygame.time.Clock()

w,h = width/5,height/5
test_surface = pygame.Surface((w,h))
test_surface.fill("Red")

"""
while True:
    # process inputs
    
    if Inputs.QUIT in Inputs:
        pygame.quit()

    if Inputs.MOVE_UP in Inputs:
        print("Moving")

    # update everything
    pygame.display.update()
    """

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(test_surface,(5,5))

    #update everything
    pygame.display.update()
    framerate.tick(60)