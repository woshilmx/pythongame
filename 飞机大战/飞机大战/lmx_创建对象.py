import pygame
from plane_sprite import *
pygame.init()
#创建屏幕对象
screen = pygame.display.set_mode((1000,700))
hero = pygame.Rect(500,350,120,100)
#绘制背景图像
# #1>加载图片到内存
bg = pygame.image.load("E:\飞机大战\images\\background.png")
# #2>绘制图像到合适位置
screen.blit(bg,(0,0))
feiji = pygame.image.load("E:\飞机大战\images\\me1.png")
screen.blit(feiji,hero)
#3>刷新屏幕

clock = pygame.time.Clock()



#创建敌机对象
plan = Gamesprite("E:\飞机大战\images\enemy2.png")
ex = pygame.sprite.Group(plan)
while True:
    #监听事件的操作,固定的套路
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            print("游戏已结束")
            pygame.quit()
            exit()
    if hero.y < -120:
        hero.y = 1000
    clock.tick(60)
    hero.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(feiji, hero)


    #敌机的创建
    ex.update()
    ex.draw(screen)
    pygame.display.update()


pygame.quit()