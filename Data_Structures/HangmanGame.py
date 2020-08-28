import random
import os

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']


WORDS = [
    'computadora',
    'celular',
    'iphone',
    'mexico',
    'palabra',
    'frase'
]

def display_board(hidden_word, tries):
    os.system('clear') # Linux and macOS
    # os.system('cls') Windows

    print(IMAGES[tries])
    print('\n', hidden_word)
    print('---- * ---- * ---- * ---- * ----')


def game(random_word):
    hidden_word = ['_'] * len(random_word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = input('Ingresa una letra: ')

        letter_indexes = []
        for i in range(len(random_word)):
            if random_word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == len(IMAGES) - 2:
                display_board(hidden_word, tries)
                print('Lo sentimos, has perdido :/. La palabra correcta era \'{}\''.format(random_word))

                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

        if '_' not in hidden_word:
            display_board(hidden_word, tries)
            print('¡Felicidades! Has ganado')

            break
            

if __name__ == '__main__':
    print('B I E N V E N I D O S')

    random_word = random.choice(WORDS)

    game(random_word)