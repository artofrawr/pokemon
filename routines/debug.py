from pynput.mouse import Controller


mouse = Controller()


def mouse_position():
    print(f'mouse position: {mouse.position}')
    return True
