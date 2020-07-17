
from plane_sprites import *
from    bullet import *
class Hero(GameSprite):

    def __init__(self):
         # 调用父类方法，设置图像 和速度
        super().__init__("./images/me1.png",0)
        # 设置英雄的初始位置

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        #创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x  +=  self.speed
        self.rect.y  +=  self.speed_y

        # 控制英雄不能超出屏幕

        if  self.rect.x <0:
            self.rect.x = 0
        elif self.rect.right >  SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        
        if  self.rect.y < 0 :
            self.rect.y  = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print("发射子弹 。。。")

        for i in (0,1,2):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置子弹的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            #添加到精灵组
            self.bullets.add(bullet)
