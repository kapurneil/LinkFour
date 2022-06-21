class Game:
    def __init__(self):
        self.board = [[0 for i in range(7)] for i in range(6)] #creates board with 6 rows, 7 columns

    def __repr__(self):
        str_board = ""
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

    def check_winner(self, player, row, column):
        def check_row():
            #checks row piece is dropped to see if connect four has been achieved
            counter = 0
            for col in self.board[int(row)]:
                if col == player:
                    counter += 1
                    if counter >= 4: return True
                else:
                    counter = 0
            return False

        def check_column():
            #checks column piece is dropped to see if connect four has been achieved
            counter = 0
            for iterate_row in range(6):
                if self.board[iterate_row][int(column)] == player:
                    counter += 1
                    if counter >= 4: return True
                else:
                    counter = 0
            return False

        def check_northeast():
            sum = int(row) + int(column) #uses sum of row and column to determine in which northeast diagonals connect 4 is possible
            if (sum > 2 or sum < 9):
                #if piece is on northeast diagonal that can have a connect 4, code checks if it has occurred
                counter = 0
                if sum < 6:
                    for i in range(sum + 1):
                        if self.board[sum-i][i] == player:
                            counter += 1
                            if counter >= 4: return True
                        else:
                            counter = 0
                else:
                    for i in range(12-sum):
                        if self.board[5-i][sum-5+i] == player:
                            counter += 1
                            if counter >= 4: return True
                        else:
                            counter = 0
            return False

        def check_southeast():
            diff = int(row)-int(column)
            abs_diff = abs(diff)
            if (abs_diff < 3) or (abs_diff == 3 and int(column) >= 3):
                counter = 0
                if diff >= 0:
                    for i in range(6-abs_diff):
                        if self.board[diff + i][i] == player:
                            counter += 1
                            if counter >= 4: return True
                        else:
                            counter = 0
                else:
                    for i in range(7-abs_diff):
                        if self.board[i][abs_diff + i] == player:
                            counter += 1
                            if counter >= 4: return True
                        else:
                            counter = 0
            return False

        return (check_row() or check_column() or check_northeast() or check_southeast())

def main():
    #creates game and necessary variables
    game = Game()
    turn_counter = 0
    winner = 0

    #game is played
    while True:
        for player in range(1, 3):
            if turn(game, player):
                winner = player
                break
            turn_counter += 1
        if winner != 0 or turn_counter >= 42: break

    #print out winner
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

def turn(game, player):
    while True:
        column = ask_column(player) - 1
        row = game.drop_piece(player, column)
        if row != -1: break #ends loop if piece can be dropped in specified column/turn is over
        print("ERROR: Column is already full!")
    print(game)
    return game.check_winner(player, row, column)

def ask_column(player):
    while True:
        get_column = input(f"Player {player}, enter column: ")
        try:
            column = int(get_column)
            if column > 0 and column < 8:
                return column
            else:
                print("ERROR: Column number must be 1-7.")
        except ValueError:
            print("ERROR: Column number must be an INTEGER 1-7")

if __name__ == "__main__":
    main()
