import random
import sys
from pathlib import Path

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from sound_effects import SoundEffects


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.sb = Scoreboard(self)
        self.play_button = Button(self, "PLAY")
        self.sounds = SoundEffects()
        self.stars = self._make_stars(130)

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(event.pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key in (pygame.K_p, pygame.K_RETURN):
            self._start_game()
        elif event.key == pygame.K_q:
            self._quit_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()

    def _start_game(self):
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if not self.stats.game_active:
            return
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))
            self.sounds.play("shoot")

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            aliens_destroyed = sum(len(aliens) for aliens in collisions.values())
            self.stats.score += self.settings.alien_points * aliens_destroyed
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sounds.play("hit")

        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self._create_fleet()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.time.delay(550)
        else:
            self.stats.ships_left = 0
            self.sb.prep_ships()
            self.stats.game_active = False
            self.stats.save_high_score()
            self.play_button.set_text("PLAY AGAIN")
            pygame.mouse.set_visible(True)
            self.sounds.play("game_over")

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x = alien_width
        current_y = alien_height + 36
        while current_y < (self.ship.rect.top - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        alien = Alien(self)
        alien.x = x_position
        alien.rect.x = x_position
        alien.rect.y = y_position
        self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_stars()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self._draw_title()
            self.play_button.draw_button()

        pygame.display.flip()

    def _draw_title(self):
        font = pygame.font.SysFont(None, 58)
        small_font = pygame.font.SysFont(None, 26)
        title = font.render("ALIEN INVASION", True, (226, 244, 240))
        hint = small_font.render(
            "Arrows move   Space shoots   P/Enter starts   Q quits",
            True,
            (155, 185, 190),
        )
        title_rect = title.get_rect(centerx=self.screen.get_rect().centerx, y=190)
        hint_rect = hint.get_rect(centerx=self.screen.get_rect().centerx, y=376)
        self.screen.blit(title, title_rect)
        self.screen.blit(hint, hint_rect)

    def _make_stars(self, count):
        stars = []
        for _ in range(count):
            stars.append(
                {
                    "x": random.randrange(0, self.settings.screen_width),
                    "y": random.randrange(0, self.settings.screen_height),
                    "speed": random.uniform(0.15, 0.75),
                    "size": random.choice((1, 1, 1, 2)),
                    "color": random.choice(
                        ((90, 117, 130), (140, 172, 174), (255, 211, 105))
                    ),
                }
            )
        return stars

    def _draw_stars(self):
        for star in self.stars:
            star["y"] += star["speed"]
            if star["y"] > self.settings.screen_height:
                star["x"] = random.randrange(0, self.settings.screen_width)
                star["y"] = 0
            pygame.draw.circle(
                self.screen,
                star["color"],
                (int(star["x"]), int(star["y"])),
                star["size"],
            )

    def _quit_game(self):
        if self.stats.score >= self.stats.high_score:
            self.stats.save_high_score()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent
    if Path.cwd() != project_root:
        print(f"Tip: run from {project_root}")
    ai = AlienInvasion()
    ai.run_game()
