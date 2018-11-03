

class Settings():
    '''存储飞机大战所有的设置选项'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #设置飞船的速度
        self.ship_speed_factor = 1.5
        '''通过将速度设置为制定小数值,可在后面加快游戏节奏更细致控制飞船速度'''

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        
        