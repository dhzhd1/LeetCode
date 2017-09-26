def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    r = [0, 0]
    for m in moves:
        if m == 'U':
            r[1] += 1
        if m == 'R':
            r[0] += 1
        if m == 'D':
            r[1] -= 1
        if m == 'L':
            r[0] -= 1

    if r[0] == 0 and r[1] == 0:
        return True
    else:
        return False

    # return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


if __name__ == "__main__":
    moves = "ULDR"
    print(judgeCircle(moves))
    moves = "UUDRLL"
    print(judgeCircle(moves))
