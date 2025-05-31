# Prompt: "Guess a number between 1 and 100:". If number not inputted, return "Enter a valid number". If number higher, return "Too high", If number lower, return, "too low".
import random

num = ((random.randint(1, 100)))
while True:
    try:
        prompt = int(input("Guess a number between 1 and 100: "))
        if prompt > num:
            print("Too high")
        elif prompt < num:
            print("Too low")
        else:
            print("Congrats, you guessed the number")
            exit()
    except ValueError:
        print("Enter a valid number")




