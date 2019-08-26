numbers = [1, 2, 3]
print(*numbers)
# in js it...

values = [*range(5), *'hello']

print(values)


all = [*numbers, *values]

print('all', all)
