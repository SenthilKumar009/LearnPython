def pizza_order(pizza_size, add_pepperoni, extra_cheese):
    bill = 0
    if pizza_size == "S":
        bill = bill + 15
        if add_pepperoni == "Y":
            bill += 2
    elif pizza_size == "M":
        bill = bill + 20
        if add_pepperoni == "Y":
            bill += 3
    else:
        bill = bill + 25
        if add_pepperoni == "Y":
            bill += 3
    
    if extra_cheese == "Y":
        bill += 1
    
    print(f"Your Final Bill is: ${bill}")


pizza_size = input("What size pizza do you want? S or M or L :")
add_pepperoni = input("Do you want Pepperoni? Y or N :")
extra_cheese = input("Do you want Extra Cheese? Y or N :")

pizza_order(pizza_size, add_pepperoni, extra_cheese)