import pygame
# from enum import Enum

class Inputs:
    QUIT = 1
    MOVE_UP = 2
    MOVE_RIGHT = 3
    MOVE_DOWN = 4
    MOVE_LEFT = 5
    SUCCESS = 6
    FAIL = 7
    CRITICAL = 8

    def __init__(self):
        self.state = {
            Inputs.MOVE_UP: False,
            Inputs.MOVE_RIGHT: False,
            Inputs.MOVE_DOWN: False,
            Inputs.MOVE_LEFT: False,
            Inputs.CRITICAL: False,
            Inputs.FAIL: False, 
            Inputs.SUCCESS: False,
            }
    
    def __contains__(self, item):
        return self.state[item]
    
    def process_inputs(self):
        self.state[Inputs.QUIT] = False
        self.state[Inputs.MOVE_UP] = False
        self.state[Inputs.MOVE_RIGHT] = False
        self.state[Inputs.MOVE_DOWN] = False
        self.state[Inputs.MOVE_LEFT] = False
        

        action = pygame.key.get_pressed()
        

        if action[pygame.K_w]:
            self.state[Inputs.MOVE_UP] = True
        if action[pygame.K_a]:
            self.state[Inputs.MOVE_RIGHT] = True
        if action[pygame.K_s]:
            self.state[Inputs.MOVE_DOWN] = True
        if action[pygame.K_d]:
            self.state[Inputs.MOVE_LEFT] = True
        if action[pygame.K_LSHIFT]:
            self.state[Inputs.CRITICAL] = True
        if action[pygame.K_y]:
            self.state[Inputs.SUCCESS] = True
        if action[pygame.K_n]:
            self.state[Inputs.FAIL] = True
        if action[pygame.K_ESCAPE] or action[pygame.K_q]:
            self.state[Inputs.QUIT] = True

        return self