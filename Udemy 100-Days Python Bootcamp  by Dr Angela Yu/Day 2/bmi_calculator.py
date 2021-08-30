### 
# Program Name: BMI Calculator

height = float(input("Enter the Height (kg): "))
weight = float(input("Enter the Weight (m): "))

bmi = int(weight / (height ** 2))

print("Your BMI:" + str(bmi))