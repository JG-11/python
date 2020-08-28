def binary_search(numbers, number):
    numbers.sort()

    higher = len(numbers) - 1
    lower = 0

    while lower <= higher:
        middle = (lower + higher) // 2

        if number > numbers[middle]:
            lower = middle + 1
        elif number < numbers[middle]:
            higher = middle - 1
        else:
            return True
    
    return False



if __name__ == '__main__':
    numbers = [4, 5, 2, 3, 1, 19, 0, 25]

    number = int(input('Type the number to look for: '))

    exists = binary_search(numbers, number)

    if exists:
        print('{} exists in {}'.format(number, numbers))
    else:
        print('{} not exists in {}'.format(number, numbers))