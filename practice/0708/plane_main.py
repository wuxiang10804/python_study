import pygame
from  plane_sprites import *


class PlaneGame():
    """
    主游戏类
    """
    def __init__(self):
        
        #创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        
        #创建游戏的时钟
        self.clock = pygame.time.Clock()

        #调用私有方法，精灵和精灵组的创建
        self.__create_sprites()


    def __create_sprites(self):
        pass



    def start_game(self):
        while  True:

            # 设置刷新频率
            self.clock.tick(FRAMEP_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()
            
    
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()


    def __check_collide(self):
        pass
    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()




if __name__ == "__main__":
    #创建对象
    game = PlaneGame()
    game.start_game()