# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

size = input()
pepparoni = input()
extra_cheese = input()
price = 0

if size == 'S':
  price = 15
elif size == 'M':
  price = 20
elif size == 'L':
  price = 25

if pepparoni == 'Y':
  if size == 'S':
    price += 2
  elif size == 'M':
    price += 3
  elif size == 'L':
    price += 3

if extra_cheese == 'Y':
  price += 1

print(f'Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${price}.')