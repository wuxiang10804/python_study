from plane_sprites import *

class Bullet(GameSprite):
    """
    子弹精灵
    """
    def __init__(self):
        #调用父类的方法，设置子弹的图片，设置初始速度
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        super().update()
        # 判断是否飞出屏幕
        if self.rect.bottom < 0: 
            self.kill()

    def __del__(self):
        print("子弹被销毁。。。")