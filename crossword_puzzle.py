# Catherine Javadian, Jennifer Cafiero, and Jordana Approvato
# We pledge our honor that we have abided by the Stevens Honor System

grid = []
spaces = []
blanks = []

class space:
    def __init__(self, start, end, length, taken):
        self.start = start
        self.end = end
        self.length = length
        self.taken = False

#def _can_add(word):
    

def findSol(words):
    if len(words) == 0:
        return True
    for word in words:
        for space in spaces:
            if _can_add(word):
                before = _add(word)
                slot.taken = True
                new_words = set(words)
                new_words.remove(word)
                if solve_puzzle(new_words):
                    return True
                _add(before)
                slot.taken = False
    
    return

def foundSpace(row, col):
    return


def findSpace():
    for row in range(10):
        for col in range(10):
            if grid[row][col] == '-':
                foundSpace(row, col)
    return
    
def main():
    lines = 10
    while (lines):
        grid_l = input()
        grid.append(list(grid_l))
        lines = lines - 1
    words = input().split(';')
    findSpace()
    #findSol(words)
    return

main()
