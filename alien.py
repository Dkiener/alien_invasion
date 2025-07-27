"""

Alien

David Kiener  
07-27-2025

Defines a single enemy unit, including its position, movement, and rendering.

"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A single alien enemy unit in the fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initialize alien position and load its image."""
        super().__init__()

        # Reference to fleet, screen, and settings
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load and scale the alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )

        # Set initial rectangle position
        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

        # Use float for smooth movement tracking
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Update the alien's horizontal position."""
        # Move alien horizontally based on fleet speed and direction
        speed = self.settings.fleet_speed
        self.x += speed * self.fleet.fleet_direction
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def check_edges(self) -> bool:
        """Return True if alien hits left or right screen edge."""
        # Return True if alien has hit the screen edge
        return (
            self.rect.right >= self.boundaries.right
            or self.rect.left <= self.boundaries.left
        )

    def draw_alien(self) -> None:
        """Draw the alien to the screen."""
        # Draw alien to the screen
        self.screen.blit(self.image, self.rect)
