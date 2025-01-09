import time, random
from ui import *
from util import *

h = 50
w = 50
state = {
    'add': True,
    'grid': [[0 for _ in range(w)] for _ in range(h)],
    'cur': [0, 0],
    'quit': False,
    'fps': 0,
}

def update(state, keys):
    if 'q' in keys:
        state['quit'] = True
    if 'w' in keys:
        if state['cur'][0] > 0:
            state['cur'][0] -= 1
    if 's' in keys:
        if state['cur'][0] < h-1:
            state['cur'][0] += 1
    if 'a' in keys:
        if state['cur'][1] > 0:
            state['cur'][1] -= 1
    if 'd' in keys:
        if state['cur'][1] < w-1:
            state['cur'][1] += 1
    state['grid'] = [[random.randrange(1,9,1) for _ in range(w)] for _ in range(h)]

def view(state):
    s = blank(False) + cls()
    for y, row in enumerate(state['grid']):
        for x, cell in enumerate(row):
            if y == state['cur'][0] and x == state['cur'][1]:
                s += color(234, cell)
                s += '  '
            else:
                s += color(234, 0)
                s += '  '
        s += color(9, 0) + '\n'
    s += '\nFPS: ' + str(state['fps'])
    return s + blank(True)

InitialTime = time.time()
print(altscreen(True))
while not state['quit']:
    keys = getpressed(['w', 's', 'a', 'd', 'q'])
    update(state, keys)
    print(view(state))
    state['fps'] = 1 / (time.time() - InitialTime)
    InitialTime = time.time()
    time.sleep(0.01)
print(altscreen(False))
