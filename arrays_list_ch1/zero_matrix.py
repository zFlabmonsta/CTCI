# Iterating through each cell and finding 0 and changing the row and col of cell will
# eventual make the whole matrix 0

# O(N^2) Space Complexity
# O(N^3) Time Complexity
def zero_matrix (matrix):
    zero_m = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_m[i][j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if zero_m[i][j] == 0:
                k = 0
                while (k < len(matrix)):
                    matrix[k][j] = 0
                    k += 1

                k = 0
                while (k < len(matrix[0])):
                    matrix[i][k] = 0
                    k += 1

    return matrix

# We can reduce the space complexity to O(N)
# by keeping track of which row or col needs to be zero-ed
# O(N^2)
def zero_matrix_1(matrix):
    row = set()
    col = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                col.add(j)
                row.add(i)

    for r in row:
        i = 0
        while i < len(matrix[0]):
            matrix[r][i] = 0
            i += 1

    for c in col:
        i = 0
        while i < len(matrix):
            matrix[i][c] = 0
            i += 1

    return matrix
















