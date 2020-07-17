import  pygame
from plane_sprites import GameSprite

pygame.init()

"""
创建游戏的窗口 480×700
"""
screen = pygame.display.set_mode((480,700))

"""
绘制背景图像
"""
# 1. 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2. blit绘制图像
screen.blit(bg,(0,0))
# 3. update 进行刷帧操作
pygame.display.update()

"""
创建时钟对象
"""
clock = pygame.time.Clock()

"""
绘制英雄的飞机
"""
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))



"""
定义rect记录飞机的初始位置
"""
hero_rect = pygame.Rect(150,300,102,126)


"""
创建敌机的精灵
"""
enemy = GameSprite("./images/enemy1_down1.png")
enemy2 = GameSprite("./images/enemy1_down1.png",2)


"""
创建敌机的精灵组
"""
enemy_group = pygame.sprite.Group(enemy,enemy2)


"""
游戏循环
"""
while True:
    clock.tick(60)

    """
    捕获事件
    """
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")

            pygame.quit()
            exit()



    hero_rect.y -=1
    if  hero_rect.y < 1 :
        hero_rect.y = 700

    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    """
    精灵组调用方法
    """
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
