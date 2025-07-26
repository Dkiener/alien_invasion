"""

Alien Fleet

David Kiener
07-20-2025

Contains class to handle player ship.

"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        # Reference to the game instance, settings, and screen
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        # Get rectangle for positioning and center the ship
        self.rect = self.image.get_rect()
        self._center_ship()

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Arsenal for handling bullets fired from the ship
        self.arsenal = arsenal

    def _center_ship(self):
        # Position the ship at the bottom center of the screen
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)  # Use float for smoother movement

    def update(self):
        # Update ship position and update bullets
        self._update_ship_movement()
        self.arsenal.update_aresnal()

    def _update_ship_movement(self):
        # Move the ship left or right, respecting screen boundaries
        speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += speed

        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= speed

        self.rect.x = int(self.x)

    def draw(self) -> None:
        # Draw bullets and the ship
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        # Attempt to fire a bullet
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group) -> bool:
        # Check if the ship has collided with any sprite in the other group
        if pygame.sprite.spritecollideany(self, other_group): # type: ignore
            self._center_ship()  # Re-center the ship on collision
            return True
        return False
