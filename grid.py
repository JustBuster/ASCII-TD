from tiles import Tiles


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

        self.path = self.pathFinder((0, 0), (self.row - 1, self.cols - 1))
        

    def draw(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[i][j].img, end = " ")
            print("\n")

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
            
            for coords in self.validNeighbours(x, y):
                if coords not in visited:
                    stack.append(coords)
                    path.append(coords)
            


    def validNeighbours(self, x, y) -> list[Tiles]:
        coords = [[0,1], [0,-1], [-1,0], [1,0]]

        for dx, dy in coords:
            X, Y = x + dx, y + dy

        if self.grid[X][Y].path:
            yield (X, Y)

        


sample_path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7), (8, 7), (8, 8), (9, 8), (9, 9), (10, 9), (10, 10), (11, 10), (11, 11), (12, 11), (12, 12), (13, 12), (13, 13), (14, 13), (14, 14)]
Grid(sample_path).draw()
