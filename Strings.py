# Strings are immutable
foo = 'foo'
boo = 'b' + foo[1:]
print(boo)

print('Is {} equals to {}: {}'.format(foo, boo, foo == boo))
print('Is {} greater than {}: {}'.format(foo, boo, foo > boo))

"""
    ASCII vs Unicode

    1. ASCII (American Standard Code for Information Interchange)

    2. Unicode = International Standard

    Python 2 assumes strings are in ASCII, in the other hand, Python 3 assumes strings are in Unicode.
"""