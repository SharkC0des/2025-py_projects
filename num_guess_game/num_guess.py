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



# """
#
#     - given try and except
#         Include condition in the try and not after the except
#         or else code will be unreachable/not initialized
#
# """
# Next time add a feature where given the inputted number, the program slices down the range.