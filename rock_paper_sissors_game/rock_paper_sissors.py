import random

options = ("r", "p", "s")


cpu = random.choice(options)
print(f"Computer chose {cpu}")

while True:
    prompt = input("Type: r, p, or s: ").lower()
    if prompt not in options:
        print("Invalid Choice!")
        continue

    if prompt == cpu:
        print("Draw!")

    elif (
            (prompt == "r" and cpu == "s") or
            (prompt == "p" and cpu == "r") or
            (prompt == "s" and cpu == "p")
    ):
        print("You Win!")
    else:
        print("Computer Wins!")

    want_continue = input("Would you like to continue? y/n ")
    if want_continue == "n":
        break




















        # if prompt == "r" and cpu != "p":
        #     print(prompt)
        #     print(cpu)
        #     print("You Win!")
        # else:
        #     print("Computer Wins!")
        #
        # if prompt == "p" and cpu != "s":
        #     print("You Win!")
        # else:
        #     print("Computer Wins!")
        #
        # if prompt == "s" and cpu != "r":
        #     print("You Win!")
        # else:
        #     print("Computer Wins!")

