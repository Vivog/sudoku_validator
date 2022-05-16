etalon: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def valid_solution(board):
    if chk_zero(board) and chk_rows(board) and chk_column(board) and chk_3x3(board, 0, 3, 0, 3):
        return True
    else:
        return False


# Check ZERO
def chk_zero(arr):
    for i in arr:
        for j in i:
            if j == 0:
                return False
    return True


# Chek rows
def chk_rows(arr):
    for i in arr:
        for j in etalon:
            if j not in i:
                return False
    return True


# Check columns
def chk_column(arr):
    arr_column = [[]]
    for i in range(0, 9):
        for j in range(0, 9):
            arr_column[i].append(arr[j][i])
        if i != 8:
            arr_column.append(list())
    for i in arr_column:
        for j in etalon:
            if j not in i:
                return False
    return True


# Check 3x3
def chk_3x3(arr, x, y, a, b):
    arr_3x3 = [[]]
    for i in range(0, 9):
        for j in range(x, y):
            for k in range(a, b):
                arr_3x3[i].append(arr[j][k])
        x += 3
        y += 3
        if y > 9:
            x = 0
            y = 3
            a += 3
            b += 3
        if b > 9:
            break
        arr_3x3.append(list())
    for i in arr_3x3:
        for j in etalon:
            if j not in i:
                return False
    return True


# Checking solution

print(valid_solution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]))
