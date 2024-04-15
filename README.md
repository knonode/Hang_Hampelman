# Challenge rules (sic!):

Create a Hangman game on Algorand from ```main.py``` OR using your own code.

Word dictionary MUST be ```bip_39_list.py```.

ASCII graphics of the hanged Hampelman - ```stages``` MUST be used. Other parts of GUI is up to you.

However, if your Hampelman figure is hanged by a Python snake, then you should use that graphics.

Player MUST pay at least 1 Algo to play. Reward for guessing right word is atm a random number from 0 to 9,
and is up to you to redefine.

If player guesses correct word, a small random reward is to be payed to player.

# Extra Challenge:

Algorand account mnemonics consist of 25 words, where the last word is the hash of the first 24.

If ```chosen_word``` is the 25th word of a known account, consider implementing this in the game.
