'''
This program is a very basic version of tic tac toe game. Below I have explained how this game works..

GamePlay:
It prints a empty tic tac toe board on the screen.

Since its a 2 player game, this game prompts users to name 2 players who going to play..

After getting the player name, it will be randomly decided which player will be using mark 'x' and mark 'o'.

Then input will be received from the player and the updated tic tac toe board will be printed on the screen on                            everytime the player given the location to place the marker.

when a player successfuly placed 3 marks on horizontal|vertical|digonal line before the other player, then the  player
will be declared winner and an option will be asked to play a rematch or a new match will be decided..
               
Based on the reply, a new match will be played or a rematch or the game will quit

'''
import random

# Global tic_tac variable for the location of the board 
tic_tac= {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
print('Empty tic tac board')

#function to print the board..
def print_dict(tic_tac):
    print('  |   |   ')
    print('{:2}|{:3}|{:2}'.format(tic_tac['1'],tic_tac['2'],tic_tac['3']))
    print('  |   |   ')
    print('----------')
    print('  |   |   ')
    print('{:2}|{:3}|{:2}'.format(tic_tac['4'],tic_tac['5'],tic_tac['6']))
    print('  |   |   ')
    print('----------')
    print('  |   |   ')
    print('{:2}|{:3}|{:2}'.format(tic_tac['7'],tic_tac['8'],tic_tac['9']))
    print('  |   |   ')

print_dict(tic_tac)

# Getting the board position from player 1 and printing the updated tic tac toe board
def player1_func(player1):
    while True:
        player= input('{} turn:'.format(player1))
        if player not in ['1','2','3','4','5','6','7','8','9']:
            continue
        if not tic_tac[player]:
            tic_tac[player] = 'x'
        else:
            print('given place occupied please try again')
            continue
        print_dict(tic_tac)
        break

# Getting the board position from player 2 and printing the updated tic tac toe board
def player2_func(player2):
    while True:
        player= input('{} turn: '.format(player2))
        if player not in ['1','2','3','4','5','6','7','8','9']:
            continue
        if not tic_tac[player]:
            tic_tac[player] = 'o'
        else:
            print('given place occupied please try again')
            continue
        print_dict(tic_tac)
        break

# Checking whether player 1 or player 2 is the winner 
def check_winner(mark):
    if tic_tac['1'] == mark and tic_tac['2'] == mark and tic_tac['3'] == mark:
        return True
    elif tic_tac['4'] == mark and tic_tac['5'] == mark and tic_tac['6'] == mark:
        return True
    elif tic_tac['7'] == mark and tic_tac['8'] == mark and tic_tac['9'] == mark:
        return True
    elif tic_tac['1'] == mark and tic_tac['4'] == mark and tic_tac['7'] == mark:
        return True
    elif tic_tac['2'] == mark and tic_tac['5'] == mark and tic_tac['8'] == mark:
        return True
    elif tic_tac['3'] == mark and tic_tac['6'] == mark and tic_tac['9'] == mark:
        return True
    elif tic_tac['1'] == mark and tic_tac['5'] == mark and tic_tac['9'] == mark:
        return True
    elif tic_tac['3'] == mark and tic_tac['5'] == mark and tic_tac['7'] == mark:
        return True
    else:
        return False

# game_play function calls functions to get the input from the players and calls functions to determine the winners..
def game_play(player1,player2):
    for i in range(5):
        player1_func(player1)
        Result = check_winner('x')
        if Result:
            print('{} is the winner'.format(player1))
            break
        i += 1
        if i > 4:
            print('Game end in draw')
            break
        player2_func(player2)
        Result = check_winner('o')
        if Result:
            print('{} is the winner'.format(player2))
            break

# Getting the 2 players name and randomly assigning the mark 'x' and 'o' to the two players
def who_gonna_play():
    player_1 = input('Enter the name of the player: ')
    player_2 = input('Enter the name of the other player: ')
    toss = random.randint(0,1)
    if toss:
        print(player_1 + ' will be assigned marker "x" and '+player_2+' will be assigned marker "o" ')
        return player_1,player_2
    else:
        print(player_2 + ' will be assigned marker "x" and'+player_1+' will be assigned marker "o" ')
        return player_2,player_1

#main function to start functions who_gonna_play and game_play and based on player input 'rematch or new game' will be determined..
def main():
    global tic_tac
    player1,player2 = who_gonna_play()
    game_play(player1,player2)
    
    while True:
        match = input('Type "N" for the new game and "R" for the rematch:')
        
        if match.lower().startswith('n'):
            tic_tac = {'1':'' ,'2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'' ,'9':''}
            player1,player2 = who_gonna_play()
            print_dict(tic_tac)
            game_play(player1,player2)
        elif match.lower().startswith('r'):
            tic_tac = {'1':'' ,'2':'', '3':'', '4':'', '5':'', '6':'', '7':'', '8':'' ,'9':''}
            print_dict(tic_tac)
            game_play(player1,player2)
        else:
            print('Thanks for playing the game')
            break


if __name__ == '__main__':
    main()
    
   
