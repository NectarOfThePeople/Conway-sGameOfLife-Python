import os
import time


def singlegridpass():
    print(i)
    os.system("cls" if os.name == "nt" else "clear")

#input to start the sim by entering it's seed.

f=input("Seed = ")

os.system("cls" if os.name == "nt" else "clear")

interval=0.5



for i in grid:
    current = time.monotonic
    singlegridpass()
    exectime=time.monotonic-current
    diffednewinterval=interval-exectime
    time.sleep(diffednewinterval)



#defines the grid
row=[0]*10
grid=[row]*10





print(row)