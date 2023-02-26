from grid import Grid
from enemy import Enemy
from tower import Tower
from time import sleep

sample_path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7), (8, 7), (8, 8), (9, 8), (9, 9), (10, 9), (10, 10), (11, 10), (11, 11), (12, 11), (12, 12), (13, 12), (13, 13), (14, 13), (14, 14)]
GRID = Grid(sample_path)
e = Enemy(GRID, GRID.path, 100, 10)
t = Tower(GRID, 1, 2, 3)
counter = 0

while True:

    print("------------------------------------------------------------------")
    GRID.draw()
    x, y = GRID.path[counter]    
    e.move(x, y)
    counter += 1
    sleep(1)

