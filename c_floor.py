import pygame


class Floor:
    color = 'green'

    def __init__(self, pos_x, pos_y):
        self.hitbox = pygame.Rect(pos_x, pos_y, 50, 50)

    def _draw(self, win):
        pygame.draw.rect(win, self.color, self.hitbox)

    def update(self, screen):
        self._draw(screen)
