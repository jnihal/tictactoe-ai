"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import numpy
from random import shuffle


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X and O
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)

    # Player X's turn if the counts are equal else player O's turn
    if X_count == O_count:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize an empty action set
    actions = list()

    # If the cell is empty, add it to the set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    shuffle(actions)
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Invalid action
    if board[i][j] != EMPTY:
        raise NameError('Not a valid action')
    
    # Create a copy of the board
    board_copy = deepcopy(board)

    # Return the modified board
    board_copy[i][j] = player(board_copy)
    return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]
    
    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]

    # Check columns
    board = numpy.transpose(board)
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

    return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if someone has won the game
    if winner(board) != None:
        return True
    
    # Check if the board is complete
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:    
            return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        return maxValue(board)[1]
    elif player(board) == O:
        return minValue(board)[1]
        
    raise NotImplementedError


# Helper functions
# Maximize the value
def maxValue(board):
    v = -math.inf

    if terminal(board):
        return utility(board), -1
    
    # Find the action that produces the maximum value
    for action in actions(board):
        v0 = minValue(result(board, action))[0]
        if v0 > v:
            v, a = v0, action
        if v == 1:
            break
    return v, a


# Minimize the value
def minValue(board):
    v = math.inf

    if terminal(board):
        return utility(board), -1
        
    # Find the action that produces the minimum value
    for action in actions(board):
        v0 = maxValue(result(board, action))[0]
        if v0 < v:
            v, a = v0, action
        if v == -1:
            break    
    return v, a