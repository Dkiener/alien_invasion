"""

Ship

David Kiener
07-27-2025

Defines the player-controlled ship, including movement, firing, and collision behavior.

"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        # Reference to game, settings, and screen
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        # Get rect and center ship at the start
        self.rect = self.image.get_rect()
        self._center_ship()

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Bullet manager for this ship
        self.arsenal = arsenal

    def _center_ship(self):
        # Position the ship at the bottom center of the screen
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)  # Use float for sub-pixel accuracy

    def update(self):
        # Update ship position and bullets
        self._update_ship_movement()
        self.arsenal.update_aresnal()

    def _update_ship_movement(self):
        # Move ship within screen bounds based on input
        speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += speed

        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= speed

        self.rect.x = int(self.x)

    def draw(self) -> None:
        # Draw bullets first, then the ship
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        # Fire a bullet using the arsenal
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group) -> bool:
        # Check for collision with any sprite in other_group
        if pygame.sprite.spritecollideany(self, other_group):  # type: ignore
            self._center_ship()  # Reset position if hit
            return True
        return False
