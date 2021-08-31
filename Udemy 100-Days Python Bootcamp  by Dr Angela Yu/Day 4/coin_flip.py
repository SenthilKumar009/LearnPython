import random

user_cash = 10000
bot_cash = 10000

def check_choice(choice):
    random_side = random.randint(0,1)
    if random_side == choice:
        return "User"
    else:
        return "Bot"

print("Welcome to the Casino. Hear You gonna be a Millionire!!!")
print("You will have $1000 Dollers in your Hand and you Start play with the Bot. Who goes empty first they lost and the other Win")


play_continue = 1

while(True):
    if play_continue == 1:
        while(user_cash > 0 and bot_cash > 0):
            if user_cash >= bot_cash:
                cash = int(input(f"How much cash you wanna put for bet? (1-{bot_cash})\n"))
            else:
                cash = int(input(f"How much cash you wanna put for bet? (1-{user_cash})\n"))
            
            choice = int(input("What's your call? (0 - H/ 1 - T)\n"))
            winner = check_choice(choice)

            if winner == "User":
                user_cash += cash
                bot_cash -= cash
            else:
                user_cash -= cash
                bot_cash += cash
        print(f"The Winner is {winner}.")
    
        play_continue = int(input("Do you Want to play next Round? (Y - 1/ N- 0)\n"))
    else:
        print("Thank You!!!")
        break
    