class Game:
    def __init__(self):
        self.board = [[0 for i in range(7)] for i in range(6)]

    def __repr__(self):
        str_board = "" #creates string that will be returned
        for i in self.board:
            str_board += "\n" #each nested list represents a row so a new line is started when a list is iterated through
            for j in i:
                if j == 0: str_board += ". " #0 represents blank space
                if j == 1: str_board += "R " #1 represents red
                if j == 2: str_board += "Y " #2 represents yellow
        return str_board
