import pygame
import random
#设置屏幕常量
SCREEN_SIZE = pygame.Rect(0,0,700,700)
#贪吃蛇的常量
SNAKE_SIZE = pygame.Rect(350,350,20,20)
FOOD_SIZE = pygame.Rect(random.randint(0,SCREEN_SIZE.width),random.randint(0,SCREEN_SIZE.height),20,20)
#定义屏幕大小，时钟变量
screen = pygame.display.set_mode(SCREEN_SIZE.size)
title = pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()
def game_over():
    print("游戏结束")
    pygame.quit()
    exit()
def event_check():
    '''事件监听'''
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
          game_over()

while True:
    #设置帧率
    clock.tick(60)
    #事件监听
    event_check()
    key_passdown = pygame.key.get_pressed()
    if key_passdown[pygame.K_RIGHT]:
        SNAKE_SIZE.x += 7
    elif key_passdown[pygame.K_LEFT]:
        SNAKE_SIZE.x -= 7
    elif key_passdown[pygame.K_UP]:
        SNAKE_SIZE.y -= 7
    elif key_passdown[pygame.K_DOWN]:
        SNAKE_SIZE.y += 7
    #碰撞检测
    if SNAKE_SIZE.x < 0 or SNAKE_SIZE.x > SCREEN_SIZE.width:
        game_over()
    elif SNAKE_SIZE.y < 0 or SNAKE_SIZE.y > SCREEN_SIZE.height:
       game_over()

    if SNAKE_SIZE == FOOD_SIZE:
        pass

    #背景图片的绘制
    pygame.draw.rect(screen,(255,255,255),SCREEN_SIZE)
    #贪吃蛇的绘制
    pygame.draw.rect(screen,(0,0,255),SNAKE_SIZE)
    #食物的绘制
    pygame.draw.rect(screen,(255,255,0),FOOD_SIZE)
    pygame.display.flip()
    # 屏幕刷新
    pygame.display.update()
