def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print('start')
print(multiply(3, 5, 6))
print('finish')


# to use f9 and f10 to debug
# f9 mark a stop
# f10 continue