# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height**2

if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}. That is underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}. You are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}. You are obese.")
else:
    print(f"Your BMI is {round(bmi)}. You are clinically obese.")