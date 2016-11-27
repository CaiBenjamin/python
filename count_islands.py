w, h = 3,4
myArray = [[0 for x in range(w)] for y in range(h)]

myArray[0][0] = 0
myArray[0][1] = 0
myArray[0][2] = 1
myArray[1][0] = 1
myArray[1][1] = 1
myArray[1][2] = 1
myArray[2][0] = 0
myArray[2][1] = 0
myArray[2][2] = 0
myArray[3][0] = 1
myArray[3][1] = 1
myArray[3][2] = 1

def count_islands(myArray):
    num_islands = 0
    island_found = False
    for i in range(len(myArray)):
        for j in range(len(myArray[i])):
            island_found = False
            if myArray[i][j] == 1:
                myArray[i][j] = 2
                if j-1 >= 0:
                    if myArray[i][j-1] == 1:
                        island_found = True
                if j+1 < len(myArray[i]):
                    if myArray[i][j+1] == 1:
                        island_found = True
                if i-1 >= 0:
                    if myArray[i-1][j] == 1:
                        island_found = True
                if i+1 < len(myArray):
                    if myArray[i+1][j] == 1:
                        island_found = True
                while(j > 0 or i > 0):
                    if j-1 >= 0:
                        if myArray[i][j-1] == 2:
                            island_found = False
                    if j+1 < len(myArray[i]):
                        if  myArray[i][j+1] == 2:
                            island_found = False
                    if i-1 >= 0:
                        if myArray[i-1][j] == 2:
                            island_found = False
                    if i+1 < len(myArray):
                        if myArray[i+1][j] == 2:
                            island_found = False
                    i-=1
                    j-=1
                 
                if myArray[i][j-1] == 1:
                        myArray[i][j-1] = 2
                if j+1 < len(myArray[i]):
                    if myArray[i][j+1] == 1:
                        myArray[i][j+1] = 2
                if i-1 >= 0:
                    if myArray[i-1][j] == 1:
                        myArray[i-1][j] = 2
                if i+1 < len(myArray):
                    if myArray[i+1][j] == 1:
                        myArray[i+1][j] = 2
                        
                if island_found == True:       
                    num_islands+=1

           
    return num_islands



print count_islands(myArray)