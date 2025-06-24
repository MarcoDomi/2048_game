from game_2048 import game_2048
gg = game_2048()

gg.run_game()

while True:
    choice = input("enter Choice ")
    if choice == 'w':
        gg.shift_up()

    elif choice == 'a':
        gg.shift_left()

    elif choice == 's':
        gg.shift_down()

    elif choice == 'd':
        gg.shift_right()
        
    gg.print_board()
