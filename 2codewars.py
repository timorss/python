# def odd_count(n):
#     res = []
#     for num in range(n):
#         if num < n and num % 2 != 0:
#             res.append(num)
#     return len(res)


# print(odd_count(7))


import math


def name_value(my_list):
    res = []
    characters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i, word in enumerate(my_list):
        sum_of_letters = 0
        for char in word:
            sum_of_letters += (characters.index(char))
        res.append(sum_of_letters*(i+1))
    return res


print(name_value(["abac", "abc", "abc", "abc"]))


def accum(s):
    res = []
    chars = list(s)
    for i, char in enumerate(chars, 1):
        res.append(char*i)
    return '-'.join([word.capitalize() for word in res])


print(accum("ZpglnRxqenU"))


def get_middle(s):
    string_length = len(s)
    equal = string_length % 2 == 0
    equal_length = int(string_length / 2)
    return f'{s[equal_length-1]}{s[equal_length]}' if equal else s[math.ceil(string_length / 2)]


print(get_middle("testr"))
