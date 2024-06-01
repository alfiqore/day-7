import random
from hangman_words import word_list 
from hangman_art import stages, logo
print(logo)
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
print(stages[6])

blank_word = []
for letter in chosen_word:
  blank_word.append("_")

tries = 6

win = False

while win != True:
    print("You have " + str(tries) + " tries left.")

    guess = input("Guess a letter: ").lower()
    if guess in blank_word:
        tries -=1
        print("You already guessed this letter.")

    for letter in range(len(chosen_word)):
        letter_in_word = chosen_word[letter]
        if letter_in_word == guess:
            blank_word[letter] = guess


    if guess in chosen_word:
        print(stages[tries])
    else:
        tries -= 1
        print(stages[tries])

    final_word = " ".join(blank_word)
    print(final_word)
    if "_" not in blank_word:
        win = True
        print("you win")
    elif tries == 0:
        print(stages[0])
        print("You lose!")
        break

