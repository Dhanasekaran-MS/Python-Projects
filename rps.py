import random
rock='''
_______         
| | | |/\       
|_|_|_|\ \       
|        /
\_______/
'''
paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

collection=[rock, paper, scissors]
get=int(input("What Do You Choose ? Type 0 for rock and 1 for paper and 2 for scissors : "))
if get>=3 or get<0 :
  print(" YOU HAVE TYPED AN INCORRECT NUMBER ")
else:
  print(collection[get])
print("Computer Choose : ")
rand=random.randint(0,2)
comp=collection[rand]
print(comp)   #0-rock 1-paper 2-scissors

if get==0 and rand==2 :      #rock > sci
  print(" YOU WON ")
elif get==2 and rand==0 :    #sci > rock
  print(" YOU LOSE ")
elif get>rand:               #sci>paper and paper>rock
  print(" YOU WON ")
elif get==rand:
  print(" TIE ")
else :
  print(" YOU LOSE ")
