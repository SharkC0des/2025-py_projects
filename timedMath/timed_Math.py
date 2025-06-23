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
def addition(num1,num2):
    return f"{num1} + {num2} = "

def subtraction(num1, num2):
    return f"{num1} - {num2} = "

def multiply(muilt_n_div):
    return f"{muilt_n_div} * {muilt_n_div} = "

def divide(mult_n_div):
    return f"{mult_n_div} / {mult_n_div} = "
def gameplay():
    count = 0
    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        mult_n_div = random.randint(1, 10)

        add = addition(num1, num2)
        sub = subtraction(num1, num2)
        times = multiply(mult_n_div)
        div = divide(mult_n_div)

        sum = num1 + num2
        diff = num1 - num2
        product = mult_n_div * mult_n_div
        quotient = mult_n_div / mult_n_div

        op_list = [add, sub, times, div]
        choose = random.choice(op_list)

        if choose == add:
            equation = int(input(choose))
            if sum == equation:
                print("Correct")
                count+= 1
                continue
            print("incorrect")
            break

        elif choose == sub:
            if num1 < num2:
                equation = int(input(f"{num2} - {num1} = "))
            equation = int(input(f"{num2} - {num1} = "))
            if diff == equation:
                print("Correct")
                count += 1
                continue
            print("Incorrect")
            break
        elif choose == times:
            equation = int(input(choose))
            if product == equation:
                print("Correct")
                count += 1
                continue
            print("Incorrect")
            break
        elif choose == div:
            if num1 < num2:
                equation = int(input(f"{num2} / {num1} = "))
            equation = int(input(choose))
            if math.floor(quotient) == math.floor(equation):
                print("Correct")
                count += 1
                continue
            print("Incorrect")
            break
    print(f"You answered {count} problems correctly")




if __name__ == "__main__":
    gameplay()

