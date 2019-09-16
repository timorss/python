# # def next_item(xs, item):
# #     return listiter(xs)
# #     for char in arr:
# #         if char == item:
# #             return next(arr, None)


# # print(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5))
# # print(next_item(['a', 'b', 'c'], 'c'))
# # print(next_item('testing', 't'))
# from datetime import date
# signs = ['!', '@', '#', '$', '%', '^', '&', '*',
#          '(', ')', '_', '-', '\'', '+', ' ', ',', '.',
#          '/', '[', ']', '1', '2', '3', '4', '5', '6', '7',
#          '8', '9', '0']


# def shortcut(s):
#     vowels = ['a', 'o', 'u', 'i', 'e']
#     return ''.join([char for char in s if char not in vowels])


# print(shortcut('helooomannn'))


# def two_oldest_ages(ages):
#     return ages[-2]


# print(two_oldest_ages([1, 5, 87, 45, 8, 8]))


# def solution(value):
#     string = str(value)
#     string_length = len(string)
#     rest = 5-string_length
#     answer = ''
#     for num in range(rest):
#         answer += '0'
#     answer += string
#     return f"Value is {answer}"


# print(solution(15))


# def remove_url_anchor(url):
#     try:
#         index_of_anchor = url.index('#')
#         print(index_of_anchor)
#         return url[0:index_of_anchor]
#     except:
#         return url


# print(remove_url_anchor('www.codewars.com/katas/?page=#about'))


# def time_for_milk_and_cookies(dt):
#     print(dt.month)
#     print(dt.day)
#     return dt.month == 12 and dt.day == 24


# print(time_for_milk_and_cookies(date(2013, 12, 24)))


# def likes(names):
#     if len(names) == 0:
#         return 'no one likes this'
#     arrOfNames = names[:3]
#     print(arrOfNames)
#     string = ''
#     like = 'likes' if len(names) == 1 else 'like'
#     for name in arrOfNames:
#         if arrOfNames.index(name) == 0:
#             string += name
#         elif arrOfNames.index(name) == len(arrOfNames)-1:
#             last = ' and ' + str(len(names)-2) + \
#                 ' others' if len(names) > 3 else ' and ' + name
#             string += last
#         else:
#             string += ', ' + name
#     return string + ' ' + like + ' this'


# print(likes(['Max', 'John', 'Mark']))


# def password(s):
#     res = len(s) >= 8
#     lower = False
#     upper = False
#     number = False
#     print(s)
#     for char in s:
#         if char == char.islower():
#             lower = True
#         if char == char.isupper()():
#             print(char)
#             upper = True
#         if char.isnumeric():
#             number = True
#     return res and lower and upper and number

# print(password('abcd1234'))

# def numericals(string):
#     dic = {}
#     res=''
#     for char in string:
#         if char in dic:
#             dic[char] += 1
#             res+=str(dic[char])
#         else:
#             dic[char] = 1
#             res+='1'
#     return res


# print(numericals('abcda'))

def cakes(recipe, available):
    return min([available.get(k, 0)/recipe[k] for k in recipe])


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
