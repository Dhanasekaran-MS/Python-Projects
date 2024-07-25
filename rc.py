print("welcome To The Rollercoaster Ride !")
height = int(input("What is your height in cm ? : "))
bill = 0
if height >= 120:
  print("You can ride the Rollercoaster")
  age = int(input("What is your Age ? : "))
  if age <= 10:
    bill = 70
    print("child tickets are 70")
  elif age <= 18:
    bill = 120
    print("Youth tickets are 120")
  elif age >= 45 and age <= 55:
    print("Everything is Ok have a free ride")
  else:
    bill = 150
    print("Adult tickets are 150")
  ph = input("Do You Want To Take Photo ? Y or N : ")
  if ph == "Y":
    bill += 50
  print(f"Your final bill is : {bill}")
else:
  print("Sorry , You can't Ride ")

