import random
game_title = 'Words, Words, Words'
file_path = './words.txt'

word_bank = []
with open(file_path, 'r') as readFile:
    for line in readFile:
        word_bank.append(line.lower().rstrip())

word_choice = random.choice(word_bank)

wrong_location = []
wrong_letters = []
max_turns = 5
player_turns = 0

print(f"Welcome to {game_title}\n")
print(f"There are {len(word_choice)} letters in the word\n")

def is_valid_guess(word: str): 
  return len(word) == len(word_choice) and word.isalpha()

while player_turns < max_turns:
    remaining_turns = max_turns - player_turns
    print(f"You have {remaining_turns} turns remaining\n")
    
    response = input("Enter your guess: ")
    
   
    if is_valid_guess(response):
      response = response.lower()
      
      if response == word_choice:
        print("Congratulations! You guessed the word correctly!")
        break
      
      checked_guess = ""
      
      for i, letter in enumerate(response):
        if letter == word_choice[i]:
          checked_guess+=letter + " "
          
          if letter in wrong_location:
            wrong_location.remove(letter)
        
        elif letter in word_choice:
          checked_guess+="_ "

          if letter not in wrong_location:
            wrong_location.append(letter)
          
        else:
          checked_guess+="_ "

          if letter not in wrong_letters:
            wrong_letters.append(letter)
          
      print(checked_guess)
      player_turns +=1
    else:
      print('Enter a valid five letter word')
   
    
    print("Misplaced letters: ", wrong_location)
    print("Incorrect letters: ", wrong_letters)
    
    if player_turns == max_turns:
      print(f"Sorry, you ran out of turns. The word was {word_choice}.")


      
      