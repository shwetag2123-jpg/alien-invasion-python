import sys

import pygame

import alien
from settings import Settings

from ship import Ship

from alien_fleet import create_fleet , update_fleet ,check_aliens_bottom

from bullet import Bullet

from game_stats import GameStats


pygame.init()
font = pygame.font.SysFont(None, 80)

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    game_stats = GameStats(ai_settings)

    ship = Ship(screen)

    aliens = create_fleet(ai_settings, screen)

    bullets = pygame.sprite.Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False


        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        if game_stats.game_active:

            ship.update() #update the ship's position based on movement flags
        
            update_fleet(ai_settings, aliens) #move the aliens

            if check_aliens_bottom(ai_settings, ship, aliens):
                game_stats.ships_left -= 1
                if game_stats.ships_left > 0:
                    aliens = create_fleet(ai_settings, screen)
                    bullets.empty()
                else:
                    game_stats.game_active = False
            aliens.draw(screen) #draw the aliens at their current location
            bullets.update() #update bullet positions
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

            if len(aliens) == 0:
                bullets.empty()
                aliens = create_fleet(ai_settings, screen)
            ship.blitme() #draw the ship at its current location

            for bullet in bullets.sprites():
                bullet.draw_bullet() #draw each bullet at its current location


            if not game_stats.game_active:
                game_over_text = font.render("GAME OVER!!!!", True, (0, 255, 0))
                text_rect = game_over_text.get_rect(center= screen.get_rect().center)
                screen.blit(game_over_text, text_rect)


            #make the most recently drawn screen visible.
            pygame.display.flip()

        

run_game()
