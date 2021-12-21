import pygame
import random
#设置屏幕常量
SCREEN_SIZE = pygame.Rect(0,0,700,700)
#设置贪吃蛇常量
SNAKE_SIZE = pygame.Rect(350,350,20,20)

#定义屏幕大小，时钟变量
screen = pygame.display.set_mode(SCREEN_SIZE.size)
title = pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()
#设置贪吃蛇类
class snake(object):
    def __init__(self,speed = 1):
        self.color = (0,0,255)
        self.snake_size = SNAKE_SIZE
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.snake_size)
    def copy(self,point):
        self.snake_size = point.snake_size

class food(object):
    def __init__(self):
        self.color = (255,255,0)
        self.food_size = pygame.Rect(random.randint(0,SCREEN_SIZE.width),random.randint(0,SCREEN_SIZE.height),20,20)
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.food_size)

def creat_food(food):
    return food()

def game_over():
    print("游戏结束")
    pygame.quit()
    exit()

def event_check(point):
    '''事件监听'''
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
          game_over()


snake_list = []
point = snake()
snake_list.append(point)
food1 = food()
while True:
    #设置帧率
    clock.tick(60)
    #事件监听
    event_check(point)
    key_passdown = pygame.key.get_pressed()
    if key_passdown[pygame.K_RIGHT]:
        point.snake_size.x += 6
    elif key_passdown[pygame.K_LEFT]:
        point.snake_size.x -= 6
    elif key_passdown[pygame.K_UP]:
        point.snake_size.y -= 6
    elif key_passdown[pygame.K_DOWN]:
        point.snake_size.y += 6
    #碰撞检测
    if SNAKE_SIZE.x < 0 or SNAKE_SIZE.x > SCREEN_SIZE.width:
        game_over()
    elif SNAKE_SIZE.y < 0 or SNAKE_SIZE.y > SCREEN_SIZE.height:
       game_over()
    if point.snake_size == food1.food_size:
        pass
    #绘制
    背景图片的绘制
    pygame.draw.rect(screen, (255, 255, 255), SCREEN_SIZE)
    #
    #贪吃蛇的绘制
    point.draw(screen)
    food1.draw(screen)
    #屏幕刷新
    pygame.display.update()