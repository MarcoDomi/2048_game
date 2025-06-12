from enum import Enum

GAME_STATUS = Enum('GAME_STATUS', [("IN-PROGRESS", 0), ("WIN", 1), ("LOSE", 2)])

class GAME_STATUS(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    WIN = 2
    LOSE = 3

class game_2048:

    GAMEBOARD_DIM = 4

    def __init__(self):
        self.tile_count = 0
        self.game_state = GAME_STATUS.NOT_STARTED
        self.game_board = [[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]]

        self.valid_locations = {'A':(0,0), 'B':(0,1), 'C':(0,2), 'D':(0,3),
                                'E':(1,0), 'F':(1,1), 'G':(1,2), 'H':(1,3),
                                'I':(2,0), 'J':(2,1), 'K':(2,2), 'L':(2,3),
                                'M':(3,0), 'N':(3,1), 'O':(3,2), 'P':(3,3)}

        self.invalid_locations = dict()

    def init_game():
        pass

    def run_game():
        pass

    def print_board(self):
        row_line = "{:->34}".format("\n")  #len of row line is 33. set to 34 to accommadate newline esc seq
        grid_cell = "|{:^7}".format("")

        grid_row = f"{row_line}{grid_cell}{grid_cell}{grid_cell}{grid_cell}|\n"
        board = f"{grid_row}{grid_row}{grid_row}{grid_row}{row_line}"

        print(board)

    def check_game_status(self):
        pass

    def place_item(self):
        pass

    def shift_up(self):
        pass

    def shift_down(self):
        pass

    def shift_right(self):
        pass

    def shift_left(self):
        pass


# game_2048().print_board()
