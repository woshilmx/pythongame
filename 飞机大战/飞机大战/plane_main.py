import pygame
from plane_sprite import *
pygame.init()
#屏幕尺寸大小常量
SCREEN_BACK = pygame.Rect(0,0,1000,700)
#敌机定时器常量
CHANGE_TIME_EVENT = pygame.USEREVENT
#子弹定时器常量
HERO_TIME_EVENT = pygame.USEREVENT + 1


class Plangame:
    #游戏初始化
    def __init__(self):
        #设置屏幕大小
        self.screen = pygame.display.set_mode(SCREEN_BACK.size)
        #创建时钟对象
        self.clock = pygame.time.Clock()
        #创建精灵，精灵族
        self.__creat_sprits()
        #设置定时器,1秒
        pygame.time.set_timer(CHANGE_TIME_EVENT,100)
        pygame.time.set_timer(HERO_TIME_EVENT,300)



    def __creat_sprits(self):
        """创建精灵和精灵组"""
        #创建背景精灵，组
        bg1 = Backgroud()
        bg2 = Backgroud(True)
        self.sprite_group = pygame.sprite.Group(bg1,bg2)
        #创建敌机精灵组

        self.enamy_group = pygame.sprite.Group()
        #创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)



    def start_game(self):
        while True:
        #游戏循环的
        #帧率
            self.clock.tick(60)
        #事件监听
            self.__event_check()
        #碰撞检测
            self.__check_peng()
        #精灵组刷新和绘制
            self.__update_draw()
        #屏幕刷新
            pygame.display.update()
            pass
    def __event_check(self):
        '''事件监听'''
        for p in pygame.event.get():
            if p.type == pygame.QUIT:
                self.__game_over()
            elif p.type == CHANGE_TIME_EVENT:
                enay= Enamy()
                self.enamy_group.add(enay)
            elif p.type ==HERO_TIME_EVENT:
                self.hero.fire()
            key_passdown = pygame.key.get_pressed()
            if key_passdown[pygame.K_RIGHT]:
                self.hero.speed = 7
            elif key_passdown[pygame.K_LEFT]:
                self.hero.speed = -7
            else:
                self.hero.speed = 0





    def __check_peng(self):
        '''碰撞检测'''
        #1.子弹摧毁敌机、
        pygame.sprite.groupcollide(self.hero.bullt_group,self.enamy_group,True,True)
        #2.敌机摧毁英雄
        list = pygame.sprite.spritecollide(self.hero,self.enamy_group,True)
        if len(list)>0:
            self.hero.kill()
            self.__game_over()

    def __update_draw(self):
        '''绘制刷新'''
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)
        #敌机
        self.enamy_group.update()
        self.enamy_group.draw(self.screen)
        #英雄
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        #子弹
        self.hero.bullt_group.update()
        self.hero.bullt_group.draw(self.screen)




    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    plane = Plangame()
    plane.start_game()
