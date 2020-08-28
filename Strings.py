# Strings are immutable
foo = 'foo'
boo = 'b' + foo[1:]
print(boo)

# Reassign is better for modifying strings
s = 'qux'
s = s[0:2] + 'u' + s[2]
print(s)

print('Is {} equals to {}: {}'.format(foo, boo, foo == boo))
print('Is {} greater than {}: {}'.format(foo, boo, foo > boo))

"""
    ASCII vs Unicode

    1. ASCII (American Standard Code for Information Interchange)

    2. Unicode = International Standard

    Python 2 assumes strings are in ASCII, in the other hand, Python 3 assumes strings are in Unicode.
"""

# Length
quux = 'quux'
print('{} length: {}'.format(quux, len(quux)))
print('The character of {}, in the last position, is: {}'.format(quux, quux[-1]))

# Methods
print(quux.upper())

print(quux.endswith('u'))

i = quux.find('x')
print(i)

# Slices - Substrings
foo = 'world'

print(foo[::-1]) # Reverse a string

# string[start:end:steps]
print(foo[0:len(foo):2])

print(foo[1:3])

print(foo[2:])
