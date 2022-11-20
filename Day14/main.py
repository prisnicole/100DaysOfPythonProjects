from random import sample
from art import logo, vs
from game_data import data 
from replit import clear
# print(len(data))
# select questions 
def select_pair():
  """
  randomly selects 2 unique elements in game_data 
  returns the elements in a list 
  """
  # generate random number btw 1 - 50
  # a sample() function for random sampling, randomly picking more than one element from the list without repeating elements. It returns a list of unique items chosen randomly from the list, sequence, or set. 
  pair = sample(data, 2)
  return pair

# select_pair
def generate_question(pair): 
  """
  Takes a list of 2 dictionary as input 
  Prints the values using the keys of the dictionary 
  """
  # access key in list of dic - index the list and enter key
  option_A = pair[0]
  option_B = pair[1]

  name_A = option_A['name']
  name_B = option_B['name']

  cty_A = option_A['country']
  cty_B = option_B['country']

  desc_A = option_A['description']
  desc_B = option_B['description']

  print(f"Compare A: {name_A}, a {desc_A}, from {cty_A} \n {vs} \n B: {name_B}, a {desc_B}, from {cty_B}.")


def compare_follower_count(guess, pair):
  """
  Takes the pair and user's guess as input 
  Returns True if user's guess is correct and False if incorrect 
  """
  if guess == 'A' and pair[0]['follower_count'] > pair[1]['follower_count']:
    return True 
  if guess == 'B' and pair[1]['follower_count'] > pair[0]['follower_count']:
    return True
  else: 
    return False 


def game():
  print(logo)
  score = 0
  is_correct = True
  while is_correct: 
    pair = select_pair()
    generate_question(pair)
    guess = input ("Which has a higher follower count? Type 'A' or 'B' \n Guess: ")
    is_correct = compare_follower_count(guess, pair)
    if is_correct: 
      score+= 1
      print(f"That's right! Current Score {score}")
      clear()
  
  print(f"That was a wrong guess, you lose! Your score is {score}")
  return 
  
  

game()
