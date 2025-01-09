import keyboard

def getpressed(keys):
    return [key for key in keys if keyboard.is_pressed(key)]
