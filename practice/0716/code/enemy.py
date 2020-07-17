
from plane_sprites import *

class Enemy(GameSprite):
    """
    enemy class
    """
    def __init__(self):
        
        # 调用父类方法，创建敌机精灵，同时制定敌机图片
        super().__init__("./images/enemy1.png")

        #指定敌机的初始随机速度
        self.speed = random.randint(1,3)
        #指定敌机的初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):

        # 调用父亲方法，保持垂直方向的飞行
        super().update()

        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            #print("删除敌机")
            self.kill()

    def __del__(self):
        #print(" 敌机从精灵组中删除 %s" % self.rect)
        pass