year = int(input("Enter the year : "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Year {year} is a Leap year")
    else:
      print(f"Year {year} is Not a Leap year")
  else:
    print(f"Year {year} is a Leap year")
else:
  print(f"Year {year} is Not a Leap year")