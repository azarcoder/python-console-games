import random 
from colorama import Fore, Back, Style, init
import pwinput
import cowsay
from tabulate import tabulate
from pyfiglet import Figlet
init()
f = Figlet()
print(f.renderText('Welcome to the GAME'))

p1 = 0 
p2 = 0 
toggle = 0

cards = ['a','2','3','4','5','6','7','8','9','10','j','k','q']

coin = ['head', 'tail']

player_1 = input('Player 1, enter your choice: (head/tail) : ')

random.shuffle(coin)

if player_1 == coin[0]:
    print(Fore.MAGENTA + f'Nice :) coin is {coin[0]}')
    toggle = 1
    print(Fore.GREEN + 'Player 1 you can start the game first!')
else:
    print(Fore.MAGENTA + f'OOPS :( coin is {coin[0]}')
    toggle = 2
    print(Fore.GREEN + 'Player 2 you can start the game first!')

print(Back.RED +'RULES : who wins 3 times, they consider as a winner!')
print(Style.RESET_ALL)

t = 0
first_game = True
p1_choices = []
p2_choices = []
xx = False
player_input1 = None 
player_input2 = None
while True:
    if p1 == 3:
        cowsay.turtle(Fore.GREEN + 'Player 1 Won the game')
        break
    elif p2 == 3:
        cowsay.turtle(Fore.GREEN + 'Player 2 Won the game')
    t+=1
    print(f'\n------>round : {t}<------')
    if t > 1:
        first_game = False
    if toggle == 1:
        if first_game:
            p1_choices.clear()
            p2_choices.clear()
        print(Style.RESET_ALL)
        while True:
            try:
                player_input1 = pwinput.pwinput(prompt='Player 1: ')
                if not player_input1 in  cards:
                    raise ValueError
            except ValueError:
                pass
            else:
                break

        if len(p2_choices) > 0 and p2_choices[-1] == player_input1:
            p1+=1
            if p1 < 3:
                print(Fore.YELLOW + f'Cheers ! Player 1, you have to win { 3-p1 } times to win the game :)')
            print(Back.LIGHTBLUE_EX+ f'Your Score: {p1}')
            toggle=1
            print(Style.RESET_ALL)
            print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
            t = 0
            first_game = True
            p1_choices.clear()
            p2_choices.clear()
            continue
        if xx == False:
            while True:
                try:
                    player_input2 = pwinput.pwinput(prompt='Player 2: ')
                    if  not player_input2 in  cards:
                        raise ValueError
                except ValueError:
                    pass
                else:
                    break
            
        
        

        if first_game:
            p1_choices.clear()
            p2_choices.clear()
            if player_input2 == player_input1:
                p2+=1
                if p2 < 3:
                    print(Fore.YELLOW + f'Cheers ! Player 2, you have to win { 3-p2 } times to win the game :)')
                print(Back.LIGHTBLUE_EX+ f'Your Score: {p2}')
                toggle=2
                print(Style.RESET_ALL)
                print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
                t = 0
                first_game = True
                p1_choices.clear()
                p2_choices.clear()
                xx = False
            
        else:
            if player_input1 == p2_choices[-1]:
                p1+=1
                if p1 < 3:
                    print(Fore.YELLOW + f'Cheers ! Player 1, you have to win { 3-p1 } times to win the game :)')
                print(Back.LIGHTBLUE_EX+ f'Your Score: {p1}')
                toggle=1
                print(Style.RESET_ALL)
                print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
                t = 0
                first_game = True
                p1_choices.clear()
                p2_choices.clear()
                xx = False
            elif player_input2 == player_input1:
                p2+=1
                if p2 < 3:
                    print(Fore.YELLOW + f'Cheers ! Player 2, you have to win { 3-p2 } times to win the game :)')
                print(Back.LIGHTBLUE_EX+ f'Your Score: {p2}')
                toggle=2
                print(Style.RESET_ALL)
                print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
                t = 0
                first_game = True
                xx = False
        
        p1_choices = p1_choices[:-1]
        p2_choices = p1_choices[:-1]
        p1_choices.append(player_input1)
        p2_choices.append(player_input2)


    elif toggle == 2:
        if first_game:
            p1_choices.clear()
            p2_choices.clear()
        print(Style.RESET_ALL)
        while True:
            try:
                player_input2 = pwinput.pwinput(prompt='Player 2: ')
                if  not player_input2 in  cards:
                    raise ValueError
            except ValueError:
                pass
            else:
                break

        if len(p1_choices) > 0 and p1_choices[-1] == player_input2:
            p2+=1
            if p2 < 3:
                print(Fore.YELLOW + f'Cheers ! Player 2, you have to win { 3-p2 } times to win the game :)')
            print(Back.LIGHTBLUE_EX+ f'Your Score: {p2}')
            print(Style.RESET_ALL)
            print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
            toggle = 2
            t = 0
            first_game = True
            p1_choices.clear()
            p2_choices.clear()
            continue

        if xx == False:
            while True:
                try:
                    player_input1 = pwinput.pwinput(prompt='Player 1: ')
                    if  not player_input1 in  cards:
                        raise ValueError
                except ValueError:
                    pass
                else:
                    break

        if first_game:
            p1_choices.clear()
            p2_choices.clear()
            if player_input1 == player_input2:
                p1+=1
                if p1 < 3:
                    print(Fore.YELLOW + f'Cheers ! Player 1, you have to win { 3-p1 } times to win the game :)')
                print(Back.LIGHTBLUE_EX+ f'Your Score: {p1}')
                print(Style.RESET_ALL)
                print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
                toggle = 1
                t = 0
                first_game = True
                xx = False
                continue
            
        else:
            if player_input2 == p1_choices[-1]:
                p2+=1
                if p2 < 3:
                    print(Fore.YELLOW + f'Cheers ! Player 2, you have to win { 3-p2 } times to win the game :)')
                print(Back.LIGHTBLUE_EX+ f'Your Score: {p2}')
                print(Style.RESET_ALL)
                print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
                toggle = 2
                t = 0
                first_game = True
                p1_choices.clear()
                p2_choices.clear()
                xx = False
                continue
            elif player_input1 == player_input2:
                p1+=1
                if p1 < 3:
                    print(Fore.YELLOW + f'Cheers ! Player 1, you have to win { 3-p1 } times to win the game :)')
                print(Back.LIGHTBLUE_EX+ f'Your Score: {p1}')
                print(Style.RESET_ALL)
                print(tabulate([["Player 1 Score", "Player 2 Score"], [p1, p2]], headers="firstrow"))
                toggle = 1
                t = 0
                first_game = True
                p1_choices.clear()
                p2_choices.clear()
                xx = False
                continue
                
        p1_choices = p1_choices[:-1]
        p2_choices = p1_choices[:-1]
        p1_choices.append(player_input1)
        p2_choices.append(player_input2)
        
    if p1 == 3:
        print(f' Player 1 won the game :)')
        break
    elif p2 == 3:
        print(f'Player 2 won the game :)')
        break
