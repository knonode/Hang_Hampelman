import random
from hangman_art import stages, logo, asci_num
from bip_39_list import bip_39

end_of_game = False
guessed_chars = []
lives = 6
prize = random.choice(asci_num)
chosen_word = random.choice(bip_39)
print(chosen_word)
print(logo)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(''.join(display))
print(stages[6])

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guessed_chars += guess
    for pos in range(len(chosen_word)):
        char = chosen_word[pos]
        if char == guess:
            display[pos] = char
    if guess not in chosen_word:
        lives -= 1
        print(f"{logo}You lose one life, you have {lives} lives left")

        print(f'Letters guessed: {' '.join(guessed_chars)}')
        if lives == 0:
            end_of_game = True
            print(f'Well done, Hampelman is hanged.'
                  f' Pay 1A for your show ticket.\nThe word was {chosen_word.upper()}')
    print(''.join(display))
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print(f"You win {prize}")
        def ch(h, x, y): # iterative Algorand logo pattern by Tomasso
            return '*' if y >= 0 and x in [h - y, h + y] else ''
        def draw_algorand(h1):
            h2 = h1 // 2 + 1
            for y in range(h1):
                print(''.join(
                    '*' if ch(h1, x, y) == '*' or ch(h2, x - (h1 - h2) * 2, y - (h1 - h2)) == '*' else ' ' for x in
                    range(h1 * 2)))
        print()
        draw_algorand(asci_num.index(prize))