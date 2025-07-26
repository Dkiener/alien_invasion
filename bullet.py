"""

Alien Fleet

David Kiener
07-20-2025

Contains class to handle ship laser.

"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion') -> None:
        super().__init__()
        # Reference to game screen and settings
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Set bullet's initial position at the top-center of the ship
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)  # Store y-position as float for smooth movement

    def update(self) -> None:
        # Move the bullet upward
        self.y -= self.settings.bullet_speed
        # Convert y back to int for assigning to rect (required by Pygame)
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        # Draw the bullet to the screen
        self.screen.blit(self.image, self.rect)
