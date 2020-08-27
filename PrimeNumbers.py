import math

def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    root = math.sqrt(number) # The smallest factor is less than, or is at most equal to, the square root

    for i in range(3, int(root) + 1):
        if number % i == 0:
            return False
    
    return True

if __name__ == '__main__':
    number = int(input('Type a number: '))

    result = is_prime(number)

    if result:
        print('{} is prime'.format(number))
    else:
        print('{} is not prime'.format(number))