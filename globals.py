import pygame
pygame.init()


TILE = {'SIZE': (32, 32), 'WIDTH': 32, 'HEIGHT': 32}
SCREEN = {'SIZE': (TILE['WIDTH'] * 25, TILE['HEIGHT'] * 14), 'WIDTH': TILE['WIDTH'] * 25, 'HEIGHT': TILE['HEIGHT'] * 14}


TILE_SIZE = TILE_WIDTH, TILE_HEIGHT = 32, 32
SIZE = WIDTH, HEIGHT = 25 * 32, 14 * 32
COLOR = pygame.color.THECOLORS
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
FPS = 60

GRAVITY = 0.35

FONT = {
    'scene': pygame.font.SysFont('monospace', 64)
}
