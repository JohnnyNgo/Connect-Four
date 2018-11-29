#cfshared.py

import connectfour

def check_winner(game: connectfour.GameState) -> bool:
    '''checks if red or yellow won'''    
    winner = connectfour.winner(game)
    if winner != 0:
        if winner == 1:
            print('RED Player Wins')
        elif winner == 2:
            print('YELLOW Player Wins')
        return True
    

def start_game() -> connectfour.GameState:
    '''creates a new game state'''
    return connectfour.new_game()

def check_move(move:str, game: connectfour.GameState) -> bool:
    '''checks if the moves is good'''
    move = move.upper()

    try:
        if move[0:4] == 'DROP':
            connectfour.drop(game,(int(move[5:]) - 1))
        elif move[0:3] == 'POP':
            connectfour.pop(game,(int(move[4:]) - 1))
        else:
            return False
    except (connectfour.InvalidMoveError, ValueError, connectfour.GameOverError):
        return False
    else:
        return True


def main_game(move: str, game: connectfour.GameState):
    '''loops board and takes input action'''
    move = move.upper()
    
    if move[0:4] == 'DROP':
        game = connectfour.drop(game,(int(move[5:]) - 1))
    else:
        game = connectfour.pop(game,(int(move[4:]) - 1))

    print_board(game, game.board)
    print()

    return game

def print_board(game_state: connectfour.GameState, board: list):
    '''takes in game status and prints current board'''
    if game_state.turn == 1:
        print('RED PLAYERS TURN:')
    else:
        print('YELLOW PLAYERS TURN:')
    for num in range(len(board)):
        print(str(num+1) + '  ', end = '')
    print()

    for rows in range(len(board[0])):
        for columns in range(len(board)):
            if board[columns][rows] == 1:
                print('R  ', end = '')
            elif board[columns][rows] == 2:
                print('Y  ', end = '')
            else:
                print('.  ', end = '')
        print()
