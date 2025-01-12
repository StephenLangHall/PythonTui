from time import time, sleep
from keyboard import is_pressed as pressed
from ui import *

h, w = size()
w //= 2
state = {
    'add': True,
    'quit': False,
    'fps': 0,
    'ball': {
        'y': 40,
        'x': 40,
        'yv': 0,
        'xv': 0,
        'color': 0,
    },
}

def update(state):
    h, w = size()
    w //= 2

    # Ball Controls
    if pressed('q'):
        state['quit'] = True
    if pressed('w'):
        state['ball']['yv'] -= 2
    if pressed('s'):
        state['ball']['yv'] += 2
    if pressed('a'):
        state['ball']['xv'] -= 2
    if pressed('d'):
        state['ball']['xv'] += 2

    # Ball Drag
    if state['ball']['xv'] > 0:
        state['ball']['xv'] -= 1
    if state['ball']['xv'] < 0:
        state['ball']['xv'] += 1
    if state['ball']['yv'] > 0:
        state['ball']['yv'] -= 1
    if state['ball']['yv'] < 0:
        state['ball']['yv'] += 1

    # Update Ball Position
    state['ball']['x'] += state['ball']['xv']
    state['ball']['y'] += state['ball']['yv']

    # Ball Boundaries
    if state['ball']['y'] < 0:
        state['ball']['y'] = 0
    if state['ball']['y'] > h-1:
        state['ball']['y'] = h-1
    if state['ball']['x'] < 0:
        state['ball']['x'] = 0
    if state['ball']['x'] > w-1:
        state['ball']['x'] = w-1

    # Update Ball Color
    if state['ball']['color'] >= 230:
        state['ball']['color'] = 21
    else:
        state['ball']['color'] += 1


def view(state):
    s = blank(False) + clear(color(9, 0))
    for y in range(h):
        for x in range(w):
            if y == state['ball']['y'] and x == state['ball']['x']:
                s += color(234, state['ball']['color'])
            else:
                s += color(234, 0)
            s += '  '
        if y < h-1: s += color(9, 0) + '\n'
    s += color(9, 0)
    s += goto(1, 0) + 'FPS:      ' + str(state['fps'])
    s += goto(2, 0) + 'ball X:   ' + str(state['ball']['x'])
    s += goto(3, 0) + 'ball Y:   ' + str(state['ball']['y'])
    s += goto(4, 0) + 'ball Vx:  ' + str(state['ball']['xv'])
    s += goto(5, 0) + 'ball Vy:  ' + str(state['ball']['yv'])
    s += goto(6, 0) + 'screen H: ' + str(h)
    s += goto(7, 0) + 'screen W: ' + str(w)
    return s + blank(True)

print(hidecursor(True))
start = time()

while not state['quit']:
    update(state)
    print(view(state))
    state['fps'] = 1/(time() - start)
    start = time()
    sleep(0.01)

print(reset())
