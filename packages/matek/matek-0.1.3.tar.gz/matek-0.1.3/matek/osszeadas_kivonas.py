#!/usr/bin/python3

import random
import sys
import os

def generate_problem():
    op = random.choice(['+', '-'])
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    if op == '-' and num1 < num2:
        num1, num2 = num2, num1  # Ensure positive result in subtraction
    result = num1 + num2 if op == '+' else num1 - num2
    
    missing_part = random.choice(['num1', 'num2', 'result'])
    
    if missing_part == 'num1':
        display1 = ['_'] * 3
        display2 = list(f"{num2:03d}")
        display_result = list(f"{result:03d}")
        answer = list(f"{num1:03d}")
    elif missing_part == 'num2':
        display1 = list(f"{num1:03d}")
        display2 = ['_'] * 3
        display_result = list(f"{result:03d}")
        answer = list(f"{num2:03d}")
    else:
        display1 = list(f"{num1:03d}")
        display2 = list(f"{num2:03d}")
        display_result = ['_'] * 3
        answer = list(f"{result:03d}")
    
    return op, display1, display2, display_result, answer

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(display1, display2, display_result, answer, op):
    user_input = ['*'] * 3
    for i in range(2, -1, -1):  # Jobbról balra
        while True:
            clear_screen()
            if display1[0] == '_':
                print(f"\n  {' '.join(user_input)}\n{op} {' '.join(display2)}\n  ---\n  {' '.join(display_result)}\n")
            elif display2[0] == '_':
                print(f"\n  {' '.join(display1)}\n{op} {' '.join(user_input)}\n  ---\n  {' '.join(display_result)}\n")
            elif display_result[0] == '_':
                print(f"\n  {' '.join(display1)}\n{op} {' '.join(display2)}\n  ---\n  {' '.join(user_input)}\n")
#            print(f"\n  {' '.join(display1)}\n{op} {' '.join(display2)}\n  ---\n  {' '.join(display_result)}\n")
            digit = input("> ").strip()
            if digit.isdigit() and len(digit) == 1:
                user_input[i] = digit
                break
            print("Csak egyjegyű számokat adj meg!")
    return user_input

def main():
    while True:
        op, display1, display2, display_result, answer = generate_problem()
        user_answer = get_user_input(display1, display2, display_result, answer, op)
        
        if user_answer == answer:
            print("Helyes!")
        else:
            print(f"Helytelen! A helyes válasz: {' '.join(answer)}")
        
        if input("Új feladat? (I/N): ").strip().lower() != 'i':
            print("Kilépés...")
            sys.exit()

if __name__ == "__main__":
    main()
