"""

Alien Fleet

David Kiener
07-20-2025

Contains class to handle Alien Fleet.

"""

import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        # Calculate how many aliens fit and where to position the fleet
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        # Create the alien fleet in staggered formation
        self._create_staggered_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        # Creates a grid of aliens, skipping even rows and columns for a sparse formation
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                curreny_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, curreny_y)

    def _create_staggered_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        # Creates a staggered (zig-zag) pattern for the alien fleet
        columns = fleet_w // 2
        rows = fleet_h // 2

        for row in range(rows):
            for col in range(columns):
                # Shift odd rows right by half an alien width
                offset_x = alien_w // 2 if row % 2 == 1 else 0
                current_x = col * alien_w * 2 + offset_x + x_offset
                current_y = row * alien_h * 2 + y_offset
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        # Center the fleet horizontally and vertically (upper half of screen)
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        # Calculate how many aliens can fit on the screen (minus a little for borders)
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2) // alien_h)

        # Make dimensions odd and slightly smaller for better centering
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x: int, current_y: int):
        # Create a single alien at given coordinates and add to fleet group
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        # Reverse fleet direction and drop when any alien hits screen edge
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        # Move the entire fleet down
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self) -> None:
        # Update fleet position and direction
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self) -> None:
        # Draw each alien in the fleet
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        # Check and handle collisions with another group (e.g., bullets)
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        # Return True if any alien reaches bottom of screen
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        # Return True if all aliens have been destroyed
        return not self.fleet
