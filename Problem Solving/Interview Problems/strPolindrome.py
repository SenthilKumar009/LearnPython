inputStr = input("Enter the string: ")

#reverseStr = ''.join(list(inputStr)[::-1])

#print(reverseStr)

if inputStr.lower() == ''.join(list(inputStr)[::-1]):
    print('Palindrome')
else:
    print('Not Palindrome!!!')