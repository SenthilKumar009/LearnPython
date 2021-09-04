import random

def getChar(nlist, number):
    pwd = []
    for n in range(0, number):
        pwd += random.choice(nlist)
    return pwd

letter = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['!', '@', '#', '$', '%', '^6', '&', '*']

print("Welcome to the password Generator!!!")
nLetter = int(input("How many letter should be there in the password\n"))
nNumber = int(input("How many number should be there in the password\n"))
nSymbol = int(input("How many symbol should be there in the password\n"))
password = []

password = getChar(letter, nLetter) + getChar(number, nNumber) + getChar(symbol, nSymbol)
random.shuffle(password)
#print(''.join(password))
print(f"Your Password is {''.join(password)}. Length of the password is {len(password)}.")

