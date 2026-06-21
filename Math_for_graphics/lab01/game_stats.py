import json
from pathlib import Path


class GameStats:
    """Track current session stats and persistent high score."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score_file = Path("high_score.json")
        self.high_score = self._load_high_score()
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _load_high_score(self):
        if not self.high_score_file.exists():
            return 0

        try:
            data = json.loads(self.high_score_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return 0

        return int(data.get("high_score", 0))

    def save_high_score(self):
        payload = {"high_score": int(self.high_score)}
        self.high_score_file.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
