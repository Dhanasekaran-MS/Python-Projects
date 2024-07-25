print("Welcome to Python Pizza Deliveries ! ")
size = input("What size of pizza  do you want ? S , M , L : ")
addpep = input("Do you want Pepperoni ? Y or N : ")
extracheese = input("do you want extra cheese ? Y or N : ")
bill = 0
if size == "S":
  bill += 70
  print("you have ordered a small size pizza")
elif size == "M":
  bill += 100
  print("you have ordered a medium size pizza")
elif size == "L":
  bill += 150
  print("you have ordered a Large size pizza")
if addpep == "Y":
  if size == "S":
    bill += 10
  else:
    bill += 15
if extracheese == "Y":
  bill += 5
print(f"The Total Bill is : {bill}")

