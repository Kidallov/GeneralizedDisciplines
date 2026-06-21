import json
import pickle
from pathlib import Path


class GameStats:
    """Track current session stats and persistent high score."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score_file = Path("high_score.json")
        self.save_file = Path(self.settings.save_file)
        self.high_score = self._load_high_score()
        self.game_active = False
        self.status_message = ""
        self.status_message_until = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.shield_until = 0
        self.power_until = 0

    def shield_active(self, now=None):
        return (now or 0) < self.shield_until

    def power_active(self, now=None):
        return (now or 0) < self.power_until

    def set_status(self, message, now):
        self.status_message = message
        self.status_message_until = now + self.settings.status_message_duration

    def build_save_data(self, now):
        return {
            "score": int(self.score),
            "high_score": int(self.high_score),
            "level": int(self.level),
            "ships_left": int(self.ships_left),
            "shield_remaining": max(0, self.shield_until - now),
            "power_remaining": max(0, self.power_until - now),
        }

    def save_progress(self, now):
        with self.save_file.open("wb") as file:
            pickle.dump(self.build_save_data(now), file)

    def load_progress(self, now):
        with self.save_file.open("rb") as file:
            data = pickle.load(file)

        self.score = int(data.get("score", 0))
        self.high_score = max(self.high_score, int(data.get("high_score", 0)))
        self.level = max(1, int(data.get("level", 1)))
        self.ships_left = max(0, int(data.get("ships_left", self.settings.ship_limit)))
        self.shield_until = now + int(data.get("shield_remaining", 0))
        self.power_until = now + int(data.get("power_remaining", 0))

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
