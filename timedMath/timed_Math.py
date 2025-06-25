import math
import random

"""
Provide Math problems until user gets one correct

- While loop needed
- Random nums
- Arithmetic operators with random num of a length

- For future: Consider difficulty levels: 
    - For instance: Easy, deals with add/sub, multiplication/div... Hard is something complex
    
    
    
print equation into terminal, user inputs answers, if answer wrong: continue. If right, "quit"


"""
def addition(n1, n2):
    return f"{n1} + {n2} = "

def subtraction(n1, n2):
    return f"{n1} - {n2} = "

def multiply(n1, n2):
    return f"{n1} * {n2} = "

def divide(n1, n2):
    return f"{n1} / {n2} = "
def gameplay():
        count = 0 # Keeps Score
        while True:
            num1 = 0
            num2 = 0
            #functions
            add = addition(num1, num2)
            sub = subtraction(num1, num2)
            times = multiply(num1, num2)
            div = divide(num1, num2)

            op_list = [sub]
            choose = random.choice(op_list)

            # case for multiplication


            if choose == add:
                while True:
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                    add = addition(num1, num2)
                    add_sum = num1 + num2
                    if add_sum > 100:
                        continue
                    break
                equation = int(input(add))
                if add_sum == equation:
                    print("Correct")
                    count += 1
                    continue
                print("incorrect")
                break

            elif choose == sub:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                sub = subtraction(num1, num2)
                diff = num1 - num2
                while True:
                    if diff < 0:
                        diff = num2 - num1
                        sub = subtraction(num2, num1)
                        break
                    else:
                        break
                equation = int(input(sub))
                if diff == equation:
                    print("Correct")
                    count += 1
                    continue
                print("Incorrect")
                print(diff)
                break
            elif choose == times:
                num1 = random.randint(1, 12)
                num2 = random.randint(1, 12)
                times = multiply(num1, num2)
                product = num1 * num2
                equation = int(input(times))
                if product == equation:
                    print("Correct")
                    count += 1
                    continue
                print("Incorrect")
                break
            elif choose == div:

                while True:
                    num1 = random.randrange(1, 145)
                    num2 = random.randrange(1, 13)
                    if num1 / num2 > 12:
                        n2 = (num1 + 11) // 12
                    else:
                        n2 = num2

                    if num1 % n2 != 0 or num1 % num2 != 0:
                        continue
                    break

                div = divide(num1, n2)
                quotient = num1 / n2
                equation = int(input(f"{div}"))
            #print(quotient)
                if quotient == equation:
                    print("Correct")
                    count += 1
                    continue
                print("Incorrect")
                break

        print(f"You answered {count} problems correctly")






if __name__ == "__main__":
    gameplay()

