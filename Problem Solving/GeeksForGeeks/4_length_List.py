
word_list = [1,2,3,4,5,6,7,8,9,10]

print(len(word_list))

total = 0
for word in word_list:
    total += 1
print(total)

list_len = sum( 1 for word in word_list)
print(list_len)