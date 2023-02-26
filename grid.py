from tiles import Tiles
from tower import *


class Grid:
    def __init__(self, path = [], rows = 15, cols = 15) -> None:
        self.rows = rows
        self.cols = cols
        self.tileCollection = {"blank": "⬜", "path": "⬛"}
        self.grid = []

        for i in range(rows):
            row = []
            for j in range(cols):
                if (i, j) in path:
                    row.append(Tiles("path"))

                else:
                    row.append(Tiles("blank"))

            self.grid.append(row)

        self.path = self.pathFinder((0, 0), (self.rows - 1, self.cols - 1))
        

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[i][j].img, end = " ")
            print("\n")

    def addTower(self, type, x, y):
        if type.lower() == 'archer':
            return ArcherTower(self, x, y)
        
        elif type.lower() == 'mortar':
            return MortarTower(self, x, y)

    def help(self):
        print('''
        The Book of Knowledge

        Types of Towers:
        ->Archer Tower (۩): The home to two sharp shooting archers sniping the enemy away from far away distance and precision.
            Stats:
            Attack: 40
            Target Type: Single
            Range: 3
            Cost: 200

        ->Mortar Tower (Ջ): The explosive lab turned into a killing machine smashing away groups of enemies at once.
            Stats:
            Attack: 20
            Target Type: Group
            Range: 2
            Cost: 300
        ''')
        
    def pathFinder(self, start, end):
        path = []
        stack = []
        visited = set()

        stack.append(start)
        path.append(start)
        visited.add(start)

        while stack:
            x, y = stack.pop()

            if (x, y) == end:
                return path
            
            for xa, ya in self.validNeighbours(x, y):
                if (xa, ya) not in visited:
                    stack.append((xa, ya))
                    path.append((xa, ya))
                    visited.add((xa, ya))
            
    def validNeighbours(self, x, y) :
        coords = [[0,1], [0,-1], [-1,0], [1,0]]

        for dx, dy in coords:
            X, Y = x + dx, y + dy

            if not(0 <= X < self.rows and 0 <= Y < self.cols):
                continue

            if self.grid[X][Y].path:
                yield (X, Y)

        

