"""

HUD (Heads-Up Display)

David Kiener
07-27-2025

Displays game information such as score, level, lives remaining, and high scores.

"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:

    def __init__(self, game: 'AlienInvasion') -> None:
        # References to game, settings, screen, and statistics
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats

        # Font for text rendering
        self.font = pygame.font.Font(
            self.settings.HUD_font_file, self.settings.HUD_font_size
        )
        self.padding = 20

        # Initialize score, life image, and level display
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def update_scores(self):
        # Refresh all score displays
        self._update_max_score()
        self.update_score()
        self._update_hi_score()

    def _setup_life_image(self):
        # Load and scale ship image for life indicators
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image, (self.settings.ship_w / 2, self.settings.ship_h / 2)
        )
        self.life_rect = self.life_image.get_rect()

    def update_score(self):
        # Update current score text and position
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(
            score_str, True, self.settings.HUD_text_color, None
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        # Update max score text and position
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(
            max_score_str, True, self.settings.HUD_text_color, None
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        # Update hi-score text and position (all-time best)
        hi_score_str = f"Hi-Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(
            hi_score_str, True, self.settings.HUD_text_color, None
        )
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def _draw_lives(self):
        # Draw remaining ships as life icons in the bottom-left corner
        current_x = self.padding
        current_y = self.boundaries.bottom - self.life_rect.height - self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def update_level(self):
        # Update level text and position (moved to top-left)
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(
            level_str, True, self.settings.HUD_text_color, None
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.padding


    def draw(self):
        # Draw all HUD elements
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
