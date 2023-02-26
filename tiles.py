class Tiles:
    tileCollection = {"blank": "⬜", "path": "⬛"}

    def __init__(self, state) -> None:

        self.path = True if state == "path" else False

        self.img = Tiles.tileCollection[state]
        
        self.onTop = None

    def placeTower(self, tower):
        self.onTop = tower
        self.img = tower.img

    def placeEnemy(self, enemy):
        self.onTop = enemy
        self.img = enemy.img

    def remove(self):
        self.onTop = None
        self.img = Tiles.tileCollection['path']