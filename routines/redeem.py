from pyautogui import typewrite
import os
import time
from utils.mouse import click

POSITIONS = {
    'TEXT': (593, 1069),
    'SUBMIT': (638, 1180),
    'CLAIM': (1442, 1183),
    'DONE': (1004, 1183),
}


def redeem_code():
    # read codes.txt
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file_path = os.path.join(root_path, 'codes.txt')
    with open(file_path, 'r') as fin:
        data = fin.read().splitlines(True)
        if len(data) == 0:
            print('redeem : NO CODES LEFT')
            return False

        first_line = data[0].strip()
        other_lines = data[1:]

    # remove first line from file
    with open(file_path, 'w') as fout:
        fout.writelines(other_lines)

    print(f'redeem : {first_line}')

    # click on textfield
    click(POSITIONS['TEXT'])
    time.sleep(0.5)

    # enter code
    typewrite(first_line)

    # click submit
    click(POSITIONS['SUBMIT'])
    time.sleep(0.5)

    # click claim
    click(POSITIONS['CLAIM'])
    time.sleep(1)

    # click done
    click(POSITIONS['DONE'])

    return True
