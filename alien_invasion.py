import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏,并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, scoreboard)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, stats, scoreboard)
            gf.update_aliens(ai_settings, aliens, ship, stats, bullets, screen, scoreboard)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, scoreboard)

run_game()

