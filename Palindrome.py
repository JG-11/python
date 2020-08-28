def palindrome(phrase):
    if phrase == phrase[::-1]:
        return True
    
    return False


if __name__ == '__main__':
    phrase = input('Type a word or phrase: ')

    aux = phrase.lower().replace(' ', '')

    result = palindrome(aux)

    if not result:
        print('{} is not a palindrome'.format(phrase))
    else:
        print('{} is a palindrome'.format(phrase))