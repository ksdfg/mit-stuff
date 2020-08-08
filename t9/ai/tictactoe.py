from random import choice
from typing import List


class Board:
    winning_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def __init__(self, board: List[str] = None):
        """
        Initialize the object with list of all values
        :param board: List of all the values
        """
        if board is None:
            self.board = ['-' for _ in range(9)]
        else:
            self.board = board

    def __str__(self):
        """
        represent the board object as a string so that we can print it easily
        :return: string representation of the object
        """
        return "\n".join(" ".join(map(str, self.board[i * 3 : i * 3 + 3])) for i in range(3))

    def __setitem__(self, position: int, player: str):
        """
        make a player's move onto the board
        :param position:
        :param player:
        """
        self.board[position] = player

    def check_game_over(self):
        """
        Check if the game is over or there is a winner
        :return: True if the game is over, else false
        """
        return '-' not in [element for element in self.board] or self.winner() != '-'

    def available_moves(self):
        """
        To check what all possible moves are remaining for a player
        :return: List of all the indices which represent available spaces that player can occupy
        """
        return [index for index, element in enumerate(self.board) if element == '-']

    def available_combos(self, player: str):
        """
        To check what are the possible places to play for winning the game
        :param player: 'X' or 'O'
        :return:
        """
        return self.available_moves() + self.get_acquired_places(player)

    def winner(self):
        """
        Checks for the winner of the game
        :return player: return 'X' or 'O' whoever has won the game else returns '-'
        """
        for player in ('X', 'O'):
            positions = self.get_acquired_places(player)

            for combo in self.winning_combos:
                for pos in combo:
                    if pos not in positions:
                        break
                else:
                    return player

        return '-'

    def get_acquired_places(self, player: str):
        """
        To get the positions already acquired by a particular player
        :param player: 'X' or 'O'
        """
        return [index for index, element in enumerate(self.board) if element == player]

    def minimax(self, node, player: str):
        """
        Minimax algorithm for choosing the best possible move towards winning the game
        :param node: Board object which represents the current state of the board
        :param player: 'X' or 'O'
        :return: best value for next move
        """
        if node.check_game_over():
            winner = node.winner()
            if winner == 'X':
                return -1
            elif winner == '-' and node.check_game_over():
                return 0
            elif winner == 'O':
                return 1

        enemy = 'O' if player == 'X' else 'X'
        best = 0

        for move in node.available_moves():
            node[move] = player
            val = self.minimax(node, enemy)
            node[move] = '-'

            if player == 'O':
                if val > best:
                    best = val
            else:
                if val < best:
                    best = val

        return best


def determine(board: Board, player: str):
    """
    Driver function to apply minimax algorithm
    :param board: Board object that represents current state of the board
    :param player: 'X' or 'O'
    :return: Best choice according to minimax algorithm
    """
    a = 0
    choices = []
    enemy = 'O' if player == 'X' else 'X'

    for move in board.available_moves():
        board[move] = player
        val = board.minimax(board, enemy)
        board[move] = '-'

        if player == 'O' and val > a or player == 'X' and val < a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)

    try:
        return choice(choices)
    except IndexError:
        return choice(board.available_moves())


if __name__ == "__main__":
    # create the initial empty board object
    board = Board()

    player = '-'
    while player not in ('X', 'O'):
        player = input("Select `X` or `O` : ")
    computer = 'O' if player == 'X' else 'X'
    print()  # just for neatness

    while not board.check_game_over():
        print("The board positions are as follows :")
        print("\n".join([" ".join(map(str, [i, i + 1, i + 2])) for i in range(0, 9, 3)]))

        player_move = int(input("\nYour Move: "))
        if player_move not in board.available_moves():
            print('Please check the input!\n')
            continue

        board[player_move] = player
        print(board)
        if board.check_game_over():
            print()  # just for neatness
            break

        computer_move = determine(board, player)
        print("\nComputer's move :", computer_move)
        board[computer_move] = computer
        print(board)

        print()  # just for neatness

    if board.winner() != '-':
        if board.winner() == player:
            print("You win!")
        else:
            print('Computer Wins!')
    else:
        print("Game tied!")
