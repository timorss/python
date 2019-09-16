from pprint import pprint
sentence = 'hhhey man how are you'

# print(sentenceChars)

chars = {}
for char in sentence:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1


# pprint(chars, width=1)

sorted_chars = sorted(
    chars.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(sorted_chars[0])

print('ss',chars.items())