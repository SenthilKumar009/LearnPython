word_list = [1,2,3,4,5,6,7,8,9,10,11]

print(word_list.clear())

for i in range(len(word_list)):
    word_list.pop()

print(word_list)

word_list = [1,2,3,4,5,6,7,8,9,10,11]
word_list*= 0

print(word_list)