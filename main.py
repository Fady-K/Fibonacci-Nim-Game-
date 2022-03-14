# game status
game_running = True
current_player = None
first_move = True
pile = 20
last_with_draw = None

def display_game_status():
    global game_running, current_player, first_move, pile, last_with_draw
    print(f"Game_Running: {game_running}\nFirst_Move: {first_move}\nPlayer: {current_player}\nPile: {f'{pile} Coins'if pile > 1 else f'{pile} Coin'}\nLast_with_Draw: {last_with_draw}" )

def first_player():
    global current_player, pile, last_with_draw, first_move
    current_player = "first_player"
    if first_move:
        print("this the first move, first_player isn't allowed to take all coins!!".title())
        inp = int(input("first_player: "))
        if inp in range(1, pile + 1):
            pile -= inp
            last_with_draw = inp
            first_move = False
        else:
            print("!!sorry, this number does not meet the rules!!".upper())




    else:
        inp = int(input("first_player: "))
        if inp in range(1, (last_with_draw * 2) + 1):
            pile -= inp
            last_with_draw = inp
        else:
            print("!!sorry, this number does not meet the rules!!".upper())


def second_player():
    global current_player, pile, last_with_draw
    current_player = "second_player"
    inp = int(input("second_player: "))
    if inp in range(1, (last_with_draw * 2) + 1):
        pile -= inp
        last_with_draw = inp

    else:
        print("!!sorry, this number does not meet the rules!!".upper())


def win():
    global pile
    if pile == 0:
        return True

def check_win():
    global current_player, game_running
    if win():
        print(f"!!!!!{current_player} Wins!!!!!".upper())
        game_running = False
        input("\npress_enter...................Exit!".upper())
        quit()


display_game_status()
print("###################################################")
while game_running:
    first_player()
    print("###################################################")

    display_game_status()
    check_win()
    print("###################################################")
    second_player()
    print("###################################################")

    display_game_status()
    check_win()
    print("###################################################")


