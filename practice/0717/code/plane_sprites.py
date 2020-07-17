
import random
import pygame

from settings import *

class GameSprite(pygame.sprite.Sprite):
    """游戏封装的精灵"""

    def __init__(self,image_name,speed=1):
        
        #调用父类的初始化方法
        super().__init__()
        
        #定义对象的自定义属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed_y = speed

    def update(self):
        
        #在垂直方向上移动
        self.rect.y +=self.speed