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
                                (1,0):(1,0), (1,1):(1,1), (1,2):(1,2), (1,3):(1,3), #randomly chosen locations will always be empty
                                (2,0):(2,0), (2,1):(2,1), (2,2):(2,2), (2,3):(2,3), #may change value to tile value at that location
                                (3,0):(3,0), (3,1):(3,1), (3,2):(3,2), (3,3):(3,3)}

        self.occupied_locations = dict() #when location is filled its removed from empty_locations and place here
        # might remove
    def init_game(self):
        # randomly place 2 tiles
        start_values = [2,4]
        start_value1, start_value2 = random.choices(start_values, weights=[3,1],k=2) #make weighted random choice between 2 and 4.  
        # return list of two randomly chosen values where 2 has higher weight.
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

    def shift_values(self):
        for col in range(game_2048.GAMEBOARD_COL): #iterate thru e/ column in gameboard
            emptySpace_count = 0 #number of empty spaces in column
            prev_value = None
            prev_cell = None
            for current_cell in range(game_2048.GAMEBOARD_ROW): #iterate thru e/ cell in current column
                current_value = self.game_board[current_cell][col]

                if prev_value == current_value:
                    self.game_board[current_cell][col] = '' #remove current value
                    emptySpace_count += 1

                    prev_value *= 2
                    self.game_board[prev_cell][col] = prev_value 

                elif current_value == '':  #if board location is empty add 1 to empty space
                    emptySpace_count += 1

                else:
                    new_cell = current_cell - emptySpace_count  # MIGHT RESULT IN NEGATIVE VALUE

                    if new_cell != current_cell: #ensures values on end of board are not removed
                        self.game_board[new_cell][col] = current_value #set new location to current value
                        self.game_board[current_cell][col] = ''        #set old location to empty

                        # update cell availability
                        self.empty_locations[(current_cell, col)] = self.occupied_locations.pop((current_cell, col))
                        self.occupied_locations[(new_cell, col)] = self.empty_locations.pop((new_cell, col))

                    prev_value = current_value
                    prev_cell = new_cell

    def shift_up(self):
        self.shift_values()

    def shift_left(self):
        self.rotate_board(90)
        self.shift_values()
        self.rotate_board(-90)

    def shift_down(self):
        degrees = 180

    def shift_right(self):
        degrees = -90

    def rotate_board(self, degree):
        degree_rotated = 0
        rotated_board = self.game_board

        if degree > 0:
            while degree_rotated != degree:
                transpose_board = list(zip(*rotated_board))
                rotated_board = [row[::-1] for row in transpose_board]
                degree_rotated += 90

        elif degree < 0:
            while degree_rotated != degree:
                reverse_board = [row[::-1] for row in rotated_board]
                rotated_board = list(zip(*reverse_board))
                degree_rotated -= 90

        self.game_board = [list(row) for row in rotated_board]
