for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break


for i in range(30):
    if i % 3 != 0:
        continue
    
    print(i)


for i in range(0, 30, 2):
    print(i)


phrase = 'Hello world'
for letter in phrase:
    print(letter)