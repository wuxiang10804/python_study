import pygame


#定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)

#刷新帧率
FRAMEP_PER_SEC = 60

class GameSprite(pygame.sprite.Sprite):
    """游戏封装的精灵"""

    def __init__(self,image_name,speed=1):
        
        #调用父类的初始化方法
        super().__init__()
        
        #定义对象的自定义属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        
        #在垂直方向上移动
        self.rect.y +=self.speed