from copy import copy

class recurSudoku:
    def __init__(self):
        self.body = [[0 for _ in range(9)] for _ in range(9)]
        self.answers = []

    def show(body):
        for line in body:
            print(line)

    def initialize(self, d):
        for k, v in d.items():
            self.body[k[0]][k[1]] = v
        self.show()

    def analyseCandidates(self, x, y):
        candidates = set(x for x in range(1,10))
        for i in range(9):
            candidates.discard(self.body[x][i])
            candidates.discard(self.body[i][y])
        for j in range(int(x/3) * 3, int(x/3)*3+3):
            for k in range(int(y/3)*3, int(y/3)*3+3):
                candidates.discard(self.body[j][k])
        print(candidates)
        if len(candidates):
            return list(candidates)
        else:
            return 0 

    def nextStep(self, x,  y):
        if y < 8:
            return x, y+1
        elif y == 8 and x < 8:
            return x+1, 0
        else:
            return -1, 0

    def recurGuess(self, x, y): 
        body = copy(self.body)
        x, y = copy(x), copy(y)
        if body[x][y]:
            x, y = self.nextStep(x, y)
            if x < 0:
                self.answers.append(body)
                return
            else:
                self.recurGuess(x, y)
        else:
            candidates = self.analyseCandidates(x, y)
            
            if candidates:
                if len(candidates) == 1:
                    print("input: ",x," ", y, " ",candidates[0])
                    body[x][y] = candidates[0]
                    x, y = self.nextStep(x, y)
                    if x < 0:
                        print("finish")
                        self.answers.append(body)
                        return
                    self.body = body
                    self.recurGuess(x, y)
                for c in candidates:
                    print("input: ", x," ", y, " ",candidates[0])
                    body[x][y] = c
                    x, y = self.nextStep(x, y)
                    if x < 0:
                        print("finish")
                        self.answers.append(body)
                        return
                    self.body = body
                    self.recurGuess(x, y)
            else:
                print("No Answer")
                return



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

    sudoku = recurSudoku()
    sudoku.initialize(d)
    sudoku.recurGuess(0, 0)
    #for i in sudoku.answers:
    #   show(i)

if __name__ == "__main__":
    main()
