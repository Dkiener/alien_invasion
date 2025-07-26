"""

Arsenal

David Kiener
07-20-2025

Contains class to handle ship weapons.

"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        # Reference to main game, settings, and screen
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        # Group to store all active bullets
        self.arsenal = pygame.sprite.Group()

    def update_aresnal(self) -> None:
        # Update position of bullets and remove offscreen ones
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        # Remove bullets that have moved off the top of the screen
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        # Draw each bullet in the arsenal
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        # Fire a bullet if under bullet limit
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
