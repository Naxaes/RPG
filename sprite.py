import pygame
from globals import COLOR, GRAVITY


actor = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()


class Actor(pygame.sprite.Sprite):

    def __init__(self, pos, collidables):
        super(Actor, self).__init__(actor)
        self.rect = pygame.Rect(pos, (32, 64))
        self.image = pygame.Surface((32, 64))
        self.image.fill(COLOR['red'])

        self.speed = 4
        self.jump_speed = 8
        self.position = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, GRAVITY)

        self.on_ground = False
        self.double_jump = False

        self.collidables = collidables
        self.previous_key = pygame.key.get_pressed()

    def update(self):
        key = pygame.key.get_pressed()

        # Move left and right.
        if key[pygame.K_a]:
            self.velocity[0] = -self.speed
        elif key[pygame.K_d]:
            self.velocity[0] = self.speed
        else:
            self.velocity[0] = 0

        # Jumping.
        if (self.on_ground or self.double_jump) and key[pygame.K_w] - self.previous_key[pygame.K_w] == 1:
            self.velocity[1] = -self.jump_speed
            if self.on_ground:
                self.on_ground = False
            else:
                self.double_jump = False

        # Update position.
        last = self.rect.copy()
        self.velocity += self.acceleration
        self.position += self.velocity
        self.rect.topleft = self.position
        new = self.rect

        for tile in pygame.sprite.spritecollide(self, self.collidables, dokill=False):
            type_ = tile.kind
            tile = tile.rect

            if last.right <= tile.left < new.right:  # Collide right.
                new.right = tile.left
                self.position[0] = new.left
            elif last.left >= tile.right > new.left:  # Collide left.
                new.left = tile.right
                self.position[0] = new.left

            if self.rect.colliderect(tile):
                if last.bottom <= tile.top < new.bottom:  # Collide bottom.
                    new.bottom = tile.top
                    self.position[1] = new.top
                    self.on_ground = True
                    self.double_jump = True
                    self.velocity[1] = 0
                elif type_ == 'W' and last.top >= tile.bottom > new.top:  # Collide top.
                    new.top = tile.bottom
                    self.position[1] = new.top
                    self.velocity[1] = 0

        self.previous_key = key


