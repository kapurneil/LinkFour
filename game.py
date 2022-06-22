class Game:
    def __init__(self):
        self.board = [[0 for element in range(7)] for row in range(6)] #creates board with 6 rows, 7 columns

    def __repr__(self):
        str_board = ""
        for row in self.board:
            str_board += "\n" #each nested list represents a row so a new line is started when a list is iterated through
            for element in row:
                if element == 0: str_board += ". " #0 represents blank space
                if element == 1: str_board += "R " #1 represents red
                if element == 2: str_board += "Y " #2 represents yellow
        return str_board

    def drop_piece(self, player: int, column: int, row: int):
        #method updates board when piece is dropped
        self.board[int(row)][int(column)] = player

    def get_next_available_row(self, column: int) -> int:
        #method returns first available row (from bottom to top) in a certain column
        for check_row in range(5, -1, -1): #goes from bottom row to top
            if self.board[check_row][column] == 0:
                return check_row #returns first available row in column if column is not full
        return -1 #returns -1 if column is full

    def has_winner(self, player: int, row: int, column: int) -> bool:
        #method checks if a connect 4 has been achieved and returns a boolean
        #row and column represent the location where the piece was dropped
        def check_row() -> bool:
            counter = 1
            #check to left
            for check_column in range(column-1, -1, -1):
                if self.board[row][check_column] != player: break
                counter +=1

            #check to right
            for check_column in range(column+1, 7, 1):
                if self.board[row][check_column] != player: break
                counter += 1

            return counter >= 4

        def check_column() -> bool:
            counter = 1
            #check upwards
            for check_row in range(row-1, -1, -1):
                if self.board[check_row][column] != player: break
                counter += 1

            #check downwards
            for check_row in range(row+1, 6, 1):
                if self.board[check_row][column] != player: break
                counter += 1

            return counter >= 4

        def check_northeast_diagonal() -> bool:
            #check if piece is on a northeast diagonal with at least 4 spaces using sum
            sum = row + column
            if sum < 3 or sum > 8: return False #NE diagonal does not have 4 spaces

            counter = 1
            #check upwards
            check_row = row - 1; check_column = column + 1
            while check_row > -1 and check_column < 7:
                if self.board[check_row][check_column] != player: break
                counter += 1; check_row -= 1; check_column += 1

            #check downwards
            check_row = row + 1; check_column = column - 1
            while check_row < 6 and check_column > -1:
                if self.board[check_row][check_column] != player: break
                counter += 1; check_row += 1; check_column -= 1

            return counter >= 4

        def check_southeast_diagonal() -> bool:
            #check if piece is on a southeast diagonal with at least 4 spaces using difference
            diff = row - column
            if diff < -3 or diff > 2: return False #SE diagonal does not have 4 spaces

            counter = 1
            #check upwards
            check_row = row - 1; check_column = column - 1
            while check_row > -1 and check_column > - 1:
                if self.board[check_row][check_column] != player: break
                counter += 1; check_row -= 1; check_column -= 1

            #check downwards
            check_row = row + 1; check_column = column + 1
            while check_row < 6 and check_column < 7:
                if self.board[check_row][check_column] != player: break
                counter += 1; check_row += 1; check_column += 1

            return counter >= 4

            #check each possible scenario and return true if four in a row has occurred
        return check_row() or check_column() or check_northeast_diagonal() or check_southeast_diagonal()
#end of game class

@staticmethod
def main():
    #creates game and necessary variables
    game = Game()
    turn_counter = 0
    winner = 0

    #game is played
    while winner == 0 and turn_counter < 42:
        for player in range(1, 3):
            row = -1
            while row == -1:
                get_column = ask_column(player)
                column = int(get_column)
                row = game.get_next_available_row(column)
                if row == -1: print("ERROR: Column is full.")
            game.drop_piece(player, column, row)
            print(game)
            if game.has_winner(player, row, column):
                winner = player
                break
            turn_counter += 1

    #prints out winner/results
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

@staticmethod
def ask_column(player: int) -> int:
    #function asks user which column they want to drop connect 4 piece in and returns the column as an integer
    while True:
        get_column = input(f"Player {player}, enter column: ")
        try:
            column = int(get_column)
            if column > 0 and column < 8:
                return column - 1
            else:
                print("ERROR: Column number must be 1-7.")
        except ValueError:
            print("ERROR: Column number must be an INTEGER 1-7")

if __name__ == "__main__":
    main()
