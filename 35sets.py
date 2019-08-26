numbers = [1, 1, 2, 3, 4]

first = set(numbers)  # removing duplicate
print(first)  # {1, 2, 3, 4}
second = {1, 5}

print(first | second) # {1, 2, 3, 4, 5}
print(first & second) # {1}
print(first - second) # {2, 3, 4}
print(first ^ second) # {2, 3, 4, 5}
