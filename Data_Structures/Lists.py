def average(temperatures):
    result = sum(temperatures) / len(temperatures)

    return result

if __name__ == '__main__':
    temperatures = [21, 25.5, 34, 30, 20, 40]

    result = average(temperatures)

    print('{} is the average temperature of {}'.format(result, temperatures))