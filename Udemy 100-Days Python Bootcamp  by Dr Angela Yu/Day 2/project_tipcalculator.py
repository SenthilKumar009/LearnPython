###
# Project Name  :  Tip Calculator
# Author        :  Senthil Kumar Kanagaraj
# Date          :  29-Aug-2021

def tip_calculator(bill, members, tip):
    return (tip/100 * bill + bill) / members

bill = float(input("What is the total amount of the bill: "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
members = int(input("How many members to split the bill: "))

print(f"Each person Should pay {tip_calculator(bill, members, tip)}")