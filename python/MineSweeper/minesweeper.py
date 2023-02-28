import random
import re
#play the game


class Board:
    def __init__(self, dim_size, num_bombs):
        #let's keep track of these parameters. They will be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # lets create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()


        # initialize a set to keep track of which locations weve oncovered
        # well save (row,col) tuples into this set
        self.dug = set() #if we dig at 0,0 then self.dug = {[0,0]}

    

    
        
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # this creates an array like this:
        # [[None, None, ..., None ],
        #  [None, None, ..., None ],
        #   [...                  ],
        #  [None, None, * None ]],
        # we can see how this represents a board!

        
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            print(self.dim_size**2 -1)
            loc = random.randint(0,self.dim_size**2 -1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size # we want the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size # we want the remainder to tell us what index in that row to loop

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*'
            bombs_planted += 1
        print(board)
        return board


    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    #if this is already a bomb, we dont want to clculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size - 1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size - 1, col+1) + 1):
                if r == row and c == col:
                    # our original location, dont check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row , col):
        # dig at that location!
        # Return True if sucessfull dig, False if bomb dig

        # a few scenarios:
        # hit a bomb = game over
        # dig at location with neigboring bombs = finish dig
        # dig at location with no neighnoring bombs = recursively dig neighbors 

        self.dug.add((row,col)) #keep track that we dug

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0,row-1), min(self.dim_size -1, row+1) + 1):
            for c in range(max(0,col-1), min(self.dim_size - 1, col+1) + 1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)

        #if our initial dig didnt hit a bomb, we *shouldnt* hit a bomb here
        return True
            
    def __str__(self):
        #this is a magic funtuon where id youy call print on this object,
        # it'll print out what this funtion returns!
        # return a string that shows the board to the player

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep






def play(dim_size=10, num_bombs=10):
    #Step 1 : create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    

    #Step 2 : show the user the board and ask for where they want to dig




    #Step 3a: if location is a bomb, show game over message
    #Step 3b : if location is not a omb, dog recursively until each square is at least next to a bomb
    #Step 4 : repeat step 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split( ',(\\s)*',input("Hello! Where would you like to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid Location. Try again")
            continue

        # if its a valid location, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhh
            break # (game over)

    if safe:
        print("CONGRATULATIONS!!! YOU HAVE WON THE GAME")
    else:
        print("You have died. Game Over...")
        # lets reveal the whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
