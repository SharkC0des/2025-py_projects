import random
# fix the continue if player chooses Hold





choices = ["Roll", "Hold"]

def player():
    dice_num = random.randint(1, 6)
    player_score = 0
    cpu_score = 0

    roll_dice = input("Roll the dice? y/n: ").lower()
    while True:
        if roll_dice == "y":
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










def cpu_func():
    dice_num = random.randint(1, 6)









# def dice():
#     choices = ['y', 'n']
#     player_score = 0
#     cmd_score = 0
#     cmd_choices = ['roll', 'hold']
#     cmd_response = random.choice(cmd_choices)
#     while True:
#         roll_dice = input("Roll the dice? y/n ").lower()
#         if roll_dice == 'y':
#             roll = random.randint(1,7)
#             print(f"You rolled a {roll}")
#             player_score = roll
#             print(f"Player's Score: {player_score}\nComputer's Score: {cmd_score}")
#             nxt_choice = input("Roll or Hold ").lower()
#
#
#
#
#
#
#
#
#             if roll == 1 or nxt_choice == 'Hold':
#                 print("Computer's turn")
#                 break
#             elif nxt_choice == "Roll":
#                 continue
#             else:
#                 break
#         elif roll_dice == 'n':
#             roll = random.randint(1,7)
#             print(roll)
#             cmd_score += roll
#             if roll != 1:
#                 print(roll)
#                 print(f"Computer chose to {cmd_response}")
#                 if cmd_response == 'roll':
#                     print(roll)
#                 else:
#                     print(f"Player Score: {player_score}\nComputer's Score: {cmd_score} ")
#             else:
#                 print("Player's turn")
#
#         elif player_score == 100:
#             print("Player Wins")
#             exit()
#         elif cmd_score == 100:
#             print("Computer Wins")
#             exit()
#         else:
#             print("Invalid Choice")


if __name__ == '__main__':
    # play = dice()
    # print(dice())
    player()