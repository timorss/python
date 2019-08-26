letters = ['a', 'b', 'c', 'd']

# add item in the beginning
letters.append('e')
print(letters)  # ['a', 'b', 'c', 'd', 'e']

# add item in specific location
letters.insert(3, '--')
print(letters)  # ['a', 'b', 'c', '--', 'd', 'e']

# remove item in the end
letters.pop()
print(letters)  # ['a', 'b', 'c', '--', 'd']

# remove item in specific location
letters.pop(1)
print(letters)  # ['a', 'c', '--', 'd']

# remove item not by index
letters.remove('--')
print(letters)  # ['a', 'c', 'd']

# remove many items
del letters[1:2]
print(letters)  # ['a', 'd']

# empty all the list
letters.clear()
print(letters)  # []
