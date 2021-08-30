def bmi_calculator(weight, height):
    bmi = round(weight / (height ** 2), 2)

    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are Underweight")
    elif bmi > 18.5 and bmi < 25:
        print(f"Your BMI is {bmi}, you are Normal Weight")
    elif bmi > 25 and bmi < 30:
        print(f"Your BMI is {bmi}, you are OverWeight")
    elif bmi > 30 and bmi < 35:
        print(f"Your BMI is {bmi}, you are Obese")
    else:
        print(f"Your BMI is {bmi}, you are Clinically Obese")


weight = float(input("Enter the Weight (kg): "))
height = float(input("Enter the Height (m): "))
bmi_calculator(weight, height)