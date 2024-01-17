import random
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]
choices_string = ['rock', 'paper', 'scissors']
userchoice = int(
    input(
        'What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n'
    ))
if userchoice <= 3:
  userinput = choices[userchoice - 1]
  systeminput = choices[random.randint(0, len(choices) - 1)]
  print(userinput)
  print("System:\n")
  print(systeminput)
  if userinput == rock and systeminput == scissors:
    print("user won")
  elif userinput == scissors and systeminput == paper:
    print("user won")
  elif userinput == paper and systeminput == rock:
    print("user won")
  elif systeminput == rock and userinput == scissors:
    print("user lose, game over")
  elif systeminput == scissors and userinput == paper:
    print("user lose, game over")
  elif systeminput == paper and userinput == rock:
    print("user lose, game over")
  else:
    print("it's a draw")
else:
  print("invalid input")
