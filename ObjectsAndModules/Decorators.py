def decorator(function):
    def wrapper(*args):
        print('Computation started')

        function(*args)

        print('Computation finished')
    
    return wrapper

@decorator
def add(number_one, number_two):
    print('Addition:', number_one + number_two)

@decorator
def subtract(number_one, number_two, number_three):
    print('Subtraction:', number_one - number_two - number_three)

if __name__ == '__main__':
    number_one = int(input('Type the first integer: '))
    number_two = int(input('Type the second integer: '))

    add(number_one, number_two)

    number_three = int(input('Type the third integer: '))

    subtract(number_one, number_two, number_three)