import pygame
from settings import *

class StartButton():
    """
    初始化开始按键
    """
    def __init__(self,imagename,screen):
        self.imagename = imagename
        self.image = pygame.image.load(imagename)
        self.screen = screen

    """
    渲染开始button
    """    
    def update(self) :
        self.screen.blit(self.image,(210,328))