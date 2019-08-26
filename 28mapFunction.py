items = [
    ('product1', 10),
    ('product2', 8),
    ('product9', 12),
    ('product4', 1)
]

# one way
# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# second way
x = map(lambda item: item[1], items)
# x = moreItems.map((item)=> item[1]) # js
for item in x:
    print(item)

# or
print('list(x)', list(map(lambda item: item[1], items)))
