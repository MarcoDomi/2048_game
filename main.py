from game_2048 import game_2048
gg = game_2048()

gg.run_game()

choice = int(input("enter Choice "))
if choice == 1:
    gg.shift_up()

elif choice == 2:
    gg.shift_left()

elif choice == 3:
    gg.shift_down()

elif choice == 4:
    gg.shift_right()
    
gg.print_board()
