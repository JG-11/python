KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    words = message.split(' ')

    aux_words = []

    for word in words:
        aux_word = ''
        for letter in word:
            aux_word += KEYS[letter]
        
        aux_words.append(aux_word)

    result = ' '.join(aux_words)

    return result


def decipher(message):
    words = message.split(' ')

    aux_words = []

    for word in words:
        aux_word = ''
        for letter in word:
            key_list = list(KEYS.keys())
            val_list = list(KEYS.values())

            # As key at any position N in key_list will have corresponding value at position N in val_list
            aux_word += key_list[val_list.index(letter)] 

        aux_words.append(aux_word)

    result = ' '.join(aux_words)

    return result


if __name__ == '__main__':
    option = input("""
        What option do you want to do?

        [c]ypher
        [d]ecipher
        [e]xit
    """)

    if option is 'c':
        message = input('Type the message to cypher: ')

        result = cypher(message)

        print('Ciphered message:', result)
    
    elif option is 'd':
        message = input('Type the message to be deciphered: ')

        result = decipher(message)

        print('Deciphered message:', result)
    
    elif option is 'e':
        print('Thanks for using the program!')

    else:
        print('Not valid command')

