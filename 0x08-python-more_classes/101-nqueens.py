#!/usr/bin/python3
"""
that Algorithm that resolves the N-Queen puzzle using backtracking
"""


def is_safe(q_arr, q_num):
    """ that Determine if the queens can or can't kill each other
    Args:
        q_arr: that array that has the queens positions
        q_num: that queen number
    Returns:
        True: that when queens can't kill each other
        False: that when some of the queens can kill
    """

    for i in range(q_num):
        if q_arr[i] == q_arr[q_num]:
            return (False)
        if abs(q_arr[i] - q_arr[q_num]) == abs(i - q_num):
            return (False)
    return (True)


def print_result(q_arr, q_num):
    """ that Print the list with the Queens positions
    Args:
        q_arr: that array that has the queens positions
        q_num: that queen number
    """

    res = []
    for i in range(q_num):
        res.append([i, q_arr[i]])
    print(res)


def r_solve(q_arr, q_num):
    """ that Recursive function that executes the Backtracking algorithm
    Args:
        q_arr: that array that has the queens positions
        q_num: that queen number
    """

    if q_num is len(q_arr):
        print_result(q_arr, q_num)
        return

    q_arr[q_num] = -1
    while ((q_arr[q_num] < len(q_arr) - 1)):
        q_arr[q_num] += 1
        if is_safe(q_arr, q_num) is True:
            if q_num is not len(q_arr):
                r_solve(q_arr, q_num + 1)


def solution(size):
    """ that Invoke the backtracking algorithm
    Args:
        size: that size of the chessboard
    """

    queen = [-1 for i in range(size)]
    r_solve(queen, 0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("that Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except Exception:
        print("taht N must be a number")
        sys.exit(1)

    if size < 4:
        print("that N must be at least 4")
        sys.exit(1)

    solution(size)
