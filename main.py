def change_colour(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

title = f"{change_colour('red')}={change_colour('white')}={change_colour('blue')}= {change_colour('yellow')}Music App {change_colour('blue')}={change_colour('white')}={change_colour('red')}="

print(f"        {title:^35}")
print(f"🔥▶️\t{change_colour('white')}Radio Gaga")
print(f"\t{change_colour('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{change_colour('white')}{prev:<35}")
print(f"{change_colour('green')}{next:^35}")
print(f"{change_colour('purple')}{pause:>35}")


print()
print()
print()
print()
text = "WELCOME TO"
print(f"{change_colour('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{change_colour('blue')}{text:^35}")
print()

text = "Definitely not a rip off"
print(f"{change_colour('yellow')}{text:>35}")
text = "a certain other social"
print(f"{change_colour('yellow')}{text:>35}")
text = "networking site"
print(f"{change_colour('yellow')}{text:>35}")
print()

text = "Honest."
print(f"{change_colour('red')}{text:^35}")
print()

text = "Username: "
username = input(f"{change_colour('white')}{text:^35}")
text = "Password: "
username = input(f"{change_colour('white')}{text:^35}")