#!/usr/bin/
# coding=utf-8

import pygame; pygame.init()
import sprite
from globals import clock, fps
from level import Level, LEVEL
from window import Window, complex_camera


window = Window(size=(720, 480), background=pygame.Color('white'))

level = Level()
level.load_level(LEVEL)

player1 = sprite.Actor(pos=(32 * 12, 200), collidables=level.tiles['all'])
player2 = sprite.Actor(pos=(32 * 16, 200), collidables=level.tiles['all'])
window.set_camera(focus=player1, camera_func=complex_camera, level_size=level.size)

all_sprites = pygame.sprite.Group(player1, player2, level.tiles['all'])
running = True
while running:
    dt = clock.tick(fps) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if window.camera.focus is player1:
                    window.camera.focus = player2
                else:
                    window.camera.focus = player1

    all_sprites.update(dt)

    window.draw(all_sprites)
    window.update()

