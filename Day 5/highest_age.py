# 156 178 165 171 187
# total height = 857
# number of students = 5
# average height = 171

userinput = input().split(" ")

height = 0

for i in userinput:
  height += int(i)

print("total height = ", height)
print("number of students =", len(userinput))
print("average height = ", height / len(userinput))
