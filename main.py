from game_2048 import game_2048
gg = game_2048()

gg.run_game()

choice = int(input("1: shift up "))
if choice == 1:
    gg.shift_up()
    gg.print_board()


