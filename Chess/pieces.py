import pygame


class Piece:
    def __init__(self, color, x, y, piece_type):
        self.color = color
        self.x = x
        self.y = y
        self.type = piece_type
        self.pos = (x, y)

    def draw(self, surface):
        img = pygame.image.load(f"images/{self.color}_{self.type}.png")
        surface.blit(img, (self.x * 75 + 10, self.y * 75 + 10))

