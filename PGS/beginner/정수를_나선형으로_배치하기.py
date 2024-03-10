# [0][0] → [0][1] → [0][2] → [0][3]
#                             ↓  ↓
# [1][0] → [1][1] → [1][2]   [1][3]
#  ↑  ↑              ↓  ↓     ↓  ↓
# [2][0]   [2][1] ← [2][2]   [2][3]
#  ↑  ↑                       ↓  ↓
# [3][0] ← [3][1] ← [3][2] ← [3][3]

def solution(n):
    array = [[0] * n for _ in range(n)]

    count = 1

    startRow = 0
    endRow = n - 1
    startCol = 0
    endCol = n - 1

    while count <= n * n:
        for i in range(startCol, endCol + 1):
            array[startRow][i] = count
            count += 1
        startRow += 1

        for i in range(startRow, endCol + 1):
            array[i][endCol] = count
            count += 1
        endCol -= 1

        for i in range(endCol, startCol - 1, -1):
            array[endRow][i] = count
            count += 1
        endRow -= 1

        for i in range(endRow, startRow - 1, -1):
            array[i][startCol] = count
            count += 1
        startCol += 1

    return array
