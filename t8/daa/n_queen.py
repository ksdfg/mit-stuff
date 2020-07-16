n = 4


def is_safe(result, row, col):
    global n
    if (
        1 in result[row]
        or 1 in map(lambda x: x[col], result[:row])
        or 1 in map(lambda x: result[x[0]][x[1]], zip(range(row - 1, -1, -1), range(col - 1, -1, -1)))
        or 1 in map(lambda x: result[x[0]][x[1]], zip(range(row - 1, -1, -1), range(col + 1, n)))
    ):
        return False
    return True


def _solve(row, result):
    global n
    for col in range(n):
        if is_safe(result, row, col):
            result[row][col] = 1
            if row + 1 < n:
                if _solve(row + 1, result):
                    return True
                result[row][col] = 0
            else:
                return True
    return False


def solve(result):
    _solve(0, result)
    return result


if __name__ == '__main__':
    n = int(input("Enter number of queens : "))
    res = [[0 for _ in range(n)] for _ in range(n)]
    print(*solve(res), sep='\n')
