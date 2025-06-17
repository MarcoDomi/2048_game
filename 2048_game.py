from enum import Enum
import random 

class GAME_STATUS(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    WIN = 2
    LOSE = 3

class game_2048:

    GAMEBOARD_ROW = 4
    GAMEBOARD_COL = 4

    def __init__(self): #sets an uninitialized state for game
        self.tile_count = 0
        self.game_state = GAME_STATUS.NOT_STARTED
        self.game_board = [['', '', '', ''], #empty cells represented by empty strings.
                           ['', '', '', ''],
                           ['', '', '', ''],
                           ['', '', '', '']]

        self.empty_locations = {(0,0):(0,0), (0,1):(0,1), (0,2):(0,2), (0,3):(0,3), #empty locations are removed when value is inserted
                                (1,0):(1,0), (1,1):(1,1), (1,2):(1,2), (1,3):(1,3), #this limits possible locations when placing new value 
                                (2,0):(2,0), (2,1):(2,1), (2,2):(2,2), (2,3):(2,3), 
                                (3,0):(3,0), (3,1):(3,1), (3,2):(3,2), (3,3):(3,3)}

        self.occupied_locations = dict() #when location is filled its removed from empty_locations and place here
                                         #might remove
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
        for i in range(game_2048.GAMEBOARD_ROW):#iterate thru each row in board
            grid_row = "{}|{:^7}|{:^7}|{:^7}|{:^7}|".format(row_line,*self.game_board[i]) #use string format to insert row_line and four game_board values
            board.append(grid_row)                                                        #use unpack operator to unpack each row in game_board

        board.append(row_line)   #append last row_line onto bottom of board
        board = "\n".join(board) 
        print(board)

    def check_game_status(self):
        pass

    def place_item(self, num): #TODO add a fail state for when there are no more valid locations
        keylist = list(self.empty_locations.keys())
        index = random.randint(0, len(keylist)-1)

        key = keylist[index]
        location = self.empty_locations.pop(key)

        self.occupied_locations[key] = location
        self.game_board[location[0]][location[1]] = num

    def shift_up(self):
        for col in range(game_2048.GAMEBOARD_COL): #iterate thru e/ column in gameboard
            empty_cells = 0 #number of consecutive empty cells
            for col_cell in range(game_2048.GAMEBOARD_ROW): #iterate thru e/ cell in current column
                if self.game_board[col_cell][col] == '':    
                    empty_cells += 1
                elif empty_cells > 0:
                    new_cell = col_cell - empty_cells #calculate new position of current value #might result in negative value

                    current_value = self.game_board[col_cell][col]
                    self.game_board[new_cell][col] = current_value #set new location to current value
                    self.game_board[col_cell][col] = ''            #set old location to empty


    def shift_down(self):
        pass

    def shift_right(self):
        pass

    def shift_left(self):
        pass


gg = game_2048()

gg.run_game()

choice = int(input("1: shift up "))
if choice == 1:
    gg.shift_up()
    gg.print_board()
