import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal
class Ship:
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self):
        # Updating the pos of the ship
        self._update_ship_movement()
        self.arsenal.update_aresenal()

    def _update_ship_movement(self):
        speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= speed

        # I get an error here when attempting to assign a float to an int
        # I casted it to an int instead
        self.rect.x = int(self.x)

    def draw(self) ->None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        return self.arsenal.fire_bullet()