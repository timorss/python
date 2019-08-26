course = 'Python Programming'
# length of string
print(len(course))


# first character
print(course[0])
# last character
print(course[-1])
# second last character
print(course[-2])
# slice string
print(course[0:7])  # slice until index 7
print(course[:7])  # slice until index 7
print(course[0:])  # slice until the end
print(course[:])  # slice until the end

###########
print(id(course))  # different id
print(id(course[0]))  # different id
###########

# secial character
message = "Python \"Programming"

print(message)  # different id

long_message = """hey 
man 
hou 
yu 
sooin
"""
print(long_message)
