
def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    for i in range(3, number):
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