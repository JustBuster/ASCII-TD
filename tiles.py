class Tiles:
    tileCollection = {"blank": "⬜", "path": "⬛"}

    def __init__(self, state) -> None:

        self.path = True if state == "path" else False

        self.img = Tiles.tileCollection[state]
        
        self.onTop = None

    def placeBuilding(self):
        pass

    def placeEnemy(self):
        pass

    def removeEnemy(self):
        pass