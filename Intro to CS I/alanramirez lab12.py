from termcolor import colored
import random

words = "braid basis stick smell slump bring crowd offer allow taste medal slant fever match chair chest union think haunt visit".split()
orig = words[random.randint(0,len(words)-1)]
for attempt in range(1, 7):
    global guess_list
    guess = input(f'Enter guess #{attempt}: ').lower()
    while len(guess) != 5:
        guess = input(f'Error, re-enter guess #{attempt}: ').lower()
    guess_list = list(guess)
    orig_list = list(orig)
    if guess == orig:
        print(f'You guessed the word in {attempt} tr{"y" if attempt == 1 else "ies"}!')
        guess_list = list(colored(guess, "green"))
        break
    for index, letter in enumerate(guess_list):
        if letter == orig_list[index]:
            guess_list[index] = colored(letter, "green")
            orig_list[index] = "-"
    for index, letter in enumerate(guess_list):
        if letter in orig_list:
            guess_list[index] = colored(letter, "yellow")
            orig_list[orig_list.index(letter)] = "-"
    print("{}".format("".join(guess_list)))
print(f'Your final guess: {"".join(guess_list)}\nThe word: {orig}')