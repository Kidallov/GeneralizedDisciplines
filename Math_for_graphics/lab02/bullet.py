import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A bullet fired from the ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.power = ai_game.stats.power_active(pygame.time.get_ticks())
        self.hits_left = self.settings.power_bullet_hits if self.power else 1
        self.color = (103, 206, 255) if self.power else self.settings.bullet_color
        width = self.settings.power_bullet_width if self.power else self.settings.bullet_width

        self.rect = pygame.Rect(
            0,
            0,
            width,
            self.settings.bullet_height,
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=2)
