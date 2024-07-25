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
  num1 = float(input("What's the first number : "))
  
  for symbols in operations :
    print(symbols)
  
  should_cont=True
  
  while should_cont:
    op = input("Pick an operation : ")
    num2 = float(input("What's the next number : "))
    calc = operations[op]
    answer = calc(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
    if input(f"Type'y' to continue calculating with {answer} , or type 'n' to start new calculation: ").lower() == "y" :
      num1 = answer
    else:
      should_cont = False
      calculator()
     
calculator()