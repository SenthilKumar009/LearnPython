###

# Project Name: Hide Treasure
# Author      : Senthil Kumar Kanagaraj
# Date        : 31-Aug-2021

#from emoji import emojize

row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

location = (input("Where do you want to hide Treasure: "))

horizantal = int(location[0])
vertical = int(location[1])

map[horizantal-1][vertical-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
