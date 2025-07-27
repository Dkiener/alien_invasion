"""

Alien Invasion Settings

David Kiener
07-20-2025

This file contains settings for the Alien Invasion game.

"""

from pathlib import Path

class Settings:
    def __init__(self) -> None:

        # Game Settings:
        
        # Name of game
        self.name: str = 'Alien Invasion'
        # Screen dimensions
        self.screen_w = 1200
        self.screen_h = 800
        # Frames per second
        self.FPS = 60
        # Background image
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'bg.png'
        # High scores file
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # The amount multiplied to increase difficulty per level
        self.difficulty_scale = 1.1

        # Ship Settings:

        # Ship sprite
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'xWing.png'
        # Ship dimensions
        self.ship_w = 60
        self.ship_h = 70

        # Bullet Settings:

        # Bullet sprite
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBolt.png'
        # Bullet sound
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'blaster.mp3'
        # Impact Sound
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'tieExplosion.mp3'
        # Bullet sound volume
        self.laser_volume = 0.7
        # Impact sound volume
        self.impact_volume = 0.5

        # Alien Settings:

        # Alien sprite
        self.alien_file = Path.cwd() / 'Assets' / 'Images' / 'tieFighter.png'
        # Alien dimensions
        self.alien_w = 40
        self.alien_h = 40
        # Starting direction of the alien fleet (1 for right -1 for left)
        self.fleet_direction = 1

        # Start Button Settings:

        # Button dimensions
        self.button_w = 200
        self.button_h = 50
        # Button color
        self.button_color = (27, 36, 230)
        # Button text size
        self.button_font_size = 48
        # Button text color
        self.button_text_color = (255, 255, 255)
        # Button font file
        self.button_font_file = Path.cwd() / 'Assets' / 'Fonts' / 'StarJedi' / 'StarJedi.ttf'
        
        # HUD Settings:

        # HUD text color
        self.HUD_text_color = (255, 255, 255)
        # HUD font size
        self.HUD_font_size = 24
         # HUD font file
        self.HUD_font_file = Path.cwd() / 'Assets' / 'Fonts' / 'StarJedi' / 'StarJedi.ttf'

    def initialize_dynamic_settings(self):
        # Dynamic Ship Settings:

        # Ship movement speed
        self.ship_speed = 5
        # Starting ship count (lives)
        self.starting_ship_count = 3

        # Dynamic Bullet Settings:

        # Bullet speed
        self.bullet_speed = 7
        # Max number of bullets allowed on the screen at once
        self.bullet_amount = 5
        # Bullet dimensions
        self.bullet_w = 80
        self.bullet_h = 80

        # Dynamic Alien Settings:

        # Alien fleet x movement speed
        self.fleet_speed = 2
        # Alien fleet y movement speed
        self.fleet_drop_speed = 40
        # Number of points recieved when alien ship is destroyed
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale