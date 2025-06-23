from game_2048 import game_2048
gg = game_2048()

gg.run_game()

choice = int(input("enter Choice "))
if choice == 1:
    gg.shift_up()
    gg.print_board()

elif choice == 2:
    gg.shift_left()
    gg.print_board()


