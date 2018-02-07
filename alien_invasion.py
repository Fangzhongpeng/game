

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import  game_functions as gf
def run_game():
       pygame.init()
       ai_settings = Settings()
       screen = pygame.display.set_mode(
                     (ai_settings.screen_width ,ai_settings.screen_height))
       pygame.display.set_caption("you need python")
       stats = GameStats(ai_settings)
       ship = Ship(ai_settings,screen)
       #创建一个用于存储子弹的编组
       bullets = Group()
       aliens = Group()
       #创建外星人群
       gf.create_fleet(ai_settings,screen,ship,aliens)
       #开始游戏主循环
       while True:
               gf.check_events(ai_settings,screen,ship,bullets)
               if stats.game_active:
                       ship.update()
                       gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
                       gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
                       gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()

