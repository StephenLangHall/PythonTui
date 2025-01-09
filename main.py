import time, random
from ui import *
from util import *

h, w = size()
state = {
    'add': True,
    'cur': {
        'y': 20,
        'x': 20,
        'yv': 0,
        'xv': 0
    },
    'quit': False,
    'fps': 0,
}

def update(state, keys):
    h, w = size()
    if 'q' in keys:
        state['quit'] = True
    if 'w' in keys:
        state['cur']['yv'] -= 1
    if 's' in keys:
        state['cur']['yv'] += 1
    if 'a' in keys:
        state['cur']['xv'] -= 1
    if 'd' in keys:
        state['cur']['xv'] += 1

    state['cur']['x'] += state['cur']['xv']
    state['cur']['y'] += state['cur']['yv']

    if state['cur']['y'] < 0:
        state['cur']['y'] = h-1
    if state['cur']['y'] > h-1:
        state['cur']['y'] = 0
    if state['cur']['x'] < 0:
        state['cur']['x'] = w-1
    if state['cur']['x'] > w-1:
        state['cur']['x'] = 0

def view(state):
    s = blank(False) + cls()
    for y in range(h-1):
        for x in range(w-1):
            if y == state['cur']['y'] and x == state['cur']['x']:
                s += color(234, random.randrange(1,9,1))
                s += '  '
            else:
                s += color(234, 0)
                s += '  '
        s += color(9, 0) + '\n'
    s += '\nFPS: ' + str(state['fps'])
    s += '\nX: ' + str(state['cur']['x'])
    s += '\nY: ' + str(state['cur']['y'])
    s += '\nVx: ' + str(state['cur']['xv'])
    s += '\nVy: ' + str(state['cur']['yv'])
    return s + blank(True)

InitialTime = time.time()
print(altscreen(True))
while not state['quit']:
    keys = getpressed(['w', 's', 'a', 'd', 'q'])
    update(state, keys)
    print(view(state))
    state['fps'] = 1 / (time.time() - InitialTime)
    InitialTime = time.time()
    time.sleep(0.05)
print(altscreen(False))
