"""
    try:
        f = open('file', 'w')
    finally:
        f.close()
    
    It is good practice to use the with keyword (our context manager) when dealing with file objects.
    The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
    Using with is also much shorter that writing equivalent try-finally blocks.

    Source: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

def read_file():
    with open('aleph.txt') as f:
        count = 0
        for line in f:
            count += line.count('Beatriz')

    print('Beatriz appears {} times'.format(count))

def write_file():
    with open('test.txt', 'w') as f:
        for i in range(1, 11):
            f.write('{}\n'.format(i))


if __name__ == '__main__':
    read_file()
    write_file()