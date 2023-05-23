import random

word_list = ["aardvark", "baboon", "camel"]
display = []
guessed_letters = []
is_first_guess = True
player_lives = 5

def get_user_input(prompt):
    user_input = input(prompt).lower()
    return user_input

# generate random word from list and print
round_word = random.choice(word_list)
print("Welcome to Hangman!")

# print array of spaces for each letter in the word
for i in range(len(round_word)):
    display.append('_')
print(display)

# game loop starts
while player_lives > 0:
    found_in_word = False
    if is_first_guess:
        user_guess = get_user_input("Guess a letter: ")
        for i in range(len(round_word)):
            if user_guess == round_word[i]:
                display[i] = user_guess
                is_first_guess = False
                found_in_word = True
            else:
                is_first_guess = False
        if not found_in_word:
            player_lives -= 1
            guessed_letters.append(user_guess)
        else:
            guessed_letters.append(user_guess)
    else:
        user_guess = get_user_input("Guess again: ")
        for i in range(len(round_word)):
            if user_guess == round_word[i]:
                display[i] = user_guess
                found_in_word = True
        if not found_in_word:
            player_lives -= 1
            guessed_letters.append(user_guess)
        else:
            guessed_letters.append(user_guess)
    if found_in_word:
        print(f"Correct! Guesses left: {player_lives}")
    else:
        print(f"Incorrect! Guesses left: {player_lives}")
    print(display)
    print(f"Guessed letters: {guessed_letters}\n")
    if player_lives == 0:
        print("You lose!")
    if '_' not in display:
        print("You win!")
        player_lives = 0



