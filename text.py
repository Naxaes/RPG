import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((13, 13, 13))
        self.image.set_colorkey((13, 13, 13))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("monospace", 18)

    def add(self, letter, pos):
        s = self.font.render(letter, 1, (255, 255, 0))
        self.image.blit(s, pos)


class Cursor(pygame.sprite.Sprite):
    def __init__(self, board):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.text_height = 17
        self.text_width = 10
        self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
        self.board = board
        self.text = []
        self.cooldown = 0
        self.cooldowns = {'.': 6, '[': 9, ']': 9, ' ': 3, '\n': 15}

    def write(self, text):
        self.text = list(text)

    def update(self):
        if not self.cooldown and self.text:
            letter = self.text.pop(0)
            if letter == '\n':
                self.rect.move_ip((0, self.text_height))
                self.rect.x = self.text_width
            else:
                self.board.add(letter, self.rect.topleft)
                self.rect.move_ip((self.text_width, 0))
            self.cooldown = self.cooldowns.get(letter, 8)

        if self.cooldown:
            self.cooldown -= 1
