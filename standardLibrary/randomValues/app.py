import random
import string

print(random.random())
print(random.randint(1, 10))
# k is the number of numbers
print(random.choices([1, 2, 3, 4, 5, 6, 10], k=2))
# k is the number of numbers
print(''.join(random.choices('acdfsdgfsdf', k=4)))

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789

print(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=4)))


numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
