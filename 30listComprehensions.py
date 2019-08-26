items = [
    ('product1', 10),
    ('product2', 8),
    ('product9', 12),
    ('product4', 1)
]

# map
prices = list(map(lambda item: item[1], items))
print('map', prices)

# list Comprehensions
prices = [item[1] for item in items]
print('list Comprehensions', prices)

# filter
_prices = list(filter(lambda item: item[1] >= 10, items))
print('filter', _prices)

# list Comprehensions
_prices = [item for item in items if item[1] >= 10]
print('list Comprehensions', _prices)
