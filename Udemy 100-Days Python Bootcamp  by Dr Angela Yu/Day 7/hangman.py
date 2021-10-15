################################################ 
# Program Name: Hangman                        #
# Author      : Senthil Kumar Kanagaraj        #
# Date        : 15-Oct-2021                    #
################################################

# import libraries
import random

# Assign and select the words
words = ['arabic', 'canada', 'data', 'apartment']
choosen_word = random.choice(words)
print(f"The word {choosen_word} has been selected")

choosen_word_length = len(choosen_word)
word_form =""
for i in range(0, choosen_word_length):
    word_form += "_"

print(f"The word you have to find {word_form}")

# Assign variables 
isContinue = 1
isAlive = 6

# Check the letter in the choosen word
def check_letter(guess, choosen_word):
    if guess in choosen_word:
        return 1
    else:
        return 0

def find_location(guess, choosen_word):
    location = list()
    for i in range(0, len(choosen_word)):
        if guess == choosen_word[i]:
            location.append(i)
    return location

def append_letter(choosen_word, guess, word_form):
    location = find_location(guess, choosen_word)
    #print(location)
    #position = choosen_word.index(guess)
    for i in range(0,len(location)):
        temp = list(word_form)
        temp[int(location[i])] = guess
        word_form = "".join(temp)
    return word_form

    #print(word_form.replace(choosen_word.index(guess), guess))

while(True):
    guess = input("Guess the Word: ").lower()
    if len(guess) > 1:
        print("You have entered more than one charactor. Please enter ONE letter!")
        continue
    else:
        letter_check = check_letter(guess, choosen_word)
        
    if letter_check == 1:
        word_form = append_letter(choosen_word, guess, word_form)
        print(word_form)
    else:
        isAlive -= 1
        if isAlive == 0:
            print("Handman is Dead!!! You have lost the Game!!!")
            break
        print(f"You have {isAlive} chances left!!!") 
        print(word_form)    

    if "_" not in word_form:
        print(f"You found the word {choosen_word}, and you have Won the Game!!!")
        break
        