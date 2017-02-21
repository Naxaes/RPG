import pygame


class Text(pygame.sprite.Sprite):

    def __init__(self, text, pos, font=pygame.font.SysFont('Arial', 64), color=pygame.Color('white'), anchor='topleft'):
        super(Text, self).__init__()
        self.image = font.render(text, False, color)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(**{anchor: pos})


class FadingText(Text):

    def __init__(self, fade_in, wait, fade_out, **kwargs):
        super(FadingText, self).__init__(**kwargs)
        self.fade_in = fade_in * 1000
        self.time_in = fade_in * 1000
        self.wait = wait * 1000
        self.time_wait = wait * 1000
        self.fade_out = fade_out * 1000
        self.time_out = fade_out * 1000

        self.alpha = 255
        self.time_since_last = pygame.time.get_ticks()

    def update(self):
        dt = pygame.time.get_ticks() - self.time_since_last
        self.time_since_last = pygame.time.get_ticks()

        if self.time_in > 0:
            self.time_in -= dt
            self.image.set_alpha(255 - 255 * self.time_in / self.fade_in)
        elif self.time_wait > 0:
            self.time_wait -= dt
        elif self.time_out > 0:
            self.time_out -= dt
            self.image.set_alpha(255 * self.time_out / self.fade_out)
        else:
            self.kill()
