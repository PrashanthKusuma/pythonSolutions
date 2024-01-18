userinput = int(input())

sum = 0

for num in range(1, userinput + 1):
  if num % 2 == 0:
    sum += num

print(f"sum of even numbers till {userinput} is : ", sum)
