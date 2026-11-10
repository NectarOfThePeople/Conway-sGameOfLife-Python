import os
import time


def singlegridpass():
    print(i)


#input to start the sim by entering it's seed.

f=input("Seed = ")

os.system("cls" if os.name == "nt" else "clear")

#defines the grid
row=[0]*10
grid=[row]*10

interval=0.5
clock = time.monotonic()


for i in grid:
    clock+=interval
    singlegridpass()
    sleepytime=clock-time.monotonic()
    if sleepytime<0:
        print("Error: Execution took too long by", -sleepytime, "seconds")
        break
    time.sleep(sleepytime)
    os.system("cls" if os.name == "nt" else "clear")









print(row)