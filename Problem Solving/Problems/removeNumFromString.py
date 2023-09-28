charText = 'abcd1234efgh5678'

resText = ''

for i in charText:
    if ord(i) >= 48 and ord(i) <= 57:
        continue
    else:
        resText += i

print(resText)