import cfshared

def run():
    '''loops input and updates gamestate'''
    game = cfshared.start_game()
    cfshared.print_board(game,game.board)
    print()
    
    while True:
        move = input('Enter DROP/POP and a num 1-' + str(len(game.board)) + ': ').strip()
        if cfshared.check_move(move,game) == True:  
            game = cfshared.main_game(move, game)
            if cfshared.check_winner(game) == True:
                break
        else:
            print('Invalid Input, please try again.')
            print()
    
if __name__ == '__main__':
    run()
