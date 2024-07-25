def prime_num_checker(number):
  is_prime=True
  for i in range(2,number):
    if number%i==0:
      is_prime=False
  if is_prime:
    print("It's a Prime Number")
  else :
    print("It's not a Prime Number")

test=int(input("Enter The Number To Check Whether It iS Prime Or Not : "))
prime_num_checker(test)
