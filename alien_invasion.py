"""

Alien Invasion Game

David Kiener
07-20-2025

A Galaga-type game made using Star Wars fighters.

"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep
from button import Button

class AlienInvasion:

    def __init__(self) -> None:
        # Initialize the game and set up resources
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        # Set up screen and window caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        # Load and scale background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
            )

        self.running = True
        self.clock = pygame.time.Clock()

        # Load sounds and set volume
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(self.settings.laser_volume)
        
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(self.settings.impact_volume)

        # Create the ship, alien fleet, and play button
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, 'Play')
        self.game_active = False

    def run_game(self) -> None:
        # Main game loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        # Check for collisions between ship and aliens
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        # Check if any alien has reached the bottom of the screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        # Check for bullet-alien collisions
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        # If all aliens destroyed, reset level
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _check_game_status(self):
        # Handle losing a ship or ending the game
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        # Reset bullets and aliens for a new level
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _restart_game(self):
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(True)

    def _update_screen(self):
        # Redraw everything on the screen
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        # Handle user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self._restart_game()

    def _check_keyup_events(self, event) -> None:
        # Handle key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
    def _check_keydown_events(self, event) -> None:
        # Handle key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # Fire bullet if spacebar is pressed
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(500)
        elif event.key == pygame.K_q:
            # Quit the game if Q is pressed
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    # Run the game if file is executed directly
    ai = AlienInvasion()
    ai.run_game()
