from pathlib import Path
class Settings:
    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'bg.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'xwing.png'
        self.ship_w = 60
        self.ship_h = 70
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBolt.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'blaster.mp3'
        self.laser_volume = 0.7
        self.bullet_speed = 7
        self.bullet_w = 80
        self.bullet_h = 80
        self.bullet_amount = 5