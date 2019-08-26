
days = ['Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday']


def whatday(x):
    return days[x-1]


def areYouPlayingBanjo(name):
    return name.title()


print(areYouPlayingBanjo('timor'))


# def remove_every_other(my_list):
#     arr = []
#     for item, i in enumerate(my_list):
#         if i % 2 == 0:
#             arr.append(item)
#     return arr


# print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
def find_smallest_int(arr):
    arr.sort()
    return arr[0]


print(find_smallest_int([6, 2, 3, 4, 10, 6, 7, 8, 9, 4]))


def reverse_seq(n):
    return list(range(1, n+1))[::-1]


print(reverse_seq(7))
