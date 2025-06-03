# Prompt: "Guess a number between 1 and 100:". If number not inputted, return "Enter a valid number". If number higher, return "Too high", If number lower, return, "too low".
import random


num = ((random.randint(1, 100)))
prompt = int(input("Guess a number between 1 and 100: "))
print(num)
while True:
        try:
            num_guessed = prompt
            if prompt > num:
                print("Too high")
                prompt = int(input(f"Guess a number between 1 and {num_guessed}: "))
            elif prompt < num:
                print("Too low")
                prompt = int(input(f"Guess a number between {num_guessed} and 100: "))
            else:
                print("Congrats, you guessed the number")
                exit()
        except ValueError:
            print("Enter a valid number")



#         prompt = int(input("Guess a number between 1 and 100: "))
# num = ((random.randint(1, 100)))
# while True:
#     try:

#         if prompt > num:
#             print("Too high")
#         elif prompt < num:
#             print("Too low")
#         else:
#             print("Congrats, you guessed the number")
#             exit()
#     except ValueError:
#         print("Enter a valid number")



"""
    num = ((random.randint(1, prompt)


"""

# """
#
#     - given try and except
#         Include condition in the try and not after the except
#         or else code will be unreachable/not initialized
#
# """
# Next time add a feature where given the inputted number, the program slices down the range.