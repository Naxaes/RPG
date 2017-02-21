import pygame


class Camera:

    def __init__(self, camera_func, window_size, level_size, focus):
        self.camera_func = camera_func
        self.state = pygame.Rect((0, 0), level_size)
        self.window_size = window_size
        self.focus = focus
        self.update()

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self):
        self.state = self.camera_func(self.state, self.focus.rect, *self.window_size)


def simple_camera(camera, target_rect, window_width, window_height):
    x, y = target_rect.topleft
    camera.topleft = (window_width/2 - x, window_height/2 - y)
    return camera


def complex_camera(camera, target_rect, window_width, window_height):
    x, y = target_rect.topleft
    w, h = camera.size
    x, y = -x + window_width / 2, -y + window_height / 2

    x = min(0, x)                                 # stop scrolling at the left edge
    x = max(-(camera.width - window_width), x)    # stop scrolling at the right edge
    y = min(0, y)                                 # stop scrolling at the top
    y = max(-(camera.height - window_height), y)  # stop scrolling at the bottom
    return pygame.Rect(x, y, w, h)


class Window:

    def __init__(self, size, background=None):
        self._screen = pygame.display.set_mode(size)
        self.background = background

        self.left, self.top = (0, 0)
        self.bottom, self.right = self.size = size
        self.center = self.centerx, self.centery = size[0] // 2, size[1] // 2

        self.camera = None

    def set_camera(self, focus, camera_func=simple_camera, level_size=None):
        if level_size is None:
            level_size = self.size
        self.camera = Camera(camera_func, window_size=self.size, level_size=level_size, focus=focus)

    def draw(self, sprites):
        if self.background:
            self._screen.fill(self.background)

        if self.camera:
            for sprite in sprites:
                self._screen.blit(sprite.image, self.camera.apply(sprite))
        else:
            sprites.draw(self._screen)

    def update(self):
        pygame.display.update()
        if self.camera:
            self.camera.update()
