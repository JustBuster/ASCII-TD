from grid import Grid
from enemy import *
from tower import *
from time import sleep
from os import startfile

sample_path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 7), (8, 7), (8, 8), (9, 8), (9, 9), (10, 9), (10, 10), (11, 10), (11, 11), (12, 11), (12, 12), (13, 12), (13, 13), (14, 13), (14, 14)]
GRID = Grid(sample_path)
BASE_HP = 100
CURRENCY = 600

waves = [[5, 90, 10, 0, 0], [5, 60, 30, 10, 0], [20, 60, 0, 30, 0], [10, 0, 0, 80, 20]]
enemies_onscreen = []
towers = []
counter = 0
wave_count = 0
play = True
pause = True

print('''
     _    ____   ____ ___ ___           _____ ____  
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
    while pause:
        print('Wave: ', wave_count + 1)
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
        print('Money: ', CURRENCY)
        done = input('Type in done to play the game or continue to add more towers : ')
        if done.lower() == 'done':
            pause = False

        elif done.lower() == 'continue':
            pause = True
    print()
    print("------------------------------------------------------------------")
    print()
    GRID.draw()
    #Enemies

    if counter < waves[wave_count][0]:
        enemies_onscreen.append(GRID.enemyGenerator(waves[wave_count]))
        counter += 1

    for i in enemies_onscreen:
        i.move()
        ind = enemies_onscreen.index(i)
        if i.state and i.current == sample_path[-1]:
            BASE_HP -= i.attack
            i.remove()
            enemies_onscreen.pop(ind)


    for i in towers:
        enemies_to_attack = i.enemyChecker()
        if enemies_to_attack:
            i.attack(enemies_to_attack[0])
            if enemies_to_attack[0].hp <= 0:
                CURRENCY += enemies_to_attack[0].worth
                enemies_to_attack[0].remove()
                enemies_onscreen.pop(enemies_onscreen.index(enemies_to_attack[0]))
                

    if not enemies_onscreen:
        pause = True
        counter = 0
        wave_count += 1
        for i in towers:
            i.life += 1
            if i.life % 3 == 0 and i.life <= 9:
                i.upgrade()
        

    

    if wave_count == len(waves):
        print('You won! You have unlocked a secret message')
        ans = input('Do you wanna read the secret message? (yes or no)')
        print('Choice is an illusion')
        sleep(2)
        print('DEEEEEEEEEEEEEEEZ NUTTTTTTTTTTTTTTTSSSSSSSSSSSSSSSSSSSSS YOU GOT RICK ROLLED')
        startfile('important.mp4')
        play = False

    if BASE_HP <= 0:
        print('You lowkey suck at this game, skill issue honestly!')
        sleep(2)
        print('You got rick rolled!!!!!!!!')
        startfile('important.mp4')
        play = False

    print('Health: ', BASE_HP)
    print('Money: ', CURRENCY)
    sleep(0.2)
