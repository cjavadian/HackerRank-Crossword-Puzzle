# Catherine Javadian, Jennifer Cafiero, and Jordana Approvato
# We pledge our honor that we have abided by the Stevens Honor System

grid = []

def countB(row):
    blanks = []
    first = False
    count = 0
    for y in range(10):
        if grid[row][y] == '-':
            if first == False:
                blanks.append(y)
                first = True
            count = count + 1
    blanks.append(count)
    return blanks
    #NAH
    

def findSol():
    row = 0
    blanks = countB(row)
    if blanks[1] > 1:
        
    return

def main():
    lines = 10
    while (lines):
        grid_l = input().strip()
        grid.append(list(grid_l))
        lines = lines - 1
    words = input().split(';')
    findSol()
    return

main()
