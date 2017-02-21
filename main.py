#!/usr/bin/
# coding=utf-8

import pygame; pygame.init()
import sprite
from globals import clock, FPS, FONT
from level import Level, LEVEL
from window import Window, complex_camera
from text import FadingText


window = Window(size=(720, 480), background=pygame.Color('white'))


def scene(t):
    window.camera = None
    text = pygame.sprite.GroupSingle(FadingText(1, 2, 1, text=t, pos=window.center, anchor='center', font=FONT['scene']))
    window.background = pygame.Color('black')
    running = True
    while running:

        if not text:
            running = False

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        text.update()

        window.draw(text)
        window.update()

    window.background = pygame.Color('white')


def main():
    scene('The beginning...')
    scene('Chapter 1')

    level = Level()
    level.load_level(LEVEL)

    player1 = sprite.Actor(pos=(32 * 12, 200), collidables=level.tiles['all'])
    player2 = sprite.Actor(pos=(32 * 16, 200), collidables=level.tiles['all'])
    window.set_camera(focus=player1, camera_func=complex_camera, level_size=level.size)

    all_sprites = pygame.sprite.Group(player1, player2, level.tiles['all'])
    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if window.camera.focus is player1:
                        window.camera.focus = player2
                    else:
                        window.camera.focus = player1

        if player1.rect.colliderect(player2.rect):
            scene('And finally...')
            scene('they were together')
            running = False

        all_sprites.update()

        window.draw(all_sprites)
        window.update()


if __name__ == '__main__':
    main()
