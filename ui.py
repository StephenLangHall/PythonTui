def cls():
    color(9, 234)
    print('\033[J\033[H', end='')

def goto(y: int, x: int):
    print('\033[' + str(x) + ';' + str(y) + 'H', end='')
def up(n: int):
    print('\033[' + str(n) + 'A', end='')
def down(n: int):
    print('\033[' + str(n) + 'B', end='')
def right(n: int):
    print('\033[' + str(n) + 'C', end='')
def left(n: int):
    print('\033[' + str(n) + 'D', end='')

def style(styles: list[str] = []):
    for style in styles:
        if style == 'b':
            print('\033[1m', end='')
        if style == 'i':
            print('\033[3m', end='')
        if style == 'u':
            print('\033[4m', end='')
        if style == 'B':
            print('\033[22m', end='')
        if style == 'I':
            print('\033[23m', end='')
        if style == 'U':
            print('\033[24m', end='')

### color table: https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png
def color(foreground: int, background: int):
    print('\033[38;5;' + str(foreground) + 'm', end='')
    print('\033[48;5;' + str(background) + 'm', end='')

def hidecursor(on):
    if on:
        print('\033[?25l', end='')
    else:
        print('\033[?25h', end='')

def altscreen(on):
    if on:
        print('\033[?1049h', end='')
        hidecursor(True)
    else:
        print('\033[?1049l', end='')
        hidecursor(False)
