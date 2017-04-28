# Catherine Javadian, Jennifer Cafiero, and Jordana Approvato
# We pledge our honor that we have abided by the Stevens Honor System

grid = []
spaces = []
blanks = []

class Space:
    def __init__(self, start, length, vertical, taken):
        self.start = start
        self.length = length
        self.vertical = vertical
        self.taken = taken


def foundSpace(row, col):
    return 23


def findSpace():
    for row in range(10):
        for col in range(10):
            if grid[row][col] == '-':
                foundSpace(row, col)
    return 23


def readSpaces():
    rows = []
    for i in range(10):
        row = input()
        rows.append(row)
    row_spaces = _get_spaces(rows, False)
    cols = []
    for i in range(10):
        col = ""
        for j in range(10):
            col += rows[j][i]
        cols.append(col)
    col_spaces = _get_spaces(cols, True)
    return [list(row) for row in rows], row_spaces + col_spaces

def _get_spaces(lines, vertical):
    '''Takes in a line of the grid and counts the spaces, and stores them in an array.
       The input vertical has the value True if the line is a column.'''
    spaces = []
    n = 0
    for i in lines:
        for j in whereAreSpaces(i):
            index, length = j
            if (vertical == True):
                start = (index, n)
            else:
                start = (n, index)
            spaces.append(Space(start, length, vertical, False))
        n += 1
    return spaces

def whereAreSpaces(line):
    spaces = []
    for blank in line.split("+"):
        length = len(blank)
        if length > 1:
            n = 0
            while n < length:
                n = line.find(blank, n)
                if line == -1:
                    break
                spaces.append((n, length))
                n += length
    return spaces

def findSol(grid, spaces, words):
    '''Finds the solution of the puzzle. If words is empty (len 0), returns
       True to indicate that the puzzle is solved.'''
    if len(words) == 0:
        return True
    for word in words:
        for space in spaces:
            if canAddWord(grid, space, word):
                before = addWord(grid, space, word)
                space.taken = True
                new_words = set(words)
                new_words.remove(word)
                if findSol(grid, space, new_words):
                    return True
                addWord(grid, space, before) #will revert the grid if the solution is incorrect
                space.taken = False
                
    #if it reaches this far, breaks out of the for loop, and does not yet have a solution, it is unsolvable
    return False

def canAddWord(grid, space, word):
    if space.taken or len(word) != space.length:
        return False
    row, col = space.start
    for i in word:
        if (grid[row][col] != "-" or grid[row][col] != i):
            return False
        row, col = nextSpace(row, col, space.vertical)
    return True

def addWord(grid, space, word):
    new_grid = []
    row, col = space.start
    for char in word:
        new_grid.append(grid[row][col])
        grid[row][col] = char
        row, col = nextSpace(row, col, space.vertical)
    return new_grid

def nextSpace(row, col, vertical):
    if vertical:
        return row + 1, col
    else:
        return row, col + 1
    

def main():
    grid, spaces = readSpaces()
    words = input().split(';')
    findSol(grid, spaces, words)
    for i in grid:
        print("".join(i))

    return

    '''      
    lines = 10
    while (lines):
        grid_l = input()
        grid.append(list(grid_l))
        lines = lines - 1
    words = input().split(';')
    findSpace()
    #findSol(words)
    return'''

main()
