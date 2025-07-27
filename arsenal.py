"""

Arsenal

David Kiener
07-27-2025

Manages the player's active projectiles, including firing, updating, and removing off-screen bullets.

"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Manages a group of active bullets for the player's ship."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the bullet group and references."""
        # Reference to game settings and screen
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        # Group to store all active bullets
        self.arsenal = pygame.sprite.Group()

    def update_aresnal(self) -> None:
        """Update all bullets and remove off-screen ones."""
        # Update bullet positions and remove off-screen bullets
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Remove any bullets that have moved beyond the top edge."""
        # Remove bullets that have moved beyond the top edge of the screen
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draw all bullets to the screen."""
        # Draw all bullets in the arsenal to the screen
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire a new bullet if under the limit. Return True if successful."""
        # Fire a new bullet if under the allowed bullet limit
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
