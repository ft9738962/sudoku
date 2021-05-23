from copy import copy, deepcopy
import time

class Sudoku:
    def __init__(self):
        self.body = [[0 for _ in range(9)] for _ in range(9)]

    def initialize(self, d):
        for k, v in d.items():
            self.body[k[0]][k[1]] = v

def show(body):
    for line in body:
        print(line)

def analyseCandidates(body, x, y):
    candidates = set(x for x in range(1,10))
    for i in range(9):
        candidates.discard(body[x][i])
        candidates.discard(body[i][y])
    for j in range(int(x/3) * 3, int(x/3)*3+3):
        for k in range(int(y/3)*3, int(y/3)*3+3):
            candidates.discard(body[j][k])
    if len(candidates):
        return list(candidates)
    else:
        return 0 

def nextStep(x,  y):
    if y < 8:
        return [x, y+1]
    elif y == 8 and x < 8:
        return [x+1, 0]
    else:
        return [-1, 0]

def recurGuess(answers, body, pos): 
    x, y = pos[0], pos[1]
    b = deepcopy(body)
    if x < 0:
        answers.append(b)
        return
    elif b[x][y]:
        recurGuess(answers, b, nextStep(x, y))
    else:
        candidates = analyseCandidates(body, x, y)
        if candidates:
            for c in candidates:
                b[x][y] = c
                recurGuess(answers, b, nextStep(x,y)) 

def main():
    d = {
        (0, 0): 1,
        (0, 2): 8,
        (2, 0): 4,
        (0, 5): 4,
        (0, 6): 3,
        (1, 5): 3,
        (1, 8): 7,
        (2, 5): 6,
        (3, 1): 5,
        (3, 6): 7,
        (4, 4): 3,
        (4, 5): 2,
        (5, 1): 4,
        (5, 3): 8,
        (5, 7): 9,
        (6, 4): 9,
        (6, 5): 1,
        (6, 7): 2,
        (6, 8): 5,
        (7, 1): 2,
        (7, 8): 6,
        (8, 2): 6,
        (8, 3): 5,
        (8, 7): 1
    }
    
    answers = []
    sudoku = Sudoku()
    sudoku.initialize(d)
    print("Origin")
    show(sudoku.body)
    bg = time.time()
    recurGuess(answers, sudoku.body, [0, 0])
    print(time.time()-bg)
    ct = 1 
    for i in answers:
        print("answer: ", ct)
        show(i)
        ct += 1

if __name__ == "__main__":
    main()
