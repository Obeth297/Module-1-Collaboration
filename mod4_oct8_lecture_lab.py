from random import randrange


def display_board(board):
    """Displays the current state of the board."""
    print("+-------+-------+-------+")
    for row in range(3):
        for _ in range(1):  # Print empty rows
            print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        for _ in range(1):  # Print empty rows
            print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    """Prompts the user for a move and updates the board."""
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            row, col = divmod(move - 1, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("That square is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def make_list_of_free_fields(board):
    """Returns a list of free squares on the board."""
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False


def draw_move(board):
    """The computer makes a random move on the board."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'


def main():
    # Initialize the board
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Computer makes the first move
    board[1][1] = 'X'  # Computer puts 'X' in the middle
    display_board(board)

    while True:
        # Check for victory conditions
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        elif victory_for(board, 'O'):
            print("You win!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        # User's turn
        enter_move(board)
        display_board(board)

        # Check for victory conditions again
        if victory_for(board, 'O'):
            print("You win!")
            break

        # Computer's turn
        draw_move(board)
        display_board(board)


if __name__ == "__main__":
    main()