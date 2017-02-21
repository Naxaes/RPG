import pygame; pygame.init()
from window import Window
from level import Level

window = Window(size=(24*32, 16*32), background=pygame.Color('white'))
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()


LEVEL_1 = [
    '                                                                                              ',
    '                                    PPPP                                                      ',
    '         PPPP                                           PPPP                      P           ',
    '                                                                                              ',
    'PP                                           PPPP                                             ',
    '                                                                                              ',
    '               PPPP                                           PPPP                   PPPP     ',
    '                                                                                              ',
    '                             PPPP                                           PPPP              ',
    '                                                                                              ',
    '                                                                                              ',
    '                                                                                              ',
    '       PPPP                                           PPPP                                    ',
    '                         PPP                                            PPP                   ',
    '                                                                                              ',
    '                                                                                              ',
    '                                     PPPP                                                     ',
    '                                                                                              ',
]


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Player, self).__init__()
        self.rect = pygame.Rect(pos, (32, 32))
        self.image = pygame.Surface((32, 32))
        self.speed = 100
        self.velocity = [0, 0]
        self.prev_velocity = self.velocity.copy()

    def update1(self, dt):
        """
        Frame dependent movement.

        Args:
            dt: Ignored parameter.

        Returns:
            None
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity[0] = -self.speed // FPS
        elif keys[pygame.K_d]:
            self.velocity[0] = self.speed // FPS
        else:
            self.velocity[0] = 0

        if keys[pygame.K_w]:
            self.velocity[1] = -self.speed // FPS
        elif keys[pygame.K_s]:
            self.velocity[1] = self.speed // FPS
        else:
            self.velocity[1] = 0

        self.rect.move_ip(*self.velocity)

    def update2(self, dt):
        """
        Time dependent movement.

        Args:
            dt: Amount of seconds since last call to update.

        Returns:
            None
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity[0] = -self.speed * dt
        elif keys[pygame.K_d]:
            self.velocity[0] = self.speed * dt
        else:
            self.velocity[0] = 0

        if keys[pygame.K_w]:
            self.velocity[1] = -self.speed * dt
        elif keys[pygame.K_s]:
            self.velocity[1] = self.speed * dt
        else:
            self.velocity[1] = 0

        self.rect.move_ip(*self.velocity)

    def update3(self, dt):
        """
        Time dependent movement with quick fix.

        Args:
            dt: Amount of seconds since last call to update.

        Returns:
            None
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity[0] = -self.speed * dt
        elif keys[pygame.K_d]:
            self.velocity[0] = self.speed * dt
        else:
            self.velocity[0] = 0

        if keys[pygame.K_w]:
            self.velocity[1] = -self.speed * dt
        elif keys[pygame.K_s]:
            self.velocity[1] = self.speed * dt
        else:
            self.velocity[1] = 0

        dx = self.velocity[0] - self.prev_velocity[0]
        dy = self.velocity[1] - self.prev_velocity[1]
        if abs(dx) < 2:
            self.velocity[0] -= dx
        if abs(dy) < 2:
            self.velocity[1] -= dy
        self.prev_velocity = self.velocity.copy()

        self.rect.move_ip(*self.velocity)


player = Player((32*4, 12*32))
level = Level()
level.load_level(LEVEL_1)
window.set_camera(focus=player)
all_sprites.add(player, level.tiles['all'])

methods = (
    ('time-dependent', player.update1),
    ('time-dependent with fix', player.update2),
    ('frame-dependent', player.update3)
)
i = 0
running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                text, method = methods[i]
                player.update = method
                print('Method:', text)
                i = (i + 1) % len(methods)
            elif event.key == pygame.K_n:
                if player.speed == 1000:
                    player.speed = 0
                player.speed += 51
                print('Speed:', player.speed)

    if player.rect.right > level.size[0] - window.centerx:
        player.rect.left = window.centerx
    elif player.rect.left < window.centerx:
        player.rect.right = level.size[0] - window.centerx

    if player.rect.bottom > level.size[1] - window.centery:
        player.rect.top = window.centery
    elif player.rect.top < window.centery:
        player.rect.bottom = level.size[1] - window.centery

    all_sprites.update(dt)
    window.draw(all_sprites)
    window.update()

