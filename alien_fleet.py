import pygame
from pygame.sprite import Group

from alien import Alien

def create_fleet(ai_settings, screen):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))

    alien_height = alien.rect.height
    available_space_y = ai_settings.screen_height - (3 * alien_height) 
    number_rows = int(available_space_y / (2 * alien_height))

    aliens = Group()
    
    # Create the full fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            alien = Alien(ai_settings, screen)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien_height * row_number
            aliens.add(alien)

    return aliens

    

def update_fleet(ai_settings, aliens):
    """move the entire fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """respond  if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, ship, aliens):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = ship.screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            return True
        
    return False