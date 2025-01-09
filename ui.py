def cls():
    return color(9, 0) + '\033[J\033[H'

def goto(y: int, x: int):
    return '\033[' + str(x) + ';' + str(y) + 'H'
def up(n: int):
    return '\033[' + str(n) + 'A'
def down(n: int):
    return '\033[' + str(n) + 'B'
def right(n: int):
    return '\033[' + str(n) + 'C'
def left(n: int):
    return '\033[' + str(n) + 'D'

def style(styles: list[str] = []):
    finalstyle = ''
    for style in styles:
        if style == 'b':
            finalstyle += '\033[1m'
        if style == 'i':
            finalstyle += '\033[3m'
        if style == 'u':
            finalstyle += '\033[4m'
        if style == 'B':
            finalstyle += '\033[22m'
        if style == 'I':
            finalstyle += '\033[23m'
        if style == 'U':
            finalstyle += '\033[24m'
    return finalstyle

### color table: https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png
def color(foreground: int, background: int):
    return '\033[38;5;' + str(foreground) + 'm\033[48;5;' + str(background) + 'm'

def hidecursor(on):
    if on:
        return '\033[?25l'
    else:
        return '\033[?25h'

def altscreen(on):
    if on:
        return '\033[?1049h' + hidecursor(True)
    else:
        return '\033[?1049l' + hidecursor(False)

def blank(on):
    if on:
        return '\033[8m'
    else:
        return '\033[28m'
