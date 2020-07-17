

import pygame.font
from pygame.sprite import Group

class Scoreboard():
    """
    显示得分信息的类
    """
    def __init__(self,screen,stats):
        """
        初始化得分涉及的属性
        """
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
         
        """
        显示得分信息使用的字体设置
        """
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        """
        准备初始化得分图像
        """
        self.prep_score()


    def prep_score(self):
        """
        得分转换为一幅渲染的图像
        """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,(195, 200, 201))

        """
        将得分放在屏幕的右上角
        """
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """
        在屏幕上显示得分
        """        
        self.screen.blit(self.score_image,self.score_rect)


    def update_score(self,stats):
        self.stats = stats
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,(195, 200, 201))
