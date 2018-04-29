from sys import exit
import pG_storingData as pgSd
from pG_description import *
from pG_engine import *

def start():
    description()
    counter = 0
    scored = 0
    while True:

        print("We are ready to go - where do you want to shoot: right (R), left(L) or in the center(C)")
        inp1 = str(input("> ")).upper()
        print("How do you want to shoot: in 9, 6 or 3")
        inp2 = input("> ")
        X1, X2 = where_shot(inp1, inp2)
        X11, X21 = random_gen()
        res = outcome(X1, X2, X11, X21)
        scored = scored + res
        counter = counter + 1
        print(f"As of now you scored {scored} out of {counter}")
        pgSd.save_result(X11, X21, X1, X2, res)
        print("Do you want to continue? Y or N")
        answer = str(input(">")).upper()
        if answer == "N":
            exit(0)
        elif answer == "Y":
            print("Cool, we continue")
        else:
            print("Didn't get that we continue Y or N?")
start()
