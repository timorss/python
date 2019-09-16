import sys


# print(sys.argv)

if len(sys.argv) == 1:
    # print('USAGE: python3 app.py <password>')
    pass
else:
    password = sys.argv[1]
    print('Password', password)
