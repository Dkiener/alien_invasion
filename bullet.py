"""

Bullet

David Kiener
07-27-2025

Defines the laser projectile fired by the player's ship. Handles movement and rendering.

"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion') -> None:
        super().__init__()
        # Reference to screen and settings
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale the bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Position bullet at the top of the ship
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Store y-position as float for smooth movement
        self.y = float(self.rect.y)

    def update(self) -> None:
        # Move bullet upward based on speed
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        # Draw bullet to the screen
        self.screen.blit(self.image, self.rect)
