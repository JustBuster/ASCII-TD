class Enemy:
    def __init__(self, grid, path, hp, attack, img = " ඞ") -> None:
        self.hp = hp
        self.attack = attack
        self.img = img
        self.path = path
        self.grid = grid
        self.current = None


    def draw(self):
        return self.img

    def move(self,x ,y):
        self.grid.grid[x][y].placeEnemy(self)
        if self.current:
            xx, yy = self.current
            self.grid.grid[xx][yy].remove()
        self.current = (x, y)       
        
    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True
        