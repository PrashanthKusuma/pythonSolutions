print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tipPercent=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))

billPerPerson=round((bill+((bill*tipPercent)/100))/people,2)
billPerPerson="{:.2f}".format(billPerPerson)
print(f"Each person should pay: ${billPerPerson}")