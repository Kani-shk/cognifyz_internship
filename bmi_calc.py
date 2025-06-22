# Task 5 – BMI Calculator

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return f"BMI = {bmi:.2f} → Underweight"
    elif 18.5 <= bmi < 24.9:
        return f"BMI = {bmi:.2f} → Normal weight"
    elif 25 <= bmi < 29.9:
        return f"BMI = {bmi:.2f} → Overweight"
    else:
        return f"BMI = {bmi:.2f} → Obese"

if __name__ == "__main__":
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    result = calculate_bmi(weight, height)
    print(result)
