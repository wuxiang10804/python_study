import pygame
from  scoreboard import Scoreboard
from  plane_sprites import *
from gamestats import GameStates

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

        #创建游戏状态
        self.stats = GameStates()

        #创建分数
        self.scoreboard = Scoreboard(self.screen,self.stats)


        #设置定时器事件 创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        """
        创建背景精灵和精灵组
        """
        bg1 = Background()
        bg2 = Background(True)
    
        self.back_group = pygame.sprite.Group(bg1,bg2)
        
        """
        创建敌机的精灵组
        """
        self.enemy_group = pygame.sprite.Group()


        """
        创建英雄的精灵和精灵组
        """
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

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

            self.scoreboard.show_score()
            # 更新显示
            pygame.display.update()
            
    
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('敌机出来了')
                #创建敌机精灵
                enemy = Enemy()
                #添加到敌机精灵组
                self.enemy_group.add(enemy)
            #elif event.type == pygame.KEYDOWN and  event.key == pygame.K_RIGHT:
            #    pass   
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            
        #使用键盘提供的方法获取键盘按键
        keys_pressed = pygame.key.get_pressed()     
        #判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT] :
            print("英雄向右移动...")
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed_y = -2
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed_y = 2
        else :
            self.hero.speed = 0
            self.hero.speed_y = 0



    def __check_collide(self):
        # 子弹摧毁敌机
        conllisions = pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        if conllisions :
            print("len conllisions = %d" % len(conllisions))
            self.stats.score += len(conllisions) * POINT
            self.scoreboard.update_score(self.stats)


            for first , second  in conllisions.items() :
                print("first = %s " % first)
                print("second = %s " % second)


        #敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        #判断列表是否有内容
        if len(enemies) > 0:
            print("len(enemies)== %d \n" %  len(enemies))
            print("%s " % enemies)
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == "__main__":

    pygame.init()
    #创建对象
    game = PlaneGame()
    game.start_game()