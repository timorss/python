
items = [
    ('product1', 10),
    ('product2', 8),
    ('product9', 12),
    ('product4', 1)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# new way
moreItems = [
    ('product1', 10),
    ('product2', 8),
    ('product9', 12),
    ('product4', 1)
]

moreItems.sort(key=lambda item: item[1])  # python
# moreItems.sort((item)= > item[1]) # js

print('moreItems', moreItems)
