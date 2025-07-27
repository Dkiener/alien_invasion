"""

Settings

David Kiener  
07-27-2025

This file contains settings for the Alien Invasion game.

"""

from pathlib import Path

class Settings:
    def __init__(self) -> None:

        # ====================
        # General Game Settings
        # ====================

        # Title of the game window
        self.name: str = 'Alien Invasion'

        # Dimensions of the game screen
        self.screen_w = 1200
        self.screen_h = 800

        # Frames per second
        self.FPS = 60

        # Background image file path
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'bg.png'

        # File path for saving high scores
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Scale factor for increasing difficulty each level
        self.difficulty_scale = 1.1

        # ==============
        # Ship Settings
        # ==============

        # File path to the ship image
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'xWing.png'

        # Ship dimensions
        self.ship_w = 60
        self.ship_h = 70

        # =================
        # Bullet Settings
        # =================

        # File path to bullet image
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBolt.png'

        # Sound file for firing bullets
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'blaster.mp3'

        # Sound file for bullet impact
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'tieExplosion.mp3'

        # Volume levels
        self.laser_volume = 0.7
        self.impact_volume = 0.5

        # =================
        # Alien Settings
        # =================

        # File path to alien image
        self.alien_file = Path.cwd() / 'Assets' / 'Images' / 'tieFighter.png'

        # Alien dimensions
        self.alien_w = 40
        self.alien_h = 40

        # Fleet direction (1 for right, -1 for left)
        self.fleet_direction = 1

        # ===================
        # Button UI Settings
        # ===================

        # Button dimensions
        self.button_w = 200
        self.button_h = 50

        # Button appearance
        self.button_color = (27, 36, 230)
        self.button_font_size = 48
        self.button_text_color = (255, 255, 255)

        # Button font file
        self.button_font_file = Path.cwd() / 'Assets' / 'Fonts' / 'StarJedi' / 'StarJedi.ttf'

        # ================
        # HUD Text Settings
        # ================

        # HUD text appearance
        self.HUD_text_color = (255, 255, 255)
        self.HUD_font_size = 24

        # HUD font file
        self.HUD_font_file = Path.cwd() / 'Assets' / 'Fonts' / 'StarJedi' / 'StarJedi.ttf'

    def initialize_dynamic_settings(self):
        # ======================
        # Dynamic Ship Settings
        # ======================

        # Ship movement speed
        self.ship_speed = 5

        # Number of lives at game start
        self.starting_ship_count = 3

        # ========================
        # Dynamic Bullet Settings
        # ========================

        # Bullet movement speed
        self.bullet_speed = 7

        # Maximum bullets allowed on screen
        self.bullet_amount = 5

        # Bullet dimensions
        self.bullet_w = 80
        self.bullet_h = 80

        # =======================
        # Dynamic Alien Settings
        # =======================

        # Horizontal fleet movement speed
        self.fleet_speed = 2

        # Vertical drop when changing direction
        self.fleet_drop_speed = 40

        # Score value per alien
        self.alien_points = 50

    def increase_difficulty(self):
        # Increase speeds to scale difficulty
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
