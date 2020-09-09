import random

def guess_number(random_number):
    guessed = False

    while not guessed:
        number = int(input('Type a number: '))

        if number == random_number:
            print('Congratulations! You have guessed the number')

            guessed = True
        elif number > random_number:
            print('The number to guess is lower')
        else:
            print('The number to guess is greater')

if __name__ == '__main__':
    random_number = random.randint(10, 100)

    guess_number(random_number)

