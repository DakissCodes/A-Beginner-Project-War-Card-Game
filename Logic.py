from Classes import Cards
from Classes import Deck
from Classes import Player
from Classes import Funcs
import random


'''
in oder to see the events, user must input 'next'
to move on to the next draw. 

provide visual output to show the cards drawn, who won 
the draw, the len() of each deck.
'''
game = True
while game:
    deck = []
    player1 = []
    player2 = []

    Deck().make_a_deck(deck)
    
    random.shuffle(deck)
    
    Deck().random_distribute(deck,player1,player2)
    Funcs.display(player1,player2)
    print(len(player1))
    print(len(player2))
    Funcs.cont()
    play = True
    rounds = 0
    while play:
        card1 = ''
        card2 = ''
        card1, card2 = Player().draw_one(player1,player2)
        if card1 == card2:
            win = 0
        else:
            win = Funcs.draw_win(Deck.rank,card1,card2)
        # Funcs.display(player1,player2)
        if win == 0:
            print('WAR!')
            cards1 = []
            cards2 = []
            while win == 0:
                rounds += 1
                print('ITS A WAR! \n')

                two_card1,two_card2 = Player().draw_two(player1,player2)
                for _ in two_card1: cards1.append(_)
                for _ in two_card2: cards2.append(_)
                win = Funcs().draw_win(random.choice(two_card1),random.choice(two_card2))
                two_card1.clear()
                two_card2.clear()
                print(cards1)
                print(cards2)
                if win == 1:
                    print('PLAYER ONE WON!')
                    for _ in cards1: player1.append(_)
                    for _ in cards2: player1.append(_)
                    player1.append(card1)
                    player1.append(card2)
                    win = -1
                    print(f'Len of player 1: {str(len(player1))}')
                    print(f'Len of player 2: {str(len(player2))}')
                    cards1.clear()
                    cards2.clear()
                    Funcs.cont()
                elif win == 2:
                    print('PLAYER TWO WON!')
                    for _ in cards1: player2.append(_)
                    for _ in cards2: player2.append(_)
                    player2.append(card1)
                    player2.append(card2)
                    win = -1
                    print(f'Len of player 1: {str(len(player1))}')
                    print(f'Len of player 2: {str(len(player2))}')
                    cards1.clear()
                    cards2.clear()
                    Funcs.cont()
                else:
                    print("IT'S A TIE!")
                    Funcs.cont()
                    continue 
            
            # give the stack here

        elif win == 1:
            rounds += 1
            print('PLAYER ONE WON!')
            player1.append(card1)
            player1.append(card2)
            print(f'Len of player 1: {str(len(player1))}')
            print(f'Len of player 2: {str(len(player2))}')
            print('player 1:' + card1)
            print('plaeyr 2:' + card2)
            Funcs.cont()
        elif win == 2:
            rounds += 1
            print('PLAYER TWO WON!')
            player2.append(card1)
            player2.append(card2)
            print(f'Len of player 1: {str(len(player1))}')
            print(f'Len of player 2: {str(len(player2))}')
            print('player 1:' + card1)
            print('plaeyr 2:' + card2)
            Funcs.cont()
        elif win == 3:
            play = False
        if len(player1) == 0:
            print('player one wins the whole game!')
            break
        elif len(player2) == 0:
            print('player two wins the whole game!')
            break
    print(f'Number of rounds: {str(rounds)}')
    run_again = input('again?: ')
    if run_again.lower()[0] == 'y':
        continue
    else:
        game == False







