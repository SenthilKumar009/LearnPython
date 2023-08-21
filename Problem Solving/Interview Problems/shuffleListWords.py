from random import shuffle

def shuffle_word(text_list):
    text_list = list(text_list)
    shuffle(text_list)
    return ''.join(text_list)

text_list = ['Python', 'list', 'exercises', 'practice', 'solution'] 
print("Original list:")
print(text_list)
print("\nAfter scrambling the letters of the strings of the said list:")
result =  [shuffle_word(word) for word in text_list]
print(result) 
