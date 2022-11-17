import time
from routines.debug import mouse_position
from routines.redeem import redeem_code
import click

ROUTINES = {
    'redeem': redeem_code,
    'mouse': mouse_position,
}


@click.command()
@click.argument('routine')
def main(routine):
    # if routine is unknown, abort
    if routine not in ROUTINES:
        print(f'ERROR: unknown routine "{routine}"')
        return

    # run routine
    running = True
    while running:
        running = ROUTINES[routine]()
        time.sleep(1)


if __name__ == '__main__':
    main()
