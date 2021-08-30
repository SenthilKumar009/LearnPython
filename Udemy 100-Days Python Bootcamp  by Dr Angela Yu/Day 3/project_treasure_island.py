print("Welcome to Treasure Islan.")
print("your mission is to find the treasure")
direction = input("You're at cross road. Where do you want to go? Type 'Left' or 'Right'\n")

if direction.lower() == "left":
    decision1 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n")
    if decision1.lower() == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color you want to choose?\n")
        if door.lower() == "red":
            print("It's full of fire. Game Over!!!")
        elif door.lower() == "blue":
            print("You entered in to a room of beasts. Game Over!!!")
        else:
            print("You found the Treasure. You Won!!!")
    else:
        print("You got attacked by angry trout. Game Over!!!")
else:
    print("You fell into a hole. Game Over!!!")