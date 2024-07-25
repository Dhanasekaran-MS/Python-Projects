for i in range(1,101) :
  if i%3==0 and i%5==0 :   #both divisible by 3 and 5
    print("FizzBuzz")
  elif i%3==0 :            #divisible by 3
    print("Fizz")
  elif i%5==0:      #divisible by 5
    print("Buzz")
  else :
    print(i)
