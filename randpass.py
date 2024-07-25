import random
lett=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','0']
sym=['!','#','$','%','&','*','(',')']
print(" WELCOME TO PASSWORD GENERATOR ")
n_lett=int(input("How many letters would you like in your password : "))
n_num=int(input("How many numbers would you like in your password : "))
n_sym=int(input("How many symbols would you like in your password : "))

password_list=[]

for char in range(1,n_lett+1) :
  password_list +=random.choice(lett)
print(password_list)

for char in range(1,n_num+1) :
  password_list +=random.choice(num)
print(password_list)

for char in range(1,n_sym+1) :
  password_list +=random.choice(sym)

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for i in password_list:
  password+=i
print(f"Your random password is : {password}")
