def rotate_90(matrix):
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    i = 0
    i_new = 0
    while (i < len(matrix)):
        k = 0
        k_new = len(matrix) - 1
        while (k < len(matrix)):
            new_matrix[k_new][i_new] = matrix[i][k]
            k_new -= 1
            k += 1
        i_new += 1
        i += 1
    return new_matrix

def in_place_rotate_90(matrix):
    y = 0
    while y < len(matrix)/2:
        x = y
        while x < len(matrix) - 1 - y:
            top = matrix[y][x]
            left = matrix[len(matrix)-1-x][y]
            bottom = matrix[len(matrix)-1-y][len(matrix)-1-x]
            right = matrix[x][len(matrix)-1-y]

            tmp = top
            matrix[y][x] = right
            matrix[x][len(matrix)-1-y] = bottom
            matrix[len(matrix)-1-y][len(matrix)-1-x] = left
            matrix[len(matrix)-1-x][y] = tmp
            x += 1
        y += 1

    return matrix
