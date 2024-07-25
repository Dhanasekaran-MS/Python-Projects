print(" WELCOME TO LOVE CALCULATOR ")
n1 = input("Enter your Name : \n")
n2 = input("Enter their Name : \n")
n = n1 + n2
n3 = n.lower()
a = 0
b = 0
a += n3.count("t")
a += n3.count("r")
a += n3.count("u")
a += n3.count("e")
b += n3.count("l")
b += n3.count("o")
b += n3.count("v")
b += n3.count("e")
d = str(a) + str(b)
c = int(d)
if c < 10 or c > 90:
  print(f"Your Score is :{c} , you go together like coke and mentos ")
if c > 40 and c < 50:
  print(f"Your Score is :{c} , you are alright together ")
else:
  print(f"your score is :{c}")

