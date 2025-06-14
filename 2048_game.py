from enum import Enum
import random 

class GAME_STATUS(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    WIN = 2
    LOSE = 3

class game_2048:

    GAMEBOARD_DIM = 4

    def __init__(self): #sets an uninitialized state for game
        self.tile_count = 0
        self.game_state = GAME_STATUS.NOT_STARTED
        self.game_board = [['', '', '', ''], #empty cells represented by empty strings.
                           ['', '', '', ''],
                           ['', '', '', ''],
                           ['', '', '', '']]

        self.valid_locations = {'A':(0,0), 'B':(0,1), 'C':(0,2), 'D':(0,3), #all empty locations on gameboard
                                'E':(1,0), 'F':(1,1), 'G':(1,2), 'H':(1,3),
                                'I':(2,0), 'J':(2,1), 'K':(2,2), 'L':(2,3),
                                'M':(3,0), 'N':(3,1), 'O':(3,2), 'P':(3,3)}

        self.invalid_locations = dict() #when location is filled it is popped from valid_locations and place here

    def init_game(self):
        # randomly place 2 tiles
        start_values = [2,4]
        start_value1, start_value2 = random.choices(start_values, weights=[3,1],k=2) #make weighted random choice between 2 and 4.  
                                                                                     #return list of two randomly chosen values where 2 has higher weight.
        self.place_item(start_value1)
        self.place_item(start_value2)

    def run_game(self):
        self.init_game()
        self.game_state = GAME_STATUS.IN_PROGRESS
        self.print_board()
        pass

    def print_board(self):
        row_line = "{:->34}".format("\n")       #len of row line is 33. set to 34 to accommadate newline esc seq
        board = []                              #esc seq is left aligned
        for i in range(game_2048.GAMEBOARD_DIM):#iterate thru each row in board
            grid_row = "{}|{:^7}|{:^7}|{:^7}|{:^7}|".format(row_line,*self.game_board[i]) #use string format to insert row_line and four game_board values
            board.append(grid_row)                                                        #use unpack operator to unpack each row in game_board

        board.append(row_line)   #append last row_line onto bottom of board
        board = "\n".join(board) 
        print(board)

    def check_game_status(self):
        pass

    def place_item(self, num): #TODO add a fail state for when there are no more valid locations
        keylist = list(self.valid_locations.keys())
        index = random.randint(0, len(keylist)-1)
        chosenKey = keylist[index]

        location = self.valid_locations.pop(chosenKey)
        self.invalid_locations[chosenKey] = location

        self.game_board[location[0]][location[1]] = num

    def shift_up(self):
        pass

    def shift_down(self):
        pass

    def shift_right(self):
        pass

    def shift_left(self):
        pass


gg = game_2048()

gg.run_game()
