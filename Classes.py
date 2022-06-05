'''
WAR CARD GAME

52 cards, each players gets half.

To play, each players shows one card.
Whomever has a higher ranked card, gets both of the cards 
at the bottom of his stack, 

If the cards have the same rank, we have a WAR. Each players draws 
2 cards: one faced up and one faced down. The player with the higher
ranked card takes both piles (6 cards). If the cards are the same 
ranks again, the process repeats (draw 2 cards each, one face up one face down). 
Winner takes all 10 cards.
'''
import random
class Cards():
    
    rank = ['Ace','King','Queen','Joker','Ten','Nine','Eight','Seven','Six','Five',\
        'Four','Three','Two']

class Deck(Cards):
    def make_a_deck(self,whole_deck):
        for _ in self.rank:
            count = 0
            while True:
                whole_deck.append(_)
                count += 1
                if count == 4:
                    break
        
    def random_distribute(self,whole_deck,player1,player2): 
        for _ in range(len(whole_deck)):
            if (_ + 1) % 2 != 0:
                player1.append(whole_deck[_])
            else:
                player2.append(whole_deck[_])
class Player(Deck):
    
    def draw_one(self,player1,player2):
        if len(player1) == 0 or len(player2) == 0:
            return 0,0
        else:
    
            player1_draw = player1.pop(0) 
            player2_draw = player2.pop(0)
        return player1_draw,player2_draw
    def draw_two(self,player1,player2): # if len(deck) < 2, must be able to draw the cards left
        player1_draw = []
        player2_draw = []     
                # without making an error!
        for _ in range(3):
            if len(player1) == 0:
                player2_draw.append(player2.pop(0))
                continue
            elif len(player2) == 0:
                player1_draw.append(player1.pop(0))
                continue
            else:
                player1_draw.append(player1.pop(0))
                player2_draw.append(player2.pop(0))

            #player1_draw = [player1.pop(0),player1.pop(0)]
            #player2_draw = [player2.pop(0),player2.pop(0)]
        return player1_draw,player2_draw
    

# A FUNCTION THAT RETURNS THE HIGHER RANK BETWEEN
# THE CARDS. 
class Funcs():

    def display(player1,player2):
        print('PLAYER 1 DECK: ')
        print(player1)
        print('PLAYER 2 DECK: ')
        print(player2)

    def draw_win(rank,card1,card2):
        if card1 == 0 or card2 == 0:
            return 3
        elif card1 == card2:
            return 0
        elif Deck().rank.index(card1) < Deck().rank.index(card2):
            return 1
        elif Deck().rank.index(card1) > Deck().rank.index(card2):
            return 2

    def cont():
        #response = input('draw?')
        pass
            
