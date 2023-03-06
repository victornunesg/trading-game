# ----------------------------
# PROJECT - TRADING GAME SIMULATOR
# ----------------------------

import random

print('----------------------------')
print('TRADING GAME SIMULATOR')
print('----------------------------')

bag = ['black', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'white']
cash: float = 1000
draw: int = 1
print('Welcome to Trading Game Simulator!')
print('Alright! Let\'s get started!')
num_rounds = int(input('\nInput the number of rounds to be played: '))
print()

for draw in range(num_rounds):
    bet = float(input('Input your bet ($): '))
    draw_result = random.choice(bag)
    print(f'\nRound #{draw+1} result: {draw_result}')
    if draw_result == 'green':
        cash += bet
        print(f'Congratulations, you won ${bet}! Your current amount of cash is ${cash}')
    elif draw_result == 'black':
        cash += (bet*10)
        print(f'Congratulations, you won ${bet}! Your current amount of cash is ${cash}')
    elif draw_result == 'red':
        if (cash - bet) <= (cash/2):
            print('GAME OVER!')
            break
        else:
            cash -= bet
            print(f'Sorry, you lost ${bet}! Your current amount of cash is ${cash}')
            print('Keep going!')
    elif draw_result == 'white':
        if (cash - (bet*5)) <= (cash/2):
            print('GAME OVER!')
            break
        else:
            cash -= (bet*5)
            print(f'Sorry, you lost ${bet}! Your current amount of cash is ${cash}')
            print('Keep going!')
