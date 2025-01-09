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
    s = cls()
    for y, row in enumerate(state['grid']):
        for x, cell in enumerate(row):
            if y == state['cur'][0] and x == state['cur'][1]:
                s += color(234, cell)
                s += '  '
            else:
                s += color(234, 0)
                s += '  '
        s += color(9, 234) + '\n'
    s += state['key']
    return s

print(altscreen(True))
while not state['quit']:
    keys = getpressed(['w', 's', 'a', 'd', 'q'])
    update(state, keys)
    print(view(state))
    time.sleep(0.1)
print(altscreen(False))
