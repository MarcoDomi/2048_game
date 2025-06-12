def print_board():
    '''
    ---------------------------------
    |       |       |       |       |
    ---------------------------------
    |       |       |       |       |
    ---------------------------------
    |       |       |       |       |
    ---------------------------------
    |       |       |       |       |
    ---------------------------------
    '''

    row_line = "{:->34}".format("\n") #len of row line is 33. set to 34 to accomadate newline esc seq
    grid_cell = "|{:^7}".format("")


    grid_row = f"{row_line}{grid_cell}{grid_cell}{grid_cell}{grid_cell}|\n"

    board = f"{grid_row}{grid_row}{grid_row}{grid_row}{row_line}"
    print(board)


    

    
print_board()
