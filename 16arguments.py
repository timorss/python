def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(3, 5, 6))


def save_user(**user):
    print(user['name'])


save_user(name='Timor', id=301)
