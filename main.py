import time, random
from ui import *
from util import *

h = 50
w = 50
state = {
    'add': True,
    'grid': [[0 for _ in range(w)] for _ in range(h)],
    'key': '',

    'cur': [0, 0],

    'quit': False
}

def update(state, keys):
    if 'q' in keys:
        state['quit'] = True
    if 'w' in keys:
        state['cur'][0] -= 1
    if 's' in keys:
        state['cur'][0] += 1
    if 'a' in keys:
        state['cur'][1] -= 1
    if 'd' in keys:
        state['cur'][1] += 1
    state['grid'] = [[random.randrange(1,9,1) for _ in range(w)] for _ in range(h)]
    state['keys'] = keys

def view(state):
    cls()
    for y, row in enumerate(state['grid']):
        for x, cell in enumerate(row):
            if y == state['cur'][0] and x == state['cur'][1]:
                color(234, 0)
                print(cell, end=' ')
            else:
                color(234, cell)
                print(cell, end=' ')
        color(9, 234)
        print('')
    print(state['key'])

altscreen(True)
while not state['quit']:
    keys = getpressed(['w', 's', 'a', 'd', 'q'])
    update(state, keys)
    view(state)
    time.sleep(0.1)
altscreen(False)
