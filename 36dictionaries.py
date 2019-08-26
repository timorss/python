# one way
point = {'x': 1, 'y': 2}
# second way
point = dict(x=1, y=2)

point['x'] = 10
point['z'] = 20
print(point)
print(point['x'])  # 10

if 'n' in point:
    print(point['n'])  # err

print(point.get('n'))  # none
print(point.get('n', 0))  # if there isn't an item with a key 'a' return 0

# delete an item

del point['x']
print(point)
print('----------')

# itirate a dic
# one way
for key in point:
    print(key, point[key])

# second way
for key, val in point.items():
    print(key, val)
