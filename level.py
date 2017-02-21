import pygame
from globals import TILE_SIZE, TILE_WIDTH, TILE_HEIGHT, COLOR


walls = pygame.sprite.Group()
platforms = pygame.sprite.Group()


class Level(pygame.sprite.Group):

    def __init__(self):
        super(Level, self).__init__()
        self.current = None
        self.size = None
        self.image = None
        self.tiles = {
            'all': pygame.sprite.Group(),
            'wall': pygame.sprite.Group(),
            'platform': pygame.sprite.Group(),
        }

    def load_level(self, level):
        self.current = level
        self.size = (TILE_WIDTH * len(level[0]), TILE_HEIGHT * len(level))
        self.image = pygame.Surface(self.size)

        tile_image = pygame.Surface(TILE_SIZE)
        tile_image.fill(COLOR['white'])
        for y, row in enumerate(level):
            for x, kind in enumerate(row):
                position = (x * TILE_WIDTH, y * TILE_HEIGHT)
                if kind == 'W':
                    tile = Tile(position, kind=kind, groups=(self.tiles['all'], self.tiles['wall']))
                elif kind == 'P':
                    tile = Tile(position, kind=kind, groups=(self.tiles['all'], self.tiles['platform']))
                else:
                    tile = Tile(position, color='white')
                self.image.blit(tile.image, tile.rect)


class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, color='black', kind=None, groups=()):
        super(Tile, self).__init__(groups)
        self.rect = pygame.Rect(pos, TILE_SIZE)
        self.image = pygame.Surface(TILE_SIZE)
        self.image.fill(COLOR[color])
        self.kind = kind


LEVEL = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W                                              W',
    'W                                              W',
    'W                                              W',
    'W    PPP                    PPP                W',
    'W                                              W',
    'W                                              W',
    'W                                              W',
    'W                PPPPPP               PPPPPP   W',
    'W                                              W',
    'W                                              W',
    'W                                              W',
    'W     PPPPPP                 PPPPPP            W',
    'W                                              W',
    'W                                              W',
    'W               PPP                    PPP     W',
    'W                                              W',
    'W    PPP                    PPP                W',
    'W                                              W',
    'W                                              W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
]

MAPPING = {
    ' ': 0,
    'W': 1,
    'P': 2
}
