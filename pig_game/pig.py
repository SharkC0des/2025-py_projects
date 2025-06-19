import random
# fix the continue if player chooses Hold





choices = ["Roll", "Hold"]

def player():
    player_score = 0
    cpu_score = 0

    while True:
        roll_dice = input("Roll the dice? y/n: ").lower()
        if roll_dice == 'n':
            quit()

        elif roll_dice == "y":
            while True:
                num = random.randint(1, 6)
                if num == 1:
                    print(f"You rolled a {num}. Computer's turn!")
                    break
                else:
                    print(f"You rolled: {num}")
                    player_score += num
                    print(f"\nPlayer's Score: {player_score}\nComputer's Score: {cpu_score}")
                    if player_score >= 100:
                        print("You Wins!")
                        quit()

                # else computer's turn
                nxt_move = input("Roll or Hold? ")
                if nxt_move == "roll":
                    continue
                elif nxt_move == 'hold':
                    break

            while True:
                num = random.randint(1, 6)
                if num != 1:
                    print(f"\nComputer rolled: {num}")
                    cpu_score += num
                    print(f"Player Score: {player_score}\n"
                        f"Computer Score: {cpu_score}")
                    if cpu_score >= 100:
                        print("Computer Win!")
                        quit()

                    cpu_choice = random.choice(choices)
                    if cpu_choice == "Roll":
                        print(f"Computer chose to Roll\n")
                        continue
                    else:
                        print(f"Computer chose to Hold")
                        print(f"\nPlayer Score: {player_score}\n"
                              f"Computer Score: {cpu_score}")
                        break
        else:
            print("Invalid Input")




if __name__ == '__main__':
    # play = dice()
    # print(dice())
    player()