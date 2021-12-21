import pygame
import random
#屏幕尺寸大小常量
SCREEN_BACK = pygame.Rect(0,0,1000,700)
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        pygame.display.update()
#背景类
class Backgroud(Gamesprite):
    def __init__(self,is_alt=False):
        super().__init__("E:\飞机大战\images\\background.png")
        self.speed = 3
        if is_alt == True:
            self.rect.y = -self.rect.height


    def update(self):
        #调用父类的方法
        super().update()
        #判断图片是否滑出平屏幕
        if self.rect.y > SCREEN_BACK.height:
            self.rect.y = -SCREEN_BACK.height


class Enamy(Gamesprite):
    def __init__(self):
        super().__init__("E:\飞机大战\images\enemy1.png")
        #设置随机速度
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0,(SCREEN_BACK.width-self.rect.width))
    def update(self):
        super().update()
        if self.rect.y > SCREEN_BACK.height:
            self.kill()


class Hero(Gamesprite):
    """英雄"""
    def __init__(self):
        super().__init__("E:\飞机大战\images\me1.png")
        self.speed = 0
        self.rect.centerx = SCREEN_BACK.centerx
        self.rect.bottom = 570
        self.bullt_group = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.x <0:
            self.rect.x=0
        elif self.rect.right >SCREEN_BACK.right:
            self.rect.right  = SCREEN_BACK.right
    def fire(self):
        #设置子弹的位置
        for i in (0,1,2):
            bullt = Bullet()
            bullt.rect.bottom = self.rect.y -i*30
            bullt.rect.centerx = self.rect.centerx
            self.bullt_group.add(bullt)




class Bullet(Gamesprite):
    def __init__(self):
        super().__init__("E:\飞机大战\images\\bullet1.png",-4)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()



