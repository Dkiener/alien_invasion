"""

Alien

David Kiener
07-20-2025

Contains class to handle individual Aliens.

"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        super().__init__()
        # Reference to the fleet this alien belongs to
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load and scale the alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        # Set position of the alien
        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

        # Store position as floats for precise movement
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        # Move the alien horizontally based on fleet speed and direction
        speed = self.settings.fleet_speed

        self.x += speed * self.fleet.fleet_direction
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def check_edges(self) -> bool:
        # Return True if alien has hit the edge of the screen
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self) -> None:
        # Draw the alien to the screen
        self.screen.blit(self.image, self.rect)
