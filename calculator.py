#art

logo="""
 _____________________
|  _________________  |
| |     Dhana   0:  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


#main

# import art
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  # print(art.logo)
  print(logo)
  num1 = int(input("What's the first number : "))
  
  for symbols in operations :
    print(symbols)
  
  should_cont=True
  
  while should_cont:
    op = input("Pick an operation : ")
    num2 = int(input("What's the next number : "))
    calc = operations[op]
    answer = calc(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
    if input(f"Type'y' to continue calculating with {answer} , or type 'n' to start new calculation: ").lower() == "y" :
      num1 = answer
    else:
      should_cont = False
      calculator()
     
calculator()
