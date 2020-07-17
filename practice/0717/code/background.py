
from plane_sprites import *

class Background(GameSprite):
    """
    background sprite
    """
    def __init__(self, is_alt=False):
        
        #调用父类方法实现精灵的创建（image / rect / speed）
        super().__init__("./images/background.png")

        # 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        
        # 调用父类的方法实现
        super().update()
        
        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height