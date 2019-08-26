
numbers = [12, 15, 3, 4]
# sort
numbers.sort()  # modify the original list
print(numbers)

# sort reverse
numbers.sort(reverse=True)  # modify the original list
print(numbers)

moreNumbers = [17, 23, 1, 7]
print('sorted()')
# sort without modify the list
print(sorted(moreNumbers))  # doesn't modify the original list
print(moreNumbers)

# sort without modify the list - reverse
print(sorted(moreNumbers, reverse=True))  # doesn't modify the original list
print(moreNumbers)
