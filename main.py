import random
import os
from data import data
from art import logo,vs


def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def formate(A):
    name = A["name"]
    description = A["description"]
    country = A["country"]
    return f"{name}, a {description} from {country}"

def checkGuess(guess, A, B):
    if(A['follower_count'] > B['follower_count']):
        return guess == 'A'

    return guess == 'B'

game_on = True
second = random.choice(data)
score = 0
print(logo)
while game_on:
    
    first = second
    second = random.choice(data)
    

    print('\n  Compare A: ' + formate(first))
    print('\n' + vs)
    print('\n  Compare B: ' + formate(second))
    
    guess = input('\n  Who has more followers? A or B:   ').upper()
    
    screen_clear()
    print(logo)
    if checkGuess(guess, first, second) == False:
        game_on = False
        
        print(f"\n  sorry! That's wrong. Final score: {score}")
        break

    else:
        print(f"\n  You're right! Current score: {score}")

    score += 1


