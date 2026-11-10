import os
import time


def singlegridpass(lenofcol):

    for i in newgrid:
        print(i)

    grid=newgrid[:]
    for i in range(0, lenofcol-1):
        for j in range(0, len(row)-1):
            neighbourcount=0
            neighbours=[
                grid[i+1][j],
                grid[i-1][j],
                grid[i+1][j+1],
                grid[i][j+1],
                grid[i][j-1],
                grid[i-1][j-1],
                grid[i+1][j-1],
                grid[i-1][j+1]
                ]

            for neighbour in neighbours:
                if neighbour == 1:
                    ++neighbourcount
            

            if grid[i][j] == 0:
                if neighbourcount==3:
                    newgrid[i][j]=1
                        
            elif grid[i][j] == 1:
                if neighbourcount>3:
                    newgrid[i][j]=0
                if neighbourcount<2:
                    newgrid[i][j]=0
    
                

#input to start the sim by entering it's seed.

f=input("Seed = ")

os.system("cls" if os.name == "nt" else "clear")

#defines the grid
row=[0]*10
grid=[row]*10
newgrid=grid[:]


interval=0.5
clock = time.monotonic()


for i in range(0, len(grid)):
    clock+=interval
    singlegridpass(i)
    sleepytime=clock-time.monotonic()
    if sleepytime<0:
        print("Error: Execution took too long by", -sleepytime, "seconds")
        break
    time.sleep(sleepytime)
    os.system("cls" if os.name == "nt" else "clear")


print(row)