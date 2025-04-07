# bmi_calculator.py
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
category = get_category(bmi)

print(f"Your BMI is: {bmi} ({category})")