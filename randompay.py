import random
names=input("Give me everbody's names separated by comma : ")
name =names.split(", ")
print(names)
print(name)
x=len(name)
rand=random.randint(0,x-1)
print(f"The person going to pay bill is : {name[rand]}")
