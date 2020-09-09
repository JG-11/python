import os

from lamp import Lamp

if __name__ == '__main__':
    lamp = Lamp(False)

    while True:
        opt = int(input('''
            Choose an option:
            0. Turn off
            1. Turn on
            2. Exit
        '''))

        if opt == 0:
            lamp.turn_off()
        elif opt == 1:
            lamp.turn_on()
        elif opt == 2:
            break
        else:
            os.system('clear')
            print('Invalid option')