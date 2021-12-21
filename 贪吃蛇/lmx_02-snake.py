import pygame
import random
from pygame.locals import *
#设置屏幕常量
SCREEN_SIZE = pygame.Rect(0,0,600,600)
pygame.init()
#定义屏幕大小，时钟变量
screen = pygame.display.set_mode(SCREEN_SIZE.size)
title = pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()
def game_over():
    print("游戏结束")
    pygame.quit()
    exit()
#初始化蛇头的位置
snake_head = [100,100]
#初始化蛇身的位置
snake_body = [[80,100],[60,100],[40,100],[20,100]]
#初始化食物的位置
food_position = [120,120]
decrotion = K_RIGHT
foodflag = 1
if __name__ == '__main__':
    while True:
        #设置帧率
        clock.tick(10)
        #事件监听
        for p in pygame.event.get():
            if p.type == pygame.QUIT:
              game_over()
        #按键检测
        key_passdown = pygame.key.get_pressed()
        if key_passdown[pygame.K_RIGHT]:
                    decrotion = K_RIGHT

        elif key_passdown[pygame.K_LEFT]:
                    decrotion = K_LEFT

        elif key_passdown[pygame.K_UP]:
                    decrotion = K_UP

        elif key_passdown[pygame.K_DOWN]:
                    decrotion = K_DOWN

        if decrotion == K_RIGHT:
            snake_head[0] += 20
        elif decrotion == K_LEFT:
            snake_head[0] -= 20
        elif decrotion == K_UP:
            snake_head[1] -= 20
        elif decrotion == K_DOWN:
            snake_head[1] += 20
        snake_body.insert(0,list(snake_head))

        if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
                    foodflag = 0
        else:
                    snake_body.pop()

        if foodflag == 0:
            x = random.randint(1,29)
            y = random.randint(1,29)
            food_position = [int(x*20),int(y*20)]
        #碰撞检测
        if snake_head[0] > 600 or snake_head[0] < 0 or snake_head[1]>600 or snake_head[1]<0:
            game_over()
        title = len(snake_body)




        #背景图片的绘制
        pygame.draw.rect(screen, (255, 255, 255), SCREEN_SIZE)
        for i in snake_body:
            pygame.draw.rect(screen,(0,0,255),(i[0],i[1],20,20))
        pygame.draw.rect(screen,(250,250,0),(food_position[0],food_position[1],20,20))
        foodflag = 1
        pygame.display.flip()
        # 屏幕刷新
        pygame.display.update()