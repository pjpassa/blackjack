from player import Player
from dealer import Dealer
from deck import Deck
from display import Display


class Game():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.display = Display(7)
        self.pot = 0

    def print_display(self, wait=False):
        self.update_display()
        self.display.print_display()
        if wait:
            self.get_continue()

    def update_display(self):
        display_list = ["Dealer:", self.dealer.display_hand(False),
                        "Score: " + str(self.dealer.get_hand_value()) +
                        " | Pot: " + str(self.pot),
                        "- "*20, "You:", self.player.display_hand(),
                        "Score: " + str(self.player.get_hand_value()) +
                        " | Money: " + str(self.player.score)]
        for index, string in enumerate(display_list):
            self.display.set_display(string, index)

    def start_round(self):
        self.deck = Deck()
        self.pot = self.player.bet(self.get_bet_input())
        self.player.start_game()
        self.dealer.start_game()
        self.add_message("Welcome to BlackJack!")
        self.get_continue()
        self.initial_deal()
        if dealer.has_blackjack() and player.has_blackjack():
            self.add_message("The round is a push.")
            self.print_display(True)
            return False
        elif player.has_blackjack():
            self.add_message("You have BlackJack!")
            self.add_message("You win the hand!")
            self.print_display(True)
            self.add_message("You won {}.".format(bet))
            self.player.add_score(bet)
            self.bet = 0
            self.print_display(True)
            return False
        elif dealer.has_blackjack():
            self.add_message("Dealer has BlackJack.")
            self.add_message("You lose the hand.")
            self.print_display(True)
            self.bet = 0
            return False
        return self.play()

    def initial_deal(self):
        for i in range(2):
            self.player.add_card(self.deal())
            self.update_display(True)
            self.dealer.add_card(self.deal())
            self.update_display(True)

    def get_input(self, type):
        self.print_display()
        if type == "hand":
            return self.get_hand_input()
        elif type == "bet":
            return self.get_bet_input()
        elif type = "choice":
            return self.get_stand_or_hit()

    def get_hand_input(self):
        while True:
            string = "Do you want to play another hand? (y/n) > "
            value = input(string).lower()
            if value in ("y", "n"):
                return value
            self.add_message("Please enter 'y' or 'n'")
            self.print_display()

    def get_bet_input(self):
        # return input("How much do you want to bet?")
        self.add_message("Betting 10.")
        return 10

    def get_stand_or_hit(self):
        while True:
            string = "Do you want to stand or hit? > "
            value = input(string).lower()
            if value in ("stand", "hit"):
                return value
            self.add_message("Please enter 'stand' or 'hit'")
            self.print_display()

    def add_message(self, message):
        self.display.add_messages(message)

    def get_continue(self):
        input("Press Enter to continue.")

    def deal(self):
        return self.deck.draw()

    def player_play(self):
        while self.get_input("choice") == "hit":
            self.player.add_card(self.draw())
            if self.player.has_blackjack():
                self.add_message("You have BlackJack!")
                self.print_display(True)
                return True
            elif self.player.is_busted():
                self.add_message("You have busted.")
                self.print_display(True)
                return False
        return True

    def dealer_play(self):
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card(self.draw())
            if self.dealer.has_blackjack():
                self.add_message("Dealer has BlackJack.")
                self.print_display(True)
                break
            if self.dealer.is_busted():
                self.add_message("Dealer is busted!")
                self.print_display(True)
                break

    def play(self):
        if self.player_play():
            self.dealer_play()
        if dealer.has_blackjack() and player.has_blackjack():
            self.add_message("The round is a push.")
            self.print_display(True)
            return False
        elif player.has_blackjack():
            self.add_message("You have BlackJack!")
            self.add_message("You win the hand!")
            self.print_display(True)
            self.add_message("You won {}.".format(bet))
            self.player.add_score(bet)
            self.bet = 0
            self.print_display(True)
            return False
        elif dealer.has_blackjack():
            self.add_message("Dealer has BlackJack.")
            self.add_message("You lose the hand.")
            self.print_display(True)
            self.bet = 0
            return False
