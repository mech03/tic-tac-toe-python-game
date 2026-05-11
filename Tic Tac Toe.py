# we need random so the computer can pick a spot
import random

# global counters - these live outside the functions
# so every function can see and update them
player1_wins   = 0
player2_wins   = 0
draws          = 0
player1_streak = 0
player2_streak = 0


def print_board(board):
    """
    This just prints the board out as a grid.
    I pass in the board list and it uses the
    index of each spot to show X, O or empty.
    """
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, marker):
    """
    This checks if someone has won the game.
    There are 8 ways to win - 3 rows, 3 columns
    and 2 diagonals. I store them all in a list
    of lists then loop through each one to see
    if all 3 spots match the marker (X or O).
    Returns True if there is a winner, False if not.
    """
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == marker:
            return True
    return False

def print_stats(name1, name2):
    """
    This prints the current scores and win streaks.
    I pass in the player names so it shows their
    actual names instead of just player 1 and player 2.
    """
    print("--- Stats ---")
    print(name1 + " wins: " + str(player1_wins) + "  (streak: " + str(player1_streak) + ")")
    print(name2 + " wins: " + str(player2_wins) + "  (streak: " + str(player2_streak) + ")")
    print("Draws: " + str(draws))
    print()


def computer_move(board):
    """
    This is for when the computer plays.
    It loops through the board, collects all
    the empty spots into a list, then picks
    one at random using random.choice().
    """
    empty_spots = []
    for i in range(9):
        if board[i] == " ":
            empty_spots.append(i)
    return random.choice(empty_spots)


def play_game():
    """
    This is the main function that runs the whole game.
    The outer while loop keeps the game going so
    players can play again after each round.
    The inner while loop runs one single game.
    I use global so the counters outside the function
    can be updated from inside here.
    """
    global player1_wins, player2_wins, draws, player1_streak, player2_streak

    print("Welcome to Tic Tac Toe!")
    print()

    # ask which mode they want to play
    print("Game modes:")
    print("1 - Two players")
    print("2 - vs Computer")
    print()

        # keep asking until they give a valid mode
    while True:
        try:
            mode = int(input("Pick a mode (1 or 2): "))
            if mode == 1 or mode == 2:
                break
            else:
                print("Please pick 1 or 2")
        except ValueError:
            print("Please enter a number!")

    # ask for player names
    name1 = input("Player 1, what is your name? ")
    if mode == 1:
        name2 = input("Player 2, what is your name? ")
    else:
        name2 = "Computer"

    print()
    print("Welcome " + name1 + " and " + name2 + "!")
    print()

    # show the position numbers so players know what to pick
    print("Here are the board positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()

    # outer loop - keeps going so players can play again
    while True:

        # reset the board for a new game
        # board is just a list of 9 empty spaces
        board  = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        turn   = name1
        marker = "X"

        print_board(board)

        # inner loop - one single game
        while True:

            # if its the computers turn it picks a random empty spot
            if turn == name2 and mode == 2:
                print(name2 + " is thinking...")
                index = computer_move(board)
                board[index] = marker
                print_board(board)

            else:
                # get the players input
                # try/except catches letters or symbols
                try:
                    move = int(input(turn + " (" + marker + ") pick a spot (1-9): "))
                except ValueError:
                    print("Please enter a number!")
                    continue

                # check the number is between 1 and 9
                if move < 1 or move > 9:
                    print("Pick a number between 1 and 9")
                    continue

                # list indexes start at 0 so we minus 1
                index = move - 1

                # check the spot is not already taken
                if board[index] != " ":
                    print("That spot is taken, try again!")
                    continue

                # place the marker and show the board
                board[index] = marker
                print_board(board)

            # check if that move won the game
            if check_winner(board, marker):
                print(turn + " wins!")
                # update the winners score and streak
                # reset the other players streak
                if turn == name1:
                    player1_wins   = player1_wins + 1
                    player1_streak = player1_streak + 1
                    player2_streak = 0
                else:
                    player2_wins   = player2_wins + 1
                    player2_streak = player2_streak + 1
                    player1_streak = 0
                print_stats(name1, name2)
                break

            # check for a draw
            # if there are no spaces left its a draw
            if " " not in board:
                print("Its a draw!")
                draws          = draws + 1
                player1_streak = 0
                player2_streak = 0
                print_stats(name1, name2)
                break

            # switch to the other player
            if turn == name1:
                turn   = name2
                marker = "O"
            else:
                turn   = name1
                marker = "X"

            # ask if they want to play again
            # keep asking until they say yes or no
        while True:
            again = input("Play again? (yes/no): ")
            if again == "yes" or again == "no":
                break
            else:
                print("Please type yes or no!")

        if again == "no":
            print("Thanks for playing!")
            print_stats(name1, name2)
            break


# start the game
play_game()
