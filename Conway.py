import os
import time

#logic for rendering and running the game

def singlegridpass(lenofcol):

    #rendering logic for the game,kept first in order for the render to be shown first instead of waiting for the logic to complete execution       TBD:Don't show the trailing zero in the matrices
    for i in newgrid:
        print(i)

    grid=newgrid[:]                 #copies the next frame grid from the previous frame to print

    for i in range(0, lenofcol-1):
        for j in range(0, len(row)-1):
            neighbourcount=0                #sets a count for the no. of neighbours

            #sets a list of the possible neighbour elements
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

            #logic to increase the count for the neighbours based on the list
            for neighbour in neighbours:
                if neighbour == 1:
                    ++neighbourcount
            
            #Conway game of life rules

            #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
            if grid[i][j] == 0:
                if neighbourcount==3:
                    newgrid[i][j]=1
            
            elif grid[i][j] == 1:

                #Any live cell with more than three live neighbours dies, as if by overpopulation.
                if neighbourcount>3:
                    newgrid[i][j]=0
                #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                if neighbourcount<2:
                    newgrid[i][j]=0
    
                #Any live cell with two or three live neighbours lives on to the next generation. - implicated by lack of change
                


input("- Enter to start the program")

gridlim=input("- Size = (INT)")
print("- Enter seed\n- r to start row\n- c to start column\n- f to end entry")
seed=input("Seed = ")                 #input to start the sim by entering it's seed.

os.system("cls" if os.name == "nt" else "clear")             #clears the screen

row=[0]*(gridlim+1)                  #defines one row of the grid
grid=[row]*(gridlim+1)               #defines the grid for the previous frame
newgrid=grid[:]             #defines the grid for the next frame

#setting the grid based on the seed | A starts a counter which looks for row, column in order | Note: used strings over enums for lack of percieved benefits
#incorrect seeds WILL throw errors and I DONOT give a fuck
counter="EMPTY"
for i in f:
    if  counter=="EMPTY" and i=="r":            #Sets the counter to row to accept row
        counter="ROW"

    if  counter=="ROW" and i=="c":              #Sets the counter to column to accept column
        counter="COLUMN"

    if  counter=="COLUMN" and i=="f":           #Sets the counter to ENTRY to insert the value
        counter="ENTRY"

    if  counter == "ROW":

        if row == NULL:                         #starts counting row if row is null
            row = int(i)
        elif i.isnumeric:                       #increases row if there are more digits
            row = (row*10) + int(i)              

    if  counter == "COLUMN":

        if col == NULL:                         #starts counting col if col is null
            col= int(i)

        elif i.isnumeric:
            col = (col*10) + int(i)             #increases col if there are more digits

    
    if counter == "ENTRY":

        newgrid[row][col]=1                     #sets value into grid
        
        #sets row, column to NULL and counter to empty
        row = NULL                              
        col = NULL
        counter = "EMPTY"

interval=0.5
clock = time.monotonic()                #sets the baseline clock outside the loop as to avoid being restarted, causing drift

#non drift clock to time refresh of the terminal window
for i in range(0, len(grid)):
    clock+=interval                 #sets the interval to be hit from the baseline clock instead of a moving window like originally planned to avoid drift    
    singlegridpass(i)               #runs the run and render logic
    
    sleepytime=clock-time.monotonic()               #calculates the gap between the target interval added amount set at loop start and the time taken to execute the loop so far

    #checks if the process took longer than the interval itself
    if sleepytime<0:                                
        print("Error: Execution took too long by", -sleepytime, "seconds")
        break
    time.sleep(sleepytime)                                            #pauses until the timer should reset for the next pass
    os.system("cls" if os.name == "nt" else "clear")


print ('execution complete')