class Enemy:
    def __init__(self, grid, path, hp, attack, img = " ඞ") -> None:
        self.hp = hp
        self.attack = attack
        self.img = img
        self.path = path
        self.grid = grid
        self.current = None
        self.step = 0
        self.state = True #True if alive
        self.worth = hp//2


    def draw(self):
        return self.img

    def move(self):
        if self.state:
            x, y = self.path[self.step]
            self.grid.grid[x][y].placeEnemy(self)
            if self.current:
                xx, yy = self.current
                self.grid.grid[xx][yy].remove()
            self.current = (x, y)     
            self.step += 1  

        else:
            pass
        
    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True
        
    def remove(self):
        x, y = self.current
        self.grid.grid[x][y].remove()
        self.state = False
        print("Bro Died!")
        

class NPCAmogus(Enemy):
    def __init__(self, grid, path, hp = 100, attack = 5, img=" ඞ") -> None:
        super().__init__(grid, path, hp, attack, img)

class ChonkAmogus(Enemy):
    def __init__(self, grid, path, hp = 150, attack = 10, img="ѾѾ") -> None:
        super().__init__(grid, path, hp, attack, img)

class MegaAmogus(Enemy):
    def __init__(self, grid, path, hp = 250, attack = 20, img="ҦҦ") -> None:
        super().__init__(grid, path, hp, attack, img)

class Imposter(Enemy):
    def __init__(self, grid, path, hp = 500, attack = 50, img="Ӝ ") -> None:
        super().__init__(grid, path, hp, attack, img)