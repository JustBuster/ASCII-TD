class Enemy:
    def __init__(self, hp, attack, img = "0") -> None:
        self.hp = hp
        self.attack = attack
        self.img = img

    def draw(self):
        return self.img

    def move(self):
        pass

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True