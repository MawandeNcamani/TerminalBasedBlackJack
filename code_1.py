#MawandeNcamani
#Made plagiarism free and with good spirit

import random

suits = ('Diamonds', 'Spades','Hearts','Clubs')

ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','king','queen','ace')

values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

playing = True



class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of '+ self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has '+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    
    def deal(self):
        single_card = self.deck.pop()
        
        return single_card 
    
class Hand:
    def __init__(self):
        self.cards= []
        self.value= 0
        self.aces = 0
    
    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
    
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.values -= 10
            self.aces -= 1
            
            
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
        
        
    def lose_bet(self):
        self.total -= self.bet
          
        
def take_bet(chips):
        
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet, you have 100? '))
        except:
            
            print('Sorry please provide a valid integer')
        else:
            
            if chips.bet>chips.total:
                    print('Sorry, you do not have enough chips! You have {} chips'.format(chips.total))
            else:
                break
                      
                      
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
                      
def hit_or_stand(deck,hand):
    global playing
        
    while True:
        x = input('Hit or Stand? Enter h or s: ')
            
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player Stands, Dealers turn!')
            playing = False
        else:
            print('Invalid, please enter h or s')
            continue
                
        break
            
            
def show_some(player,dealer):
    print('DEALERS HAND: ')
    print('Mawande has one card hidden of course! The other card is: ')
    print(dealer.cards[1])
    print('\n')
    print('PLAYERS HAND')
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    print('DEALERS HAND: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND: ')
    for card in player.cards:
          print(card)
        
        
            
def player_bust(player,dealer,chips):
    print('You have busted! And you have lost to the legendary Mawande')
    chips.lose_bet()
        
                    
def player_wins(player,dealer,chips):
    print('You win! You beat the great dealer! Do it again!')
    chips.win_bet()    
        
        
def dealer_bust(player,dealer,chips):
    print('Dealer Busted!! You beat Mawande!')
    chips.win_bet()
        
def dealer_wins(player,dealer,chips):
    print('Dealer WINS, Mawande is the LEGENDARY dealer!')
    chips.lose_bet()
        
        
def push(player,dealer):
    print('Nobody won, PUSH!')
        
while True:
    print('Welcome to Blackjack, you are up against Mawande, the legendary dealer!')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_bust(player_hand,dealer_hand,player_chips)
            
            break
            
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_bust(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
    print('\n Player total chips are at: {}'.format(player_chips.total))    
    
    new_game = input('would you like to play another hand against the legendary dealer Mawande? y/n ')
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank You for playing!')
        break
