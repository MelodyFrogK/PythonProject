#행맨_단어 맞추기 게임

import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

#기본 설정
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

display = []

#logo
print(logo)

#Create blanks
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Clear the screen
    clear()
    
    if guess in display:
      print(f"You have already guessed {guess}")
      lives -= 1
      print(f"left your life: {lives}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"That's not in the word. You lose a life.\nleft your life: {lives}")
        #게임 종료
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #매칭 단어 디스플레이
    print(f"{' '.join(display)}")

    #모든 단어 맞추면 게임 종료
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #행맨 ASCII ART
    print(stages[lives])