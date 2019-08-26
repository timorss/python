
message = 'a'


def greet():
    if True:
        message = 'b'
        print(message)


greet()  # message = a


print(message)  # message = a
