from keyboard import is_pressed
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
    if is_pressed('q'):
        state['quit'] = True
    if is_pressed('w'):
        state['ball']['yv'] -= 2
    if is_pressed('s'):
        state['ball']['yv'] += 2
    if is_pressed('a'):
        state['ball']['xv'] -= 2
    if is_pressed('d'):
        state['ball']['xv'] += 2

    if state['ball']['xv'] > 0:
        state['ball']['xv'] -= 1
    if state['ball']['xv'] < 0:
        state['ball']['xv'] += 1
    if state['ball']['yv'] > 0:
        state['ball']['yv'] -= 1
    if state['ball']['yv'] < 0:
        state['ball']['yv'] += 1

    state['ball']['x'] += state['ball']['xv']
    state['ball']['y'] += state['ball']['yv']

    if state['ball']['y'] < 0:
        state['ball']['y'] = 0
    if state['ball']['y'] > h-1:
        state['ball']['y'] = h-1
    if state['ball']['x'] < 0:
        state['ball']['x'] = 0
    if state['ball']['x'] > w-1:
        state['ball']['x'] = w-1

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
    s += goto(0, 0) + 'FPS:      ' + str(state['fps']) + '\n'
    s += goto(1, 0) + '\nball X:   ' + str(state['ball']['x'])
    s += goto(2, 0) + '\nball Y:   ' + str(state['ball']['y'])
    s += goto(3, 0) + '\nball Vx:  ' + str(state['ball']['xv'])
    s += goto(4, 0) + '\nball Vy:  ' + str(state['ball']['yv'])
    s += goto(5, 0) + '\nscreen H: ' + str(h)
    s += goto(6, 0) + '\nscreen W: ' + str(w)
    return s + blank(True)

print(hidecursor(True))

while not state['quit']:
    update(state)
    print(view(state))
#    time.sleep(0.05)

print(RESET())
