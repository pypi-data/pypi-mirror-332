#!/usr/bin/python3

import copy
import os
import random

from colorama import Fore, Back, Style, init

init(autoreset=True)

datas = {'lines': [], 'sum': []}

global num1, num2, num1_str, num2_str
num1 = -1
num2 = -1
num1_str = ''
num2_str = ''


def generate_number(digits):
    """Generates number with the given length of digits"""
    lower_bound = 10 ** (digits - 1)
    upper_bound = 10 ** digits - 1
    return random.randint(lower_bound, upper_bound)

def generate_problem():
    num1 = generate_number(3)
    num2 = generate_number(3)
#    print(f'{num1} * {num2}', datas)
    num1_str = str(num1)
    num2_str = str(num2)
    result = solve_problem(num1, num2, num1_str, num2_str)
    for line in result['lines']:
        datas['lines'].append([])
        for item in line:
            datas['lines'][-1].append('_')
    for item in result['sum']:
        datas['sum'].append('_')
        
#    print(datas)
    return num1, num2, num1_str, num2_str, result

def nth_line_is_in_progress():
    ln = 0
    for line in datas['lines']:
        if '_' in line:
            return ln
        ln = ln + 1
    return 'result'

def nth_character_is_in_progress(line):
    return len(line) - next(i for i, x in enumerate(reversed(line)) if "_" in x) - 1

def is_finished():
    return not any("_" in elem for lista in datas.values() for sor in (lista if isinstance(lista, list) else [lista]) for elem in sor)

def print_multiplication(num1, num2):
    print(f'  {num1} * {num2}')
    print(Fore.LIGHTBLACK_EX + f'  {"-" * len(num1_str)}')
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_screen(num1, num2, num1_str, num2_str):
    print_multiplication(num1, num2)

    cursor_found = False
    nth_progress = nth_line_is_in_progress()
    for count, line in enumerate(datas['lines']):
        color = ''
        # Megnezzuk, hogy az eppen aktualis sorrol van-e szo
        if count == nth_progress:
            color = Fore.YELLOW
        print(' ', end='')
        if not len(line) > len(num2_str):
            print(' ', end='')
        print(' ' * count, end='')
        # Ha az eppen aktualis sor, az eppen aktualis karaktert megjeloljuk.
        if count == nth_progress:
            nth_item_progress = nth_character_is_in_progress(line)
            for count2, item in enumerate(line):
                color2 = ''
                if count2 == nth_item_progress:
                    color2 = Back.GREEN
                print(color + color2 + item, end='')
        else:
            print(''.join(line), end='')
        print()
    print(Fore.LIGHTBLACK_EX + '+------------------------')

    # Result line
    print(' ', end='')
    if (num1 * num2) < 10 ** (len(num1_str) + len(num2_str) - 1):
        print(' ', end='')
    sum = datas['sum']
    if nth_progress == 'result':
        nth_result_progress = nth_character_is_in_progress(sum)
        for countr, item in enumerate(sum):
            colorr = ''
            if countr == nth_result_progress:
                colorr = Back.BLUE
            print(colorr + item, end='')
    else:
        print(''.join(sum), end='')
    print()

    digit = input("> ").strip()
    if digit.isdigit() and len(digit) == 1:
        if isinstance(nth_progress, int):
            datas['lines'][nth_progress][nth_item_progress] = digit
        else:
            datas['sum'][nth_result_progress] = digit
    
    
def print_screen_result(num1, num2, num1_str, num2_str, result):
    print_multiplication(num1, num2)
    for count, line in enumerate(datas['lines']):
        print(' ', end='')
        if not len(line) > len(num2_str):
            print(' ', end='')
        print(' ' * count, end='')
        for count2, item in enumerate(line):
            if result['lines'][count][count2] == item:
                color = Fore.GREEN
            else:
                color = Fore.RED
            print(color + result['lines'][count][count2], end='')
        print()
    print('--------------------------------')
    print(' ', end='')
    if (num1 * num2) < 10 ** (len(num1_str) + len(num2_str) - 1):
        print(' ', end='')
    for countr, item in enumerate(datas['sum']):
        if result['sum'][countr] == item:
            color = Fore.GREEN
        else:
            color = Fore.RED
        print(color + result['sum'][countr], end='')
    print()
        

def solve_problem(num1, num2, num1_str, num2_str):
    result = {'lines': [], 'sum': []}
    for num2_ch in num2_str:
        num2_ch = int(num2_ch)
        result['lines'].append([digit for digit in str(num1 * num2_ch)])
    result['sum'] = [digit for digit in str(num1 * num2)]
    return result
    
    

if __name__ == '__main__':
    num1, num2, num1_str, num2_str, result = generate_problem()


    while True:
        clear_screen()
    #    print(datas)
    #    print(result)
        print_screen(num1, num2, num1_str, num2_str)
        if is_finished():
            print()
            print()
            print()
            print_screen_result(num1, num2, num1_str, num2_str, result)
            break


