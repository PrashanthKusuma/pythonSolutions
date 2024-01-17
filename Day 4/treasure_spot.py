line1 = ["🟩", "🟩", "🟩"]
line2 = ["🟩", "🟩", "🟩"]
line3 = ["🟩", "🟩", "🟩"]

userinput = input("Enter the destination : ")

letter = userinput[0].lower()
number = userinput[1]

row = ""
column = int(number)-1

if letter == 'a':
  row = 0
elif letter == 'b':
  row = 1
else:
  row = 2

lines = [line1, line2, line3]

lines[column][row] = "❌"

print(f'{line1}\n{line2}\n{line3}')