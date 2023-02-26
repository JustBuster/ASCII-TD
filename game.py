from grid import Grid
from enemy import *
from tower import *
from time import sleep
from os import startfile

sample_path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7), (8, 7), (8, 8), (9, 8), (9, 9), (10, 9), (10, 10), (11, 10), (11, 11), (12, 11), (12, 12), (13, 12), (13, 13), (14, 13), (14, 14)]
GRID = Grid(sample_path)
BASE_HP = 100
CURRENCY = 600
e = Enemy(GRID, sample_path, 100, 10)
waves = [
    [NPCAmogus(GRID, sample_path), NPCAmogus(GRID, sample_path), NPCAmogus(GRID, sample_path), NPCAmogus(GRID, sample_path), ChonkAmogus(GRID, sample_path)] * 3,
    [NPCAmogus(GRID, sample_path), NPCAmogus(GRID, sample_path), ChonkAmogus(GRID, sample_path)] * 4,
    [NPCAmogus(GRID, sample_path),  ChonkAmogus(GRID, sample_path)] * 9,
    [MegaAmogus(GRID, sample_path)] * 5
]
enemies = []
enemies_onscreen = []
towers = []
counter = 0
wave_count = 0
play = True
pause = 'continue'
print('''
          ____   ____ ___ ___           _____ ____  
    / \  / ___| / ___|_ _|_ _|         |_   _|  _ \ 
   / _ \ \___ \| |    | | | |   _____    | | | | | |
  / ___ \ ___) | |___ | | | |  |_____|   | | | |_| |
 /_/   \_\____/ \____|___|___|           |_| |____/ 
                                                    
''')
print("The game's goal is to strategically place the towers to stop the enemies from walking across your Royal Path and attacking your kingdom.")
user_input = input("Type help for 'help' menu or 'play' to jump into the game. : ")
while user_input.lower() != "play":
    if user_input.lower() == 'help':
        GRID.help()
        user_input = input("Type help for 'help' menu or 'play' to jump into the game. : ")

    else:
        print("Enter a valid option")

        user_input = input("Type help for 'help' menu or 'play' to jump into the game. : ")

print()


while play == True:
    print("------------------------------------------------------------------")
    GRID.draw()
    while pause == 'continue':
        print('Money: ', CURRENCY)
        coords = eval(input("Select a tile to place a tower(row, col) : "))
        towerType = input("Enter the type of tower you want to select (Archer or Mortar): ")
        x, y = coords
            

        if not GRID.grid[x][y].path and towerType.lower() in ['archer', 'mortar']:
            tower = GRID.addTower(towerType, x, y)
            towers.append(tower)
            if CURRENCY >= tower.towerCost:
                CURRENCY -= tower.towerCost

            else:
                print('Not sufficient funds available.')
        elif GRID.grid[x][y].path:
            print('Please select a valid tile.')

        done = input('Type in done to play the game or continue to add more towers : ')
        if done.lower() == 'done':
            pause = 'done'

        elif done.lower() == 'continue':
            pause = 'continue'
    print()
    print("------------------------------------------------------------------")
    print()
    GRID.draw()
    #The enemy moving loop
    for i in waves:
        for j in i:
            print(len(i))
            enemies.append(j)

    if counter < len(enemies):
        enemies_onscreen.append(enemies[counter])
        counter += 1

    else:
        counter = 0
        wave_count += 1

    for i in enemies_onscreen:
        i.move()
        if i.state and i.current == sample_path[-1]:
            BASE_HP -= i.attack
            i.remove()


    for i in towers:
        enemies_to_attack = i.enemyChecker()
        if enemies_to_attack:
            i.attack(enemies_to_attack[0])
            if enemies_to_attack[0].hp <= 0:
                CURRENCY += enemies_to_attack[0].worth
                enemies_to_attack[0].remove()

    

    if wave_count == len(waves):
        print('You won! You have unlocked a secret message')
        ans = input('Do you wanna read the secret message? (yes or no)')
        print('Choice is an illusion')
        print('DEEEEEEEEEEEEEEEZ NUTTTTTTTTTTTTTTTSSSSSSSSSSSSSSSSSSSSS YOU GOT RICK ROLLED')
        startfile('important.mp4')
        

    if BASE_HP <= 0:
        print('You lowkey suck at this game, skill issue honestly!')
        print('You got rick rolled!!!!!!!!')
        startfile('important.mp4')

    print('Health: ', BASE_HP)
    print('Money: ', CURRENCY)
    sleep(1)
