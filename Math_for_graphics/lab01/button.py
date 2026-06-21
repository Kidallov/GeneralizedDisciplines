import pygame.font


class Button:
    """A clickable text button."""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 220
        self.height = 58
        self.button_color = (255, 119, 80)
        self.text_color = (8, 11, 24)
        self.font = pygame.font.SysFont(None, 42)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def set_text(self, msg):
        self._prep_msg(msg)

    def draw_button(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=8)
        pygame.draw.rect(self.screen, (255, 211, 105), self.rect, width=2, border_radius=8)
        self.screen.blit(self.msg_image, self.msg_image_rect)
