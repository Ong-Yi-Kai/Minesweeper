from MineSweeperBoard import Board


def get_board_dimensions():
    """
    Ask for user input for board dimensions and num_bombs
    :return: dim_size [int], num_bombs[int]
    """
    while True:
        try:
            dim_size = int(input("Length of board [int]: ").strip())
            if dim_size <= 1:
                raise ValueError
            break
        except:
            print("Please input a positive integer that is more than 1")

    while True:
        try:
            num_bombs = int(input("Number of bombs [int]: ").strip())
            if num_bombs <= 0 or num_bombs >= dim_size ** 2:
                raise ValueError
            break
        except:
            print("Please input a positive integer that is more than 0 and less than num_dim**2")

    return dim_size, num_bombs

def play():
    dim_size, num_bombs = get_board_dimensions()
    board = Board(dim_size, num_bombs)

    in_game = True
    while in_game:
        # show the board
        print("=="*50, "\n", board)
        try:
            r_str, c_str = input("Position to dig [r,c]: ").split(',')
            r,c = int(r_str.strip()), int(c_str.strip())
            for val in [r,c]:
                if val < 0 or val >= board.dim_size:
                    print(f"Value need to be more than 0 and less than {board.dim_size}, you placed {val}")
        except:
            print("Error occured, try again")

        in_game = board.dig(r,c)

        if len(board.dug) == board.dim_size**2 - num_bombs:
            board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
            break


    if in_game:
        print("Congratz! You WON!!!")
    else:
        print("Sorry. You lost")




if __name__ == "__main__":
    play()


