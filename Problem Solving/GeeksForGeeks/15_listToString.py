word_list = ["Welcome", "to", "my", "World"]

sentence = ' '.join(word_list)
print(sentence +'.')

# using list comprehension
listToStr = ' '.join(map(str, word_list))
 
print(listToStr)