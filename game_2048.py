from enum import Enum
import random 

class board_2048:
    GAMEBOARD_ROW = 4
    GAMEBOARD_COL = 4

    def __init__(self): #sets an uninitialized state for game
        self.board_degrees = 0 #degree of rotation of board
        self.game_board = [['', '', '', ''], #empty cells represented by empty strings.
                           ['', '', '', ''], 
                           ['', '', '', ''],
                           ['', '', '', '']]

        self.empty_locations = {(0,0):(0,0), (0,1):(0,1), (0,2):(0,2), (0,3):(0,3), #empty locations are removed when value is inserted
                                (1,0):(1,0), (1,1):(1,1), (1,2):(1,2), (1,3):(1,3), #randomly chosen locations will always be empty
                                (2,0):(2,0), (2,1):(2,1), (2,2):(2,2), (2,3):(2,3), #may change value to tile value at that location
                                (3,0):(3,0), (3,1):(3,1), (3,2):(3,2), (3,3):(3,3)}

        self.value_locations = dict() #when location is filled its removed from empty_locations and place here
        self.recent_value = 0 #value that was most recently doubled when converging values

    def print_board(self):
        row_line = "{:->34}".format("\n")  # len of row line is 33. set to 34 to accommadate newline esc seq
        board = []                         # esc seq is right aligned

        for i in range(board_2048.GAMEBOARD_ROW): #iterate thru each row in board
            grid_row = "{}|{:^7}|{:^7}|{:^7}|{:^7}|".format(row_line, *self.game_board[i]) #use string format to insert row_line and four game_board values
            board.append(grid_row)                                                         # use unpack operator to unpack each row in game_board

        board.append(row_line)  # append last row_line onto bottom of board
        board = "\n".join(board)
        print(board)

    def check_matchingNeighbors(self): #check each cell's right/bottom neighbor for matching values
        for row in range(self.GAMEBOARD_ROW): 
            for col in range(self.GAMEBOARD_COL - 1): #does not check last column bc that is a special case
                current_value = self.game_board[row][col]
                try: #when checking cells in last col, checking the right neighbor will throw error and skip check for matching bottom neighbor
                    if current_value == self.game_board[row][col+1] or current_value == self.game_board[row+1][col]: #check bottom and right values for match
                        return True
                except IndexError:
                    continue

        for row in range(self.GAMEBOARD_ROW - 1): #handle last column as special case
            current_value = self.game_board[row][-1]
            if current_value == self.game_board[row+1][-1]: #check current value's bottom neighbor
                return True

        return False

    def place_item(self, num):
        keylist = list(self.empty_locations.keys())
        index = random.randint(0, len(keylist)-1) #pick random index from list of keys

        key = keylist[index] #stores random key
        location = self.empty_locations.pop(key)  #prevents selecting a location that is fileld when randomly choosing a key

        self.value_locations[key] = location
        self.game_board[location[0]][location[1]] = num

    def shift_values(self):
        for col in range(game_2048.GAMEBOARD_COL): #iterate thru e/ column in gameboard
            empty_space_count = 0 #number of empty spaces in column
            prev_value = None
            prev_cell = None
            for current_cell in range(game_2048.GAMEBOARD_ROW): #iterate thru e/ cell in current column
                current_value = self.game_board[current_cell][col]

                if current_value == '': #if board lcoation is empty add 1 to empty space count
                    empty_space_count += 1

                else:
                    if current_value == prev_value:
                        self.game_board[current_cell][col] = '' #remove current value from gameboard
                        empty_space_count += 1

                        current_value *= 2
                        self.game_board[prev_cell][col] = current_value #store double current_value at prev_value's location
                        self.recent_value = current_value
                        prev_cell = None  #for any converging value only 2 values may converge at a time
                        prev_value = None 

                    elif empty_space_count > 0:
                        new_cell = current_cell - empty_space_count #shift current value based on num of empty spaces
                        self.game_board[new_cell][col] = current_value #set new location to current value
                        self.game_board[current_cell][col] = ''        #set old location to empty
                        prev_cell = new_cell
                        prev_value = current_value
                    else: #if current value not match prev_value and 0 empty spaces -> update prev_cell and prev_value
                        prev_cell = current_cell
                        prev_value = current_value

    

    def rotate_board(self, degree):
        degree_rotated = 0
        rotated_board = self.game_board

        if degree > 0: #for positive degrees: transpose then reverse
            while degree_rotated != degree:
                transpose_board = list(zip(*rotated_board))
                rotated_board = [row[::-1] for row in transpose_board]
                degree_rotated += 90

        elif degree < 0: #for negative degrees: reverse then rotate
            while degree_rotated != degree:
                reverse_board = [row[::-1] for row in rotated_board]
                rotated_board = list(zip(*reverse_board))
                degree_rotated -= 90

        self.game_board = [list(row) for row in rotated_board]
        self.board_degrees = degree



    def update_location(self): #dont like this method but will have to stick with it for now... :(
        """
        after shifting we un-rotate to board to its normal position at 0 degrees. The coordinates of any changed cells
        in the gameboard will now be relative to the board at 0 degrees. This method iterates thru the board and updated the
        un-rotated coordinates of each cell in either empty_locations or value_locations
        """
        self.empty_locations = dict()
        self.value_locations = dict()

        for row in range(self.GAMEBOARD_ROW):
            for col in range(self.GAMEBOARD_COL):
                coord = (row, col)
                if self.game_board[row][col] == '':
                    self.empty_locations[coord] = coord
                else:
                    self.value_locations[coord] = coord

    def shift_direction(self, degrees):
        self.rotate_board(degrees)
        self.shift_values()
        self.rotate_board(-degrees)
        self.update_location()

    def shift_up(self):
        degrees = 0
        self.shift_direction(degrees)

    def shift_left(self):
        degrees = 90
        self.shift_direction(degrees)

    def shift_down(self):
        degrees = 180
        self.shift_direction(degrees)

    def shift_right(self):
        degrees = -90
        self.shift_direction(degrees)


