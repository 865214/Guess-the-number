
import random
from art import logo
from replit import clear

number = range(1,101) # Declaring numbers range between 1 to 100
number_choice = random.choice(number) # randomly choosing the number beween 1 to 100

# We are declaring a function called guess_number.In this function we are doing all the required operaation for this program called Guess the number. 

def guess_number():
  print(logo)
  print('Welcome to the Number Guessing Game')
  print("I'm thinking of an number between 1 to 100")
  # We are declaring variable called difficulty. In this variable user has to choose which kind of difficilty they want(Easy or Hard). If they choose easy then they are getting 10 chances to guess the number coreectly.If they choose hard difficulaty then they are getting 5 chances to guess the number correctly.
  difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
  if difficulty == 'easy':
    chance = 10
    print(f'You have {chance} attempts to guess the number correctly')
  elif difficulty == 'hard':
    chance = 5
    print(f'You have {chance} attempt to guess the number')
    
  # We are declaring while loop for chances
  while chance:
    make_guess = int(input("Make a guess: "))
    chance -= 1 # Every wrong guesses we will substract 1 chance from the user.
    if chance == 0: # If the user uses all of there chances they will lose the game
      print("You've run out of guesses. You lose!")
      print(f"The actual number is {number_choice}") # We are showing user what is the actual number to guess.
    elif make_guess > number_choice: # If user guess the number which is higher than the random number between 1 to 100 they will deduct there chance and also they have to guess again the number.They will get a message the number is 'too high'
      print('Too high')
      print("Guess again")
      print(f"You have {chance} attempts to guess the number correctly")
    elif make_guess < number_choice:  # If user guess the number which is lesser than the random number between 1 to 100 they will deduct there chance and also they have to guess again the number.They will get a message the number is 'too low'
      print("Too low")
      print("Guess again")
      print(f"You have {chance} attempts to guess the number correctly")
    elif make_guess == number_choice:  # If user guess the number which is equal to the random number between 1 to 100 they will exit from the while loop.They will get a message the number is "You got it"
       chance = False
       print(f"You got it! Your answer is {make_guess}")
guess_number() # We are calling our function guess_number to run our game.

# For restarting our game we are using While loop with an user input if the user type 'y' then this will restart our game with clearing our previous game and restart out new game with logo.
while input("Guess The Number Again.Type 'y' to restart or Type 'n' to exit: ").lower()=='y':
  clear()
  guess_number()
    
    
  
