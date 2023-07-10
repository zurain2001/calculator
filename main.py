"""
Date: 9th July 2023
Developer: Zurain Zeeshan
Program: Calculator

"""
from art import logo

print(logo)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    num1 = float(input("What is the first number? "))

    further = True
    while further:

        num2 = float(input("What is the next number? "))

        for key in operations:
            print(key)

        symbol = input("Pick an operation from above. ")

        calculation = operations[symbol]
        result = calculation(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")

        go_on = input("If you want to continue with that result then type 'y' else type 'n'. ").lower()

        if go_on == 'y':
            num1 = result
        else:
            further = False
            calculator()

calculator()

