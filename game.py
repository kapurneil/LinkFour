class Game:
    def __init__(self):
        self.board = [[0 for i in range(7)] for i in range(6)]

    def __repr__(self):
        str_board = "" #creates string of board that will be returned
        for row in self.board:
            str_board += "\n" #each nested list represents a row so a new line is started when a list is iterated through
            for element in row:
                if element == 0: str_board += ". " #0 represents blank space
                if element == 1: str_board += "R " #1 represents red
                if element == 2: str_board += "Y " #2 represents yellow
        return str_board

    def drop_piece(self, player, column):
        #checks to see if a piece can be dropped in a column.
        #if column is full, -1 is returned, otherwise the row is returned and the board is updated
        row = -1
        for check_row in range(5, -1, -1):
            if self.board[check_row][int(column)] == 0:
                row = check_row
                self.board[row][int(column)] = player #if piece can be dropped, board is updated
                break
        return row #returns row if piece is dropped or -1 if column is full
