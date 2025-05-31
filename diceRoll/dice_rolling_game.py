# Game ask "Roll the dice? (y/n)" If "y" returns two numbers in a tuple "()" , if "n" return thanks for playing. If not "y" or "n", reeturn "Invalid choice!"
import sys
import random
count = 0
while True:
    prompt = input("Roll the dice? (y/n) ").lower()
    if prompt == 'y':
        nums = (random.randrange(1,7), random.randrange(1,7))
        print(nums)
        count += 1
        print(f"You rolled {count} times!")
    elif prompt == 'n':
        print("Thanks for Playing")
        break
    else:
        print("Invalid choice!")

