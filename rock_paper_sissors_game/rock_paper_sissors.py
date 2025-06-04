import random

options = ('r', 'p', 's')

def get_user_choice():
    while True:
        user_choice = input("Choose r, p, or s: ")
        if user_choice in options:
            return user_choice
        else:
            print("Invalid Choice. Choose again")

def made_choice(user, cpu):
    print(f'You chose {user} ')
    print(f"Computer chose {cpu} ")
def winner(user, cpu):
    if user not in options:
        print("Invalid Choice!")


    if user == cpu:
        print("Draw!")

    elif (
            (user == "r" and cpu == "s") or
            (user == "p" and cpu == "r") or
            (user == "s" and cpu == "p")
    ):
        print("You Win!")
    else:
        print("Computer Wins!")

def gameplay():
    while True:

        user = get_user_choice()
        cpu = random.choice(options)
        made_choice(user,cpu)
        winner(user, cpu)

        want_continue = input("Would you like to continue? (y/n) ")
        if want_continue == "n":
            break

gameplay()






# options = ("r", "p", "s")
#
#
# cpu = random.choice(options)
# print(f"Computer chose {cpu}")
#
#
#
#
#
# while True:










