import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
number_cards = 5
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def make_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append((suit, value))
    return deck


deck = make_deck()


def make_draw():
    draw = random.sample(deck, number_cards)
    for card in draw:
        deck.remove(card)
    return draw


player1 = make_draw()
player2 = make_draw()

current_card = ("spades", "A")

current_player1_turn = True
if ("spades", "A") in player1:
    print("Player 1 has ace of spades")
    player1.remove(("spades", "A"))
    current_player1_turn = False
elif ("spades", "A") in player2:
    print("Player 2 has ace of spades")
    player2.remove(("spades", "A"))

else:
    print("The deck has ace of spades")
    deck.remove(("spades", "A"))

def print_hand(player_deck):
    card_rows = []
    for card in player_deck:
        rows = ['', '', '', '']

        current_card_class = SPADES

        if card[0] == 'diamonds':
            current_card_class = DIAMONDS
        elif card[0] == 'hearts:':
            current_card_class = HEARTS
        elif card[0] == 'spades':
            current_card_class = SPADES
        else:
            current_card_class = CLUBS

        rows[0] += ' ___ '
        rows[1] += '|  {}|'.format(card[1])
        rows[2] += '| {} |'.format(current_card_class)
        rows[3] += '|{}__|'.format(card[1])

        card_rows.append(rows)

    space = "    "
    for card in card_rows:
        print(card[0], end=space)
    print()
    for card in card_rows:
        print(card[1], end=space)
    print()
    for card in card_rows:
        print(card[2], end=space)
    print()
    for card in card_rows:
        print(card[3], end=space)







player_card = ()

pile_cards = []

bs_card = ()

for value in values:
    if current_player1_turn == True:

        print_hand(player1)

        print()
        print()
        print()

        print(f"Player1 put down your {value}s")
        input1 = input("Player1 what card would you like to put down? ")

        bs_card = player1[int(input1) - 1]

        player1.pop(int(input1) - 1)
        print(player1)

        if len(player1) == 0:
            print("Player1 Wins")

        current_player1_turn = False


    elif current_player1_turn == False:
        bs_input = input("Player2 do you call bs on player1 (yes/no): ")
        if bs_input == "yes" and bs_card[1] == value:
            print("player2 takes all of pile")
        elif bs_input == "yes" and bs_card[1] != value:
            print("player1 takes all of pile")

        print(f"player2 put down your {value}s")

        print_hand(player1)

        print()
        print()
        print()

        print(f"Player2 put down your {value}s")
        input1 = input("Player2 what card would you like to put down? ")
        player2.pop(int(input1) - 1)
        print(player2)

        if len(player2) == 0:
            print("Player2 Wins")

        current_player1_turn = True



# player can put down 1 or more cards
# make sure after we go through the deck we go back to start
# able to call bs
