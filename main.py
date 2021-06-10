word = input("Choose word: ")
guessed = []
wrong = []
tries = 5
# Turn Letters in blank dashes
# Guess letter

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess a letter: ", out)
    print(tries," guess are left")
    guess = input()

# check individual letters for/ guesses letters/ tries lost
    if guess in guessed or guess in wrong:
        print("You already guessed", guess)
    elif guess in word:
        print("The letter/word", guess)
        tries = tries
        guessed.append(guess)
    else:
        print("Incorrect")
        tries = tries - 1
        wrong.append(guess)

# guess the word
    if guess in guessed or guess == word:
        print("Correct you guessed the right word:", guess)
    elif guess in guessed or guess != word:
        print("Wrong word, Try again!")

    print()
    if tries:
        print("You guessed", word)
    else:
        print("No, the word is not", word)
        break





#if __name__ == '__main__':
#    print_hi('PyCharm')
