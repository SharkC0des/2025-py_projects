import random
# fix the continue if player chooses Hold





choices = ["Roll"]

def player():
    player_score = 0
    cpu_score = 0
    plyr_turn = 0
    cpu_turn = 0

    while True:

        roll_dice = input("Roll the dice? y/n: ").lower()
        if roll_dice == 'n':
            quit()

        elif roll_dice == "y":
            while True:
                num = random.randint(1, 6)

                if num == 1:
                    print(f"You rolled a {num}. Computer's turn!")
                    player_score -= plyr_turn
                    print(f"\nPlayer's Score: {player_score}\nComputer's Score: {cpu_score}")
                    plyr_turn = 0
                    break
                else:
                    print(f"You rolled: {num}")
                    player_score += num
                    print(plyr_turn)
                    print(f"\nPlayer's Score: {player_score}\nComputer's Score: {cpu_score}")
                    if player_score >= 100:
                        print("You Wins!")
                        quit()

                # else computer's turn
                nxt_move = input("Roll or Hold? ")
                if nxt_move == "roll":
                    plyr_turn += num
                    continue
                elif nxt_move == 'hold':
                    plyr_turn = 0
                    break

            while True:
                num = random.randint(1, 6)
                if num == 1:
                    print(f"Computer rolled a {num}. You're turn!")
                    cpu_score -= cpu_turn
                    print(f"\nPlayer's Score: {player_score}\nComputer's Score: {cpu_score}\n")
                    cpu_turn = 0
                    break

                print(f"\nComputer rolled: {num}")
                cpu_score += num
                print(f"Player Score: {player_score}\n"
                    f"Computer Score: {cpu_score}\n")
                if cpu_score >= 100:
                    print("Computer Win!")
                    quit()

                cpu_choice = random.choice(choices)
                if cpu_choice == "Roll":
                    print(f"Computer chose to Roll")
                    cpu_turn += num
                    continue
                else:
                    print(f"Computer chose to Hold\n")
                    cpu_turn = 0
                    break
        else:
            print("Invalid Input")




if __name__ == '__main__':
    # play = dice()
    # print(dice())
    player()