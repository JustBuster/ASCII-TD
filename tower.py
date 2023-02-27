from enemy import Enemy
from collections import deque
import math



class Tower:
    def __init__(self, grid, x, y, towerRange, towerDamage, img = " ۩") -> None:
        self.x = x
        self.y = y
        self.img = img
        self.grid = grid
        self.towerRange = towerRange
        self.towerDamage = towerDamage
        self.rangeSet = self.rangeDefiner(self.towerRange)
        if not self.grid.grid[x][y].path:
            self.grid.grid[x][y].placeTower(self)

        self.life = 1

    def draw(self):
        return self.img
    
    def rangeDefiner(self, trange):
        rangeSet = set()
        rangeSet.add((self.x, self.y))

        for i in range(self.x - trange, self.x + 1 + trange):
            for j in range(self.y - trange, self.y + 1 + trange):
                if self.grid.grid[i][j].path:
                    rangeSet.add((i, j))

        return rangeSet
    
    def attack(self, enemy):
        enemy.hit(self.towerDamage)

    def enemyChecker(self):
        enemies = deque()
        for i in self.rangeSet:
            x, y = i
            tile = self.grid.grid[x][y]
            if isinstance(tile.onTop, Enemy):
                enemies.append(tile.onTop)

        if enemies and enemies[0].current not in self.rangeSet:
            enemies.popleft()

        return enemies
    
    def upgrade(self):
        self.towerRange += 1
        self.rangeSet = self.rangeDefiner(self.towerRange)
        self.towerDamage += math.floor(self.towerDamage * 0.4)

        

class ArcherTower(Tower):
    def __init__(self, grid, x, y, towerRange = 3, towerDamage = 40, img=" ۩") -> None:
        super().__init__(grid, x, y, towerRange , towerDamage, img)
        self.towerCost = 200

    def upgrade(self):
        super().upgrade()
        if self.life == 6:
            self.img = "Ұ "
            print("۩ --> Ұ")
            print("Your archer tower on %d, %d upgraded to level 2." % (self.x, self.y))

        elif self.life == 9:
            self.img = "Ѩ "
            print("Ұ --> Ѩ")
            print("Your archer tower on %d, %d upgraded to level 3." % (self.x, self.y))

class MortarTower(Tower):
    def __init__(self, grid, x, y, towerRange = 2, towerDamage = 20, img=" Ջ") -> None:
        super().__init__(grid, x, y, towerRange, towerDamage, img)
        self.towerCost = 300

    def attack(self, enemy):
        enemies_to_attack = []
        for i in range(enemy.step, enemy.step-3, -1):
            x, y = enemy.path[i]
            if isinstance(enemy.grid.grid[x][y].onTop, Enemy):
                enemies_to_attack.append(enemy.grid.grid[x][y].onTop)
        
        for i in enemies_to_attack:        
            super().attack(i)

    def upgrade(self):
        super().upgrade()
        if self.life == 6:
            self.img = "Ө "
            print("Ջ --> Ө")
            print("Your archer tower on %d, %d upgraded to level 2." % (self.x, self.y))

        elif self.life == 9:
            self.img = "Ѻ "
            print("Ө --> Ѻ")
            print("Your archer tower on %d, %d upgraded to level 3." % (self.x, self.y))