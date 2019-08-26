letters = ['a', 'b', 'c', 'd']

print(letters.index('a'))  # 0

if 'e' in letters:
    print(letters.index('e'))

    print(letters.count('d'))  # 1
    print(letters.count('e'))  # 0


def count_sheep(n):
    x = range(n)
    res = []
    for num in x:
        res.append(f'{num+1} sheep...')
    return res


print(count_sheep(4))
