import os
import time


def singlegridpass():
    print(i)
    os.system("cls" if os.name == "nt" else "clear")

#input to start the sim by entering it's seed.

f=input("Seed = ")

os.system("cls" if os.name == "nt" else "clear")

interval=0.5
clock = time.monotonic()


for i in grid:
    clock+=interval
    gridpass()
    sleepytime=clock-time.monotonic()
    if sleepytime>0:
        time.sleep(sleepytime)
    else:
        print("Error: Execution took too long by "+ -sleepytime + " seconds")
        break



#defines the grid
row=[0]*10
grid=[row]*10





print(row)