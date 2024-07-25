print(" Welcome To Tresure Island ")
print("Your Mission Is To Find The Treasure")
path = input(
  "You are at the crossroads , which direction do you want to go 'LEFT or RIGHT' ? : "
).lower()
if path == "left":
  print(" CONGRADULATIONS , You are good to go")
  sea = input("Now you are near sea , Do you you want to 'SWIM or WAIT' ? : ").lower()
  if sea == "wait":
    print(" CONGRADULATIONS , Next level : ")
    door = input("Choose the door 'RED or BLUE or YELLOW' ? :  ").lower()
    if door == "yellow":
      print(" CONGRADULATIONS !")
      print("You Reached The Treasure")
    else:
      print(" GAME OVER ")
  else:
    print(" GAME OVER ")
else:
  print(" GAME OVER ")

