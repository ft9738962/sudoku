# Author: Max Qiu
# Date: 2021/05/18
import sys, time

class node:
    def __init__(self, x, y):
        self.h = x
        self.v = y
        self.candidates = list(x for x in range(1, 10))
        self.value = 0
        self.candLen = len(self.candidates)

    def candUpdate(num=0, removeNum):
        if not num:
            try:
                self.candidates.remove(removeNum)
                self.canLen -= 1
            except:
                print(f"The candidates list {self.candidates} has no value {removeNum}")
        else:
            self.value = num
            self.candidates = []
            self.candLen = 0

class sodukuSolver:
    def __init__(self) -> None:
        self.body = dict()
        self.hlines = dict()
        self.vlines = dict()
        self.blocks = dict()
        self.solveProgress = 0
        self.finish = False
        self.tbl = {
            "h": self.hlines,
            "v": self.vlines,
            "b": self.blocks
        }
        for x in range(1, 10):
            self.hlines[x] = list(x for x in range(1,10))
            self.vlines[x] = list(x for x in range(1,10))
            for y in range(1, 10):
                self.body[10*x + y] = list(x for x in range(1,10))
            if x < 4:
                for y in range(1,4):
                    self.blocks[10*x+y] = list(x for x in range(1,10))

    
    def update(self, k, v):
        """
        Update sudoku with certain value
        k : position
        v : value
        """
        self.body[k] = v
        hline_num = int(k / 10)
        vline_num = k % 10
        self.hlines[hline_num].remove(v)
        self.vlines[vline_num].remove(v)
        self.blocks[10 * hline_num + vline_num].remove(v)

    def lineCheck(self, type):
        for k, v in self.tbl[type].items():
            if type(v) == list:
                if len(v) == 1:
                    self.update(k,v)
                    self.solveProgress += 1

    def blockCheck(self):
        for k, v in self.tbl[type].items():
            if type(v) == list:
                if len(v) == 1:
                    self.update(k,v)
                    self.solveProgress += 1

    # def blockCheck(self):
    
    def loop(self):

    def initialize(self, data):
        for k, v in data.items():
            if k > 10 and k<100 and k%10 != 0 and v > 0 and v < 10:
                self.update(k, v)
                self.solveProgress += 1 
            else:
                print(f"{k}:{v}, Input data wrong")
                sys.exit(1)            
    
    def show(self):
        for x in range(1, 10):
            line = ""
            for y in range(1, 10):
                if type(self.body[10*x + y]) == int:
                    num = self.body.get(10 * x + y)
                    line += f"[{num}]"
                else:
                    line += "[ ]"
            print(line)

    def solve(self):
        begin = time.time()
        while not self.finish:

            if self.solveProgress == 81:
                self.finish = True
        self.show()
        print(f"Spent {(time.time() - begin):.2f} seconds")


def main():
    sudoku = sodukuSolver()
    d = {
        11:3,
        22:4,
        23:5,
        78:9
    }
    sudoku.initialize(d)
    sudoku.show()
    # print(sudoku.body)

if __name__ == "__main__":
    main()
