"""

Button

David Kiener
07-27-2025

Defines a clickable button with text used to start or restart the game.

"""

import pygame.font
from typing import TYPE_CHECKING

class Button:

    if TYPE_CHECKING:
        from alien_invasion import AlienInvasion

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        # Reference to game settings and display
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Font used for the button label
        self.font = pygame.font.Font(
            self.settings.button_font_file, self.settings.button_font_size
        )

        # Define the button’s rectangle and center it
        self.rect = pygame.Rect(
            0, 0, self.settings.button_w, self.settings.button_h
        )
        self.rect.center = self.boundaries.center

        # Prepare the button label
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Render the text image and center it on the button
        self.msg_image = self.font.render(msg, True, self.settings.button_text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        # Draw the button with text on the screen
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        # Return True if the given position collides with the button
        return self.rect.collidepoint(mouse_pos)
