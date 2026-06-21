import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A player-controlled ship."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = self._build_image()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 18

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def _build_image(self):
        image = pygame.Surface((66, 54), pygame.SRCALPHA)
        hull = (119, 224, 220)
        shadow = (34, 88, 105)
        flame = (255, 119, 80)
        glass = (193, 255, 246)

        pygame.draw.polygon(image, shadow, [(6, 40), (33, 6), (60, 40), (33, 48)])
        pygame.draw.polygon(image, hull, [(10, 37), (33, 4), (56, 37), (33, 45)])
        pygame.draw.polygon(image, (78, 176, 181), [(0, 48), (25, 31), (25, 48)])
        pygame.draw.polygon(image, (78, 176, 181), [(66, 48), (41, 31), (41, 48)])
        pygame.draw.ellipse(image, glass, (24, 16, 18, 12))
        pygame.draw.rect(image, flame, (27, 45, 12, 8), border_radius=2)
        pygame.draw.line(image, (238, 255, 247), (33, 7), (33, 43), 2)
        return image

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 18
        self.x = float(self.rect.x)
