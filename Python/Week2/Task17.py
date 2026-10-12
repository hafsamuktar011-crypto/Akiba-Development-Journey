# NUMBER GUESSING GAME

secretNumber = 8
attempt = 0

while attempt < 5:
    # Ask for a new guess on each loop iteration
    guessNumber = int(input("Guess the number please: "))

    # Count each guess as one attempt
    attempt += 1

    if guessNumber == secretNumber:
        print("Congratulations!!")
        break

    if attempt == 5:
        print("GAME OVER")
    else:
        print("Try again")