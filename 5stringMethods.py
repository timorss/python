course = 'Python Programming'

# to upper case
print(course.upper())
# to lower case
print(course.lower())
# to title case
print(course.title())

# trim
message = '  Hey man    '
print(message.strip())
# trim right space
print(message.rstrip())
# trim left space
print(message.lstrip())


print(course.find('rog'))  # get index of letter
print(course.replace('rog', '-'))  # replace
print('rog' in course)  # check if exist
print('rog' not in course)  # check if does'nt exist
