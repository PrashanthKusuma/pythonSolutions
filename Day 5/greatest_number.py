userinput = input().split()

a = 0

for num in userinput:
  if a < int(num):
    a = int(num)

print("The Max number is : ",a)