year = int(input("Enter the year to check whether Leap year or Not"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It's a Leap Year")
    else:
      print("Not a Leap Year")
  else:
    print("It's a Leap Year")
else:
  print("Not a Leap Year")

