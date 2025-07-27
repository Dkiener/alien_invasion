"""

Alien Invasion Game

David Kiener
07-27-2025

A Galaga-type arcade shooter.
Manages game initialization, main loop, event handling, and screen updates.

"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:

    def __init__(self) -> None:
        # Initialize pygame and load settings
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        # Create the display surface
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Load and scale the background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        # Initialize game stats and HUD
        self.game_stats = GameStats(self)
        self.HUD = HUD(self)

        self.running = True
        self.clock = pygame.time.Clock()

        # Load sound effects and set volume
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(self.settings.laser_volume)
        
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(self.settings.impact_volume)

        # Load music and set volume
        pygame.mixer.music.load(self.settings.bg_music)
        pygame.mixer.music.set_volume(self.settings.music_volume)

        # Create game objects
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, 'Play')

        # Game starts in inactive state
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
        # Check ship-alien collisions
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        # Check if aliens reached the bottom
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        # Check bullet-alien collisions
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        # If all aliens are destroyed, start next level
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()

    def _check_game_status(self) -> None:
        # Lose a life or end game
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mixer.music.stop()

    def _reset_level(self) -> None:
        # Clear bullets and aliens, recreate fleet
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _restart_game(self) -> None:
        # Reset all dynamic settings and stats to start a new game
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.HUD.update_level()
        self.game_active = True
        pygame.mouse.set_visible(False)
        pygame.mixer.music.play(-1)


    def _update_screen(self) -> None:
        # Draw background and all game elements
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        # Draw play button if game inactive
        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self) -> None:
        # Handle keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        # Start game if play button clicked
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self._restart_game()

    def _check_keyup_events(self, event) -> None:
        # Stop moving the ship on key release
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event) -> None:
        # Handle ship movement and firing on key press
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(500)
        elif event.key == pygame.K_q:
            # Quit game with Q
            self.running = False
            self.game_stats.save_scores()
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    # Entry point: Start game
    ai = AlienInvasion()
    ai.run_game()
