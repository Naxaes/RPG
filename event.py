import pygame
pygame.init()


events = {
    'key_down': [],
    'key_up': [],
    'mouse_down': [],
    'mouse_up': [],
    'mouse_move': [],
    'window_resize': [],
    'quit': 0
}

def keys():
    pass


def _pressed(previous, current):
    return max(current - previous, 0)


def get(event_type='all'):
    if event_type == 'all':
        pass
    else:
        return events[event_type]


def update():

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            events['pressed'].append(event.key)
        elif event.type == pygame.KEYUP:
            events['released'].append(event.key)
