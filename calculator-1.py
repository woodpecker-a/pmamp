#! /usr/bin/python3


def addition(x,y):
    return x+y

def subtruction(x,y):
    return x-y

def multliplication(x,y):
    return x*y

def division(x,y):
    return x/y

def primenumber(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if (x % i) == 0:
                print(x, "is not a prime number")
        else:
            print(x, "is a prime number")

    else:
        print(x, "is not a prime number")

def evenodd(x):
    if x > 1:
        if (x % 2) == 0:
            print(x," is an Even Number")
        else:
            print(x," is an Odd Number")


name = input("Hey! Your name:\t")
print("\n\nHola!", name, "! Welcome to calculator! here you go!!\n\n")

choice = "y"

while choice!= "n": 

        n = input("\n=====Selection====\n\n## Type 1 for ADDITION\n## Type 2 for SUBTRUCTION\n## Type 3 for MULTIPLICATION\n## Type 4 for DIVISION\n## Type 5 for PRIME NUMBER CHECKING\n## Type 6 for EVEN/ODD NUMBER CHECKING\n\n--------type n for exit!\n\n")
        if n in ('1','2','3','4'):
            a = float(input("Enter First Number: "))
            b = float(input("Enter Secound Number: "))

            if n == '1':
                print("\n\n======================")
                print(a, "+", b, "=" , addition(a,b))
                print("======================\n\n")
            if n == '2':
                print("\n\n======================")
                print(a, "-", b, "=" , subtruction(a,b))
                print("======================\n\n")
            if n == '3':
                print("\n\n======================")
                print(a, "*", b, "=" , multliplication(a,b))
                print("======================\n\n")
            if n == '4':
                if b != 0:
                    print("\n\n======================")
                    print(a, "/", b, "=" , division(a,b))
                    print("======================\n\n")
                else:
                    print("\n\n=============================")
                    print("Number can not divided by '0'")
                    print("=============================\n\n")

        elif n == "5":
            p = int(input("Enter a real number: "))
            print("\n\n======================")
            primenumber(p)
            print("======================\n\n")

        elif n == '6':
            c = int(input("Enter a real number: "))
            print("\n\n======================")
            evenodd(c)
            print("======================\n\n")

        elif n == "n":
            break

        else:
            print("\n\n======================")
            print("\n\nWrong Input")
            print("======================\n\n")
            continue
print("Good Bye Mr.", name)