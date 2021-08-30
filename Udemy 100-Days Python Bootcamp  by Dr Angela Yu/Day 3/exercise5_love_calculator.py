def calculate_score(name1, name2, phrase_word):
    name = name1.lower() + name2.lower()
    count = 0
    pharse_count = 0
    for i in range(0, len(phrase_word)):
        count += name.count(phrase_word[i])
        if count > 1:
            print(f"{phrase_word[i].upper()} occurs {count} times")
        else:
            print(f"{phrase_word[i].upper()} occurs {count} time")
        pharse_count += count
        count = 0
    print(f"Total: {pharse_count}")
    return pharse_count

def check_love(true_count, love_count):
    score = str(true_count) + str(love_count)
    #print(str(true_count) + str(love_count))
    if int(score) < 10 or int(score) > 90:
        print(f"Your score is {score}, you go together like coke and mentos!!!")
    elif int(score) > 40 and int(score) < 50:
        print(f"Your score is {score}, you are alright together!!!")
    else:
        print(f"Your score is {score}")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

true_count = calculate_score(name1, name2, "true")
love_count = calculate_score(name1, name2, "love")

check_love(true_count, love_count)