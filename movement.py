import pygame

class Character(pygame.sprite.Sprite):

    """
    class to add simple movement for all character in the game
    """

    def __init__(self, x, y, scale, speed):
        self.speed = speed
        img = pygame.image.load("")
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale),
                                                      int(img.get_height() * scale)))
        self.rect = img.get_rect()
        self.rect.center = (x, y)

    def 


