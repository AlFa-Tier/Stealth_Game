import pygame

from Inputs import Inputs

width,height = 1000,600

pygame.init()
screen = pygame.display.set_mode((width, height))


while True:
    # process inputs
    
    if Inputs.QUIT in Inputs:
        pygame.quit()

    if Inputs.MOVE_UP in Inputs:
        print("Moving")

    # update everything
    pygame.display.update()