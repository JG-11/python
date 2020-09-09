import os

class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        os.system('clear')

        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


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