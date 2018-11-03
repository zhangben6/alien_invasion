import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        #初始化飞船并设置初始位置
        self.screen = screen

        self.image = pygame.image.load("./images/ship.bmp")
        # 根据图片已经获取到飞船rect属性
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 移动到屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船移动的标志位
        self.move_right = False
        self.move_left = False

        #飞机的速度设置对象实例
        self.ai_settings = ai_settings

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)



    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        # 更新飞船的center值,而不是rect
        if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx -=1
            self.center += self.ai_settings.ship_speed_factor
        elif self.move_left and self.rect.left > 0 :
            # self.rect.centerx -=1
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.centerx更新rect对象
        self.rect.centerx = self.center
    