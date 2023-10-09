# Write your code here
import random


words = ["python", "java", "swift", "javascript"]
won = 0
lost = 0


def title_game():
    print("H A N G M A N")


def menu_game():
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, '
              'and "exit" to quit: ')
        option = input()
        if option == "play":
            word_win = word_guess()
            gaming(word_win)
        elif option == "results":
            print(f"You won: {won} times.\nYou lost: {lost} times.")
            menu_game()
        elif option == "exit":
            exit()


def word_guess():
    word_random = random.choice(words)
    return word_random


def replace_occurrences(word_win__, letter_ok_, word_gamer_):
    return "".join([word_win__[i]
                    if word_win__[i] in letter_ok_ else word_gamer_[i]
                    for i in range(len(word_win__))])


def gaming(word_win_):
    global won
    global lost
    attempts = 1
    word_gamer = ("-" * len(word_win_))
    letter_ok = set()
    letter_not = set()
    while attempts <= 8:
        print(word_gamer)
        letter = input(f"Input a letter: ")
        if len(letter) > 1 or len(letter) == 0:
            print("Please, input a single letter.")
            continue
        elif letter.isalpha() is False:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        elif not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if letter in word_win_:
            if letter in letter_ok:
                print("You've already guessed this letter.")
            else:
                letter_ok.add(letter)
                word_gamer = replace_occurrences(word_win_, letter_ok, word_gamer)
        else:
            if letter in letter_not:
                print("You've already guessed this letter.")
            else:
                letter_not.add(letter)
                print("That letter doesn't appear in the word.")
                attempts += 1
        if word_gamer == word_win_:
            print(f"You guessed the word {word_gamer}!")
            print("You survived!")
            won += 1
            menu_game()
        elif attempts == 9:
            print("You lost!")
            lost += 1
            menu_game()


title_game()
menu_game()

