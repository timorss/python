numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other = numbers
print(first)
print(second)
print(other)


def multiply(*numbers):
    print(numbers)


multiply(1, 2, 3, 4, 5, 6, 7)