class GAME_STATUS(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    WIN = 2
    LOSE = 3

class game_2048:

    GAMEBOARD_ROW = 4
    GAMEBOARD_COL = 4

    def __init__(self): #sets an uninitialized state for game
       
        self.game_state = GAME_STATUS.NOT_STARTED
        

    def init_game(self):
        self.game_state = GAME_STATUS.IN_PROGRESS

        # randomly place 2 tiles
        start_values = [2,4]
        start_value1, start_value2 = random.choices(start_values, weights=[3,1],k=2) #make weighted random choice between 2 and 4.  
        # return list of two randomly chosen values where 2 has higher weight.
        self.place_item(start_value1)
        self.place_item(start_value2)

    def print_game_menu(self):
        options = ["W - UP", "A - LEFT", "S - DOWN", "D - RIGHT"]
        print(" | ".join(options))


    def check_game_status(self):
        if self.recent_value == 2048:
            self.game_state = GAME_STATUS.WIN
        elif len(self.empty_locations) == 0 and not self.check_matchingNeighbors():
            self.game_state = GAME_STATUS.LOSE

    def run_game(self):
        self.init_game()

        while self.game_state == GAME_STATUS.IN_PROGRESS:
            self.print_board()
            self.print_game_menu()
            choice = input("Choice: ").lower()
            old_value_locations = self.value_locations #store copy of value locations on board before shifting values

            match choice:
                case "w":
                    self.shift_up()
                case 'a':
                    self.shift_left()
                case 's':
                    self.shift_down()
                case 'd':
                    self.shift_right()
                case _:
                    print("ERROR: Invalid choice")
                    continue

            if self.value_locations != old_value_locations:#only place new item if value locations have changed after picking a shift direction
                self.place_item(random.choice([2,4]))
            self.check_game_status()

        self.print_board()

        if self.game_state == GAME_STATUS.WIN:
            print("You Reached 2048! Congrats!")
        elif self.game_state == GAME_STATUS.LOSE:
            print("You are outta moves! Try Again!")


 

    