from Game import Game
from Player import Player

print("Happy Chanuka! Time to play Dreidel!")
print("The rules of a dreidel game are simple")
print("GIMEL = player gets the entire pot")
print("HEY = player gets half the pot")
print("SHIN = player needs to put one token into the pot")
print("NUN = player gets nothing")


def get_number_of_players():
    minimum_2_players_needed = True
    number_of_players = 0
    while minimum_2_players_needed:
        number_of_players = int(input("How many people will be playing?"))
        if number_of_players < 2:
            print(f'Please enter a valid number, minimum 2 players needed')
        else:
            minimum_2_players_needed = False
            print('Next step')
    return number_of_players


def get_number_of_tokens_per_player():
    minimum_5_tokens_needed = True
    starting_amount = 0
    while minimum_5_tokens_needed:
        starting_amount = int(input('How many tokens should each person start with?'))
        if starting_amount < 5:
            print(f'Each player must have at least 5 tokens')
        else:
            print('Setup almost complete')
            minimum_5_tokens_needed = False
    return starting_amount


def get_number_of_rounds():
    minimum_7_rounds_needed = True
    rounds = 0
    while minimum_7_rounds_needed:
        rounds = int(input("How many rounds do you want to play?"))
        if rounds < 7:
            print(f'Please enter a valid number, minimum 7 rounds needed')
        else:
            minimum_7_rounds_needed = False
    return rounds


num_players = get_number_of_players()
num_tokens = get_number_of_tokens_per_player()
num_rounds = get_number_of_rounds()

player_list = []
for i in range(0, num_players):
    if i > 0:
        print('Next player')
    name = input('What is your name?')
    player = Player(name, num_tokens)
    player_list.append(player)


my_game = Game(player_list, num_rounds)
my_game.start_game()
