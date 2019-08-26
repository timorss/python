from timeit import timeit
# numbers = [0, 2, 3, 4]

# try:
#     print(numbers[15])
# except IndexError:
#     print('no valid man')
# else:
#     print('good job')


# print('continue')



def calculate(age):
    if age <= 0:
        raise ValueError('age cannot be 0 or less')
    return 10/age


try:
    calculate(0)
except ValueError as error:
    print(error)
