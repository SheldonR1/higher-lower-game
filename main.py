from art import logo
from game_data import data
from replit import clear
import random
INPROGRESS=True

numOption=len(data) 

def getOptions():
  comparison1=random.randint(0,numOption)
  comparison2=random.randint(0,numOption)
  print(f"Who has more followers? \n ==================================")
  print(f"A: {data[comparison1]['name']}, {data[comparison1]['description']}, from {data[comparison1]['country']}")
  print(f" --------- vs --------")
  print(f"B: {data[comparison2]['name']}, {data[comparison2]['description']}, from {data[comparison2]['country']} \n")
  GoodInput=False
  while not GoodInput:
    userInput=input("Which option has more followers? (A or B): ").upper()
    if (userInput=='A') | (userInput=='B'):
      break
  if userInput=='A':
    if data[comparison1]['follower_count']  > data[comparison2]['follower_count']:
      print(f"YOU ARE CORRECT: {data[comparison1]['name']} has {data[comparison1]['follower_count']} while {data[comparison2]['name']} has {data[comparison2]['follower_count']}")  
    elif data[comparison1]['follower_count']  < data[comparison2]['follower_count']:
      print(f"YOU ARE INCORRECT: {data[comparison1]['name']} has {data[comparison1]['follower_count']} while {data[comparison2]['name']} has {data[comparison2]['follower_count']}")
    else:
      print(f"IT'S A TIE: {data[comparison1]['name']} has {data[comparison1]['follower_count']} while {data[comparison2]['name']} has {data[comparison2]['follower_count']}")
  if userInput=='B': 
   if data[comparison1]['follower_count']  < data[comparison2]['follower_count']:
      print(f"YOU ARE CORRECT: {data[comparison1]['name']} has {data[comparison1]['follower_count']} while {data[comparison2]['name']} has {data[comparison2]['follower_count']}")  
   elif data[comparison1]['follower_count']  > data[comparison2]['follower_count']:
      print(f"YOU ARE INCORRECT: {data[comparison1]['name']} has {data[comparison1]['follower_count']} while {data[comparison2]['name']} has {data[comparison2]['follower_count']}")
   else:
      print(f"IT'S A TIE: {data[comparison1]['name']} has {data[comparison1]['follower_count']} while {data[comparison2]['name']} has {data[comparison2]['follower_count']}")


def playAgain():
  global INPROGRESS
  userInput=input("Would you like to play again? (Y/N):").upper()
  if userInput=='Y':
    clear()
  elif userInput=='N':
    INPROGRESS=False 
    print("Good bye")
  else:
    playAgain()

  
def Start():
  while INPROGRESS:
   print(logo)
   getOptions()
   playAgain()


Start()
