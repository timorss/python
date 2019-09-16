
def match_arrays(v, r):
    res = 0
    for item in v:
        if item in r:
            res += 1
    return res


print(match_arrays(['Perl', 'Closure', 'JavaScript'], ['Go', 'C++', 'Erlang']))

# Remember you have a CHANGE dictionary to work with ;)
dic = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
    'dollar': 1.00
}


def change_count(change):
    sums = 0
    _change = change.split(' ')
    for coin in _change:
        sums += dic[coin]
    return f"${round(sums, 2)}"


print(change_count(
    'dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny'))
print(len(str(456)))

# print(list(zip([1, 2, 3], [1, 2, 3], [4, 5, 6])))

print('----------------')


def avg_array(arr):
    res = []
    for n in list(zip(*arr)):
        res.append(sum(n)/len(n))
    return res


print(avg_array([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3],
                 [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]))


def duplicate_count(text):
    chars = list(text)
    dic = {}
    res = []
    for char in chars:
        if char.lower() in dic:
            dic[char.lower()] += 1
        else:
            dic[char.lower()] = 1
    for key in dic:
        if dic[key] > 1:
            res.append(key)

    return len(res)


print(duplicate_count('Indivisibilities'))


def array_mash(a, b):
    return [char for t in list(zip(a, b)) for char in t]


print(array_mash([1, 2, 3], ['a', 'b', 'c']))


