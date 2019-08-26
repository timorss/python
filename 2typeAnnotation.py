# if you declare a type of var, you will see lint problem
x: int = 1
x = 'Hey man'

print(x)


# mutable and immutable
y = 1
print(id(y))

y = 3
print(id(y))

j = [1, 2, 3]
print(id(j))

j.append(4)
print(id(j))
