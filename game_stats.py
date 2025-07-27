"""

Game Stats

David Kiener
07-27-2025

Tracks and manages game state values including score, level, remaining lives,
and persistent high scores.

"""

from typing import TYPE_CHECKING
import json

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    """Tracks game statistics including lives, scores, and levels."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize stats and load persistent hi-score."""
        # Reference to settings and game
        self.game = game
        self.settings = game.settings

        # Highest score seen across any session (non-resettable)
        self.max_score = 0

        # Load saved hi-score or create a new file
        self.init_saved_scores()

        # Stats that reset each session
        self.reset_stats()

    def init_saved_scores(self):
        """Read saved hi-score from disk or initialize it."""
        # Load hi-score from file if available; otherwise, save default
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """Write hi-score to file."""
        # Write hi-score to disk
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File not found: {e}")

    def reset_stats(self):
        """Reset dynamic stats for a new session."""
        # Reset dynamic stats for a new game session
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Update score and high scores after collisions."""
        # Process scoring and score-related updates
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """Update session max score."""
        # Update max score for the session
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """Update saved hi-score if beaten."""
        # Update and save hi-score if current score exceeds it
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()

    def _update_score(self, collisions):
        """Increase score based on number of collisions."""
        # Update score based on number of collisions
        for _ in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        """Advance to the next level."""
        # Increment level counter
        self.level += 1
