import pygame.font


class Scoreboard:
    """Render scoring, high score, level, and remaining ships."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (226, 244, 240)
        self.accent = (255, 211, 105)
        self.font = pygame.font.SysFont(None, 32)
        self.small_font = pygame.font.SysFont(None, 26)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}".replace(",", " ")
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 24
        self.score_rect.top = 16

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"Best: {high_score:,}".replace(",", " ")
        self.high_score_image = self.font.render(high_score_str, True, self.accent)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 16

    def prep_level(self):
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 24
        self.level_rect.top = self.score_rect.bottom + 6

    def prep_ships(self):
        ships_str = f"Ships: {self.stats.ships_left}"
        self.ships_image = self.small_font.render(ships_str, True, self.text_color)
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.left = 24
        self.ships_rect.top = 18

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_image, self.ships_rect)
