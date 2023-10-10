import random

def guess(x):
    random_number = random.randint(1, x)
    while(True):
        guess_number = int(input("Enter a Number between 1 and {0}: ".format(x)))
        if random_number == guess_number:
            print(f"You have guessed the correct Number {guess_number}")
            break
        elif guess_number < random_number:
            print('Sorry too low! Guess Again!!!')
        else:
            print('Sorry too High! Guess Again!!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input("Is your number higher or lower than " + str(guess) + "?")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your Number, {guess} correctly!!!')


computer_guess(100)