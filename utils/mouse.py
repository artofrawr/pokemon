from pynput.mouse import Button, Controller
import time

mouse = Controller()


def click(position):
    mouse.position = position
    time.sleep(0.2)
    mouse.click(Button.left, 2)
