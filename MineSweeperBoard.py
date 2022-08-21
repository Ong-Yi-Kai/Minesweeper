import random


class Board():
    """
    Represents the board of a minesweeper game

    Instance attributes:
        dim_size: [int] length of board
        num_bombs: [int] number of bombs. num_bombs < dim_size**2
        board: List[List[str/int]] each position is either None, 'B', or an int indicating num bombs around
        dug: set of tuples indicating the positions we hae dug
    """

    def __init__(self, dim_size, num_bombs):
        """
        Init obj attributes
        """
        assert type(dim_size) == int
        assert type(num_bombs) == int
        assert num_bombs < dim_size**2, f"num_bombs needs to be less than dim_size**2, you have {num_bombs}"

        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.create_new_board()

        self.dug = set()
        self.show_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

    def create_new_board(self):
        """
        returns a board List[List[str/int]] of dim_size with num_bombs bombs
        """

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # insert bombs
        planted_bombs = 0
        while planted_bombs < self.num_bombs:
            idx = random.randint(0,self.dim_size**2-1)
            row, col = idx // self.dim_size, idx % self.dim_size

            if board[row][col] == "B":
                continue

            board[row][col] = "B"
            planted_bombs += 1

        # insert the number
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "B":
                    continue
                board[r][c] = self.get_num_surrounding_bombs(r,c,board)
        return board

    def get_num_surrounding_bombs(self,r,c,board):
        """
        Returns the number of surrounding bombs at position r,c
        """
        bomb_count = 0
        for i in range(max(0,r-1),min(self.dim_size,r+2)):
            for j in range(max(0, c - 1), min(self.dim_size, c+2)):
                if i == r and j == c:
                    continue
                elif board[i][j] == "B":
                    bomb_count += 1

        return bomb_count

    def dig(self, r, c):
        """
        Returns whether a dig is succesful

        True -> doesn't hit a bomb
        False -> hits a bomb

        param r: [int] row idx to dig
        param c: [int] col idx to dig
        """
        self.dug.add((r,c))

        if self.board[r][c] == "B":
            return False
        elif self.board[r][c] > 0:
            return True

        for i in range(max(0,r-1),min(self.dim_size-1,r+2)):
            for j in range(max(0, c - 1), min(self.dim_size-1, c + 2)):
                if (i,j) in self.dug:
                    continue
                self.dig(i,j)

        return True

    def __repr__(self):
        """
        Returns the string representation of the board
        """
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
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
                    max(columns, key=len)
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
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep








