weight = float(input("Enter your Weight "))
height = float(input("Enter your Height in meters "))

bmi = weight/height ** 2

# • Under 18.5 they are underweight
# • Over 18.5 but below 25 they have a normal weight
# • Over 25 but below 30 they are slightly overweight
# • Over 30 but below 35 they are obese
# • Above 35 they are clinically obese.

if bmi < 18.5:
  print(f"Your BMI is {bmi}, You are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, You have a normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, You are slightly overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, You are obese")
else:
  print(f"Your BMI is {bmi}, You are clinically obese")