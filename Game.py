import math
from random import randint


class Game:
    def __init__(self, players, rounds):
        self.pot = 0
        self.players = players
        self.max_rounds = rounds

    def start_game(self):
        has_money = True
        current_round = 1
        while has_money and current_round < self.max_rounds:
            for j in self.players:
                j.tokens -= 1
                self.pot += 1
                has_money = j.tokens > 0
                if not has_money:
                    break
            for j in self.players:
                print("Next player spinning")
                self.play_round(j)
                has_money = j.tokens > 0
                if not has_money:
                    break
            current_round += 1
        print(f'{self.pot} Remaining')
        for i in self.players:
            print(i)

    def play_round(self, current_player):
        letter = randint(1, 4)
        if letter == 1:
            print('GIMEL')
            current_player.tokens += self.pot
            self.pot = 0
        elif letter == 2:
            print('HEY')
            # ceiling and floor help prevent an improper distribution of tokens
            current_player.tokens += math.ceil(self.pot / 2)
            self.pot = math.floor(self.pot / 2)
        elif letter == 3:
            print('SHIN')
            current_player.tokens -= 1
            self.pot += 1
        elif letter == 4:
            print('NUN')
