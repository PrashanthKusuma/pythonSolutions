import random

print("Enter names with comma and space after each name till last name")
print("Ex: Name1, Name2, Name3")
name_string = input()
names = name_string.split(", ")
number_of_names = len(names)

buyer = names[random.randint(0, number_of_names-1)]

print(f'{buyer} will buy the cofee today.')