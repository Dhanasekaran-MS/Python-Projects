#logo



logo="""
   ____                       _____ _            _   _                 _               
  / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                                                                

"""

#main


import random
# import art

easy_level = 10
hard_level = 5


def check_answer(guess,num,turns) :
  if guess > num :
    print("Your Guess is too High !")
    return turns -1
  elif guess < num :
    print("Your Guess is too Low !")
    return turns -1
  else : 
    print(f"You Guesssed the Number : {guess}")

def set_difficulty() :
  level = input("Choose the Difficulty 'easy' or 'hard' : ").lower()
  if level == "easy" :
    return easy_level
  elif level =="hard" :
    return hard_level
  
    
def game():
  # print(art.logo)
  print(logo)
  print("Welcome To Guess The Number Game !")
  print("I'm Guesing a Number From 1 to 100 .")
  
  num = random.randint(1,101)
  
  turns = set_difficulty()
  guess = 0  
  while guess != num :
    if turns == 0 :
      print("\nYou ran out of attempts , You Lose")
      return
    print(f"\nYou Have {turns} attempts left !")
    guess = int(input("Guess the Number : "))
    turns = check_answer(guess, num, turns)
    
game()
