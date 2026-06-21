import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """One alien in the fleet."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = self._build_image()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def _build_image(self):
        image = pygame.Surface((56, 38), pygame.SRCALPHA)
        body = (123, 214, 190)
        dome = (186, 248, 226)
        shade = (42, 111, 124)
        light = (255, 138, 100)

        pygame.draw.ellipse(image, shade, (5, 13, 46, 19))
        pygame.draw.ellipse(image, body, (4, 10, 48, 20))
        pygame.draw.ellipse(image, dome, (17, 3, 22, 18))
        pygame.draw.rect(image, shade, (9, 22, 38, 6), border_radius=3)
        for x in (14, 25, 36):
            pygame.draw.circle(image, light, (x, 25), 3)
        pygame.draw.line(image, body, (13, 31), (9, 37), 3)
        pygame.draw.line(image, body, (43, 31), (47, 37), 3)
        return image

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = int(self.x)
