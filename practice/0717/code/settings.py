
import pygame

#定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)

#刷新帧率
FRAMEP_PER_SEC = 60

#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

#击败一架敌机获得的分数
POINT = 1


class Settings():

    def __init__(self):
        self.screen_width = 480
        self.screen_height = 700
        