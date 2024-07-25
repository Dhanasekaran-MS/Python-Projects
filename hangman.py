import random
from hang_word import list
from hang_art import logo,stages
from replit import clear

end=False
choosen_word=random.choice(list)
n=len(choosen_word)
lives=6

print(logo)

print(f"track : {choosen_word}") 

display=[]
for i in range(n):
  display +="_"

while not end :
  guess=input("Guess a letter : ").lower()
  clear()
  
  if guess in display:
    print(f"You already guessed {guess}")
  
  for pos in range(n):
    letter=choosen_word[pos]
    if guess==letter:
      display[pos]=letter


  if guess not in choosen_word:
    print(f"You guessed {guess} , that's not in the word .You lose a life.")
    lives-=1
    print(stages[lives])
    if lives==0:
      end=True
      print(" YOU LOSE ")
      
  print(f"{' '.join(display)}")
  if "_" not in display:
    end=True
    print(" YOU WIN ")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
#hang_art
  
stages=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''' ,
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''     
]

logo="""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/        """              














#hang_word


list=["apple","orange","pineapple","mango","pomogranate","papaya","guava","cherry","blueberry","blackcurrent"]







  
  
    
