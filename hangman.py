import random
from word import word_list
from hangman_arts import logo,stages
end = False
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

display = []
for letter in range(word_length):
    display += "_"


while "_" in display:
    guess = input("Guess the Letter : ").lower()

    if guess in display:
        print(f"You have already guessed: {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end = True
            print("You Lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end = True
        print("You Win")

    print(stages[lives])
