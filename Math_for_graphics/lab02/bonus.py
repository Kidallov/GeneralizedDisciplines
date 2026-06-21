import random

import pygame
from pygame.sprite import Sprite


class Bonus(Sprite):
    """A falling collectible that changes the current run."""

    TYPES = ("life", "shield", "power")

    def __init__(self, ai_game, center):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.kind = random.choices(self.TYPES, weights=(2, 3, 3), k=1)[0]

        self.image = self._build_image()
        self.rect = self.image.get_rect(center=center)
        self.y = float(self.rect.y)

    def _build_image(self):
        image = pygame.Surface(
            (self.settings.bonus_width, self.settings.bonus_height),
            pygame.SRCALPHA,
        )
        palette = {
            "life": ((255, 119, 120), (255, 228, 228)),
            "shield": ((103, 206, 255), (221, 248, 255)),
            "power": ((255, 211, 105), (255, 246, 192)),
        }
        main, light = palette[self.kind]

        pygame.draw.circle(image, main, (15, 15), 14)
        pygame.draw.circle(image, light, (15, 15), 10)
        pygame.draw.circle(image, (8, 11, 24), (15, 15), 14, width=2)

        if self.kind == "life":
            pygame.draw.rect(image, main, (13, 7, 4, 16), border_radius=1)
            pygame.draw.rect(image, main, (7, 13, 16, 4), border_radius=1)
        elif self.kind == "shield":
            pygame.draw.polygon(image, main, [(15, 6), (23, 10), (21, 21), (15, 25), (9, 21), (7, 10)])
        else:
            pygame.draw.polygon(image, main, [(15, 5), (21, 14), (17, 14), (21, 25), (9, 12), (14, 13)])

        return image

    def update(self):
        self.y += self.settings.bonus_speed
        self.rect.y = int(self.y)
