#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    ops = argv[2]
    b = int(argv[3])

    if ops == "+":
        num = add(a, b)

    elif ops == "-":
        num = sub(a, b)

    elif ops == "*":
        num = mul(a, b)

    elif ops == "/":
        num = div(a, b)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, ops, b, num))
