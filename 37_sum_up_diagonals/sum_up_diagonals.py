def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    side = len(matrix)
    sum_diagonal_TLBR = 0
    sum_diagonal_BLTR = 0
    for idx in range(side):
        sum_diagonal_TLBR += matrix[idx][idx]
        sum_diagonal_BLTR += matrix[side - 1 - idx][idx]
    return sum_diagonal_TLBR + sum_diagonal_BLTR