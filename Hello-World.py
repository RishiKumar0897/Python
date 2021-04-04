import random

randomNumber = random.randint(1,20)

userNumber = int(input("Enter a number from 1 to 20 "))

for x in range(20):

    if userNumber > 20:
        print("Try Again!")
        input("Please enter a number from 1 to 20")

        continue

    elif userNumber < 1:

        print("Try Again!")
        input("Please enter a number from 1 to 20")

        continue

    elif userNumber > randomNumber:
        print("Your number is too high. Try again.")
        input("Please enter a number from 1 to 20")

        continue

    elif userNumber < randomNumber:
        print("Your number is too low. Try again.")
        input("Please enter a number from 1 to 20")
        
        continue

    else:
        print("Congrats! You guessed correctly!")
        break



