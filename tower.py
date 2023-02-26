from enemy import Enemy



class Tower:
    def __init__(self, grid, x, y, towerRange, img = " ۩") -> None:
        self.x = x
        self.y = y
        self.img = img
        self.grid = grid
        self.rangeSet = self.rangeDefiner(towerRange)
        if not self.grid.grid[x][y].path:
            self.grid.grid[x][y].placeTower(self)


    def draw(self):
        return self.img
    
    def rangeDefiner(self, trange):
        rangeSet = set()
        rangeSet.add((self.x, self.y))

        for i in range(self.x - trange, self.y + 1 + trange):
            for j in range(self.x - trange, self.y + 1 + trange):
                if self.grid.grid[i][j].path:
                    rangeSet.add((i, j))

        return rangeSet
    
    def enemyChecker(self, tile):

        return isinstance(tile.onTop, Enemy)