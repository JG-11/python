nums = []
for i in range(1, 31):
    if i % 2 == 0:
        nums.append(i)
print(nums)

# List comprehension
nums = [i for i in range(1, 31) if i % 2 == 0]
print(nums)


square = {}
for i in range(1, 11):
    square[i] = i**2
print(square)

# Dictionary comprehension
square = {i: i**2 for i in range(1, 11)}
print(square)