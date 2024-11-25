import random
random_number = random.randint(1,100)
lives = 3

while lives >0:
    try:
        guess = int(input("Guess my number: "))

        if guess == random_number:
            print("You're correct!")
            break

        elif guess > random_number:
            print(str(guess) + "Your number is too high!")

        else:
            print(str(guess) + "Your number is too low!")

        lives -= 1
        print("Lives remaining: " + str(lives))

    except Exception:
        print("Enter only number!")


else:
    print("you're dead! :>  My number was", random_number)

