import random

print("Welcome to the Rock Paper Scissors Game!!!")
print("You will be playing with the bot Until you said No")


play_continue = 1
options = ["Rock", "Paper", "scissors"]
draw = bot = user = 0

while(play_continue):
    user_choice = int(input("What to Select: Rock - 0 or Paper - 1 or Scissor - 2 ?\n"))
    
    if user_choice > 2:
        print("You have entered wrong choice! You Lost!!!")
        break
    
    bot_choice = random.randint(0,2)

    if bot_choice == user_choice:
        draw += 1
    elif (bot_choice == 0 and user_choice == 2) or (bot_choice == 2 and user_choice == 1) or (bot_choice == 1 and user_choice == 0):
        bot += 1
    else:
        user +=1

    print(f"User has picked {options[user_choice]}!!!")
    print(f"Bot has picked {options[bot_choice]}!!!")
    print(f"User won {user} matches. Bot won {bot} matches. {draw} matches are drawn")

    play_continue = int(input("Do you want to continue the Game? (Y - 1 N - Any): "))
