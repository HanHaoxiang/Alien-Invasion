# 调用库
import pygame.font
from pygame.sprite import Group
# 自己的文件
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备包含得分的初始图像
        self.prep_images()


    def prep_score(self):
        """将得分转换为渲染的图像"""
        #第二个参数控制小数点后多少位，如果为负数，则将目标圆整到最近的10，100...
        #python 2.7中，round()总是返回小数数值，如果是python3，可以省略int()
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        score_str = 'Score : ' + score_str
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        high_score_str = "High Score : " + high_score_str
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        
        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_imgae = self.font.render("Level : " + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        
        # 将等级放在得分下方
        self.level_rect = self.level_imgae.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def prep_images(self):
        # 准备包含得分的初始图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def show_score(self):
        """在屏幕上显示飞船和得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_imgae, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)