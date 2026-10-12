# NUMBER GUESSING GAME


secretNumber=8
attempt=0

while attempt < 5:
    guessNumber=int(input("Guess the number please "))
    if guessNumber != secretNumber:
            print("try again")
    if guessNumber == secretNumber:
             print("Congratulation!!")
    if attempt > 5:
            print("GAME OVER")
            break