name1 = input()
name2 = input()

combined_names = name1 + name2
combined_names = combined_names.lower()

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')

total_love = l + o + v + e

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

is_it_true = t + r + u + e

true_love= str(is_it_true) + str(total_love)

print(f"Your score is {true_love}")