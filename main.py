def playerChoice():
    number = int(input("Are you player 1 or player 2? "))
    if number != 1 and number != 2:
        print("You are player " + number)


def hangMan():
    playerChoice()
    answer = input("Please enter your word for player 2: ")
    answerlist = []

    if len(answer) > 1 and answer.isalpha():
        answerlist.append(answer)
        answer = list(answerlist[0])
        display = []
        used = []
        incorrect = []
        used.extend(display)
        display.extend(answer)
        for i in range(len(display)):
            display[i] = "_"
        print(' '.join(display))
        print()
        count = 0

        while count > len(answer) and incorrect > 0:
            incorrect = 0
            count = 0
            guess = input("Guess a letter: ")
            guess = guess.lower()
            print(count)
            print(answerlist)

            for i in range(len(answer)):
                if answer[i] == guess and guess in used:
                    display[i] = guess
                    count = count + 1

                    used.remove(guess)

            if guess not in display:
                incorrect = incorrect - 1
                print("Wrong guess.")
            else:
                print("You ran out of guesses!")
        else:
            print("You need a word!")


if __name__ == '__main__':
    hangMan()


