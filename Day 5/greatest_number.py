userinput = input().split()

a = 0

for num in userinput:
  if int(num) > a:
    a = int(num)

print("The Max number is : ",a)