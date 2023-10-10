import random

def play():

    user_count = 0
    computer_count = 0

    while (True):
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])
        
        if (user == 'r' and computer == 'p') or (user == 's' and computer == 'r') or (user == 'p' and computer == 's'):
            computer_count += 1
            print(f'Computer : {computer_count}, User: {user_count}')
        elif (computer == 'r' and user == 'p') or (computer == 's' and user == 'r') or (computer == 'p' and user == 's'):
            user_count += 1
            print(f'Computer : {computer_count}, User: {user_count}')

        if user_count ==3 or computer_count == 3:
            break

    if user_count == 3:
        print(f'User Wins by {user_count} - {computer_count}')
    elif computer_count == 3:
        print(f'Computer Wins by {computer_count} - {user_count}')
    else:
        print(f'Match Tie, {computer_count} - {user_count}')

play()