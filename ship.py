import pygame

class Ship:
    def __init__(self, screen):
        """Initialize the ship and set its starting point"""
        self.screen = screen

        self.moving_right = False
        self.moving_left = False

        #load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship.png').convert_alpha()

        #resize the ship
        self.image = pygame.transform.scale(self.image, (600, 500))

        #get the ship's rectangle
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ update the ship's position based on movement flags"""
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.rect.centerx += 1.5

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1.5
            