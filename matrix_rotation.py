
def matrix_rotate_90(matrix):
    """
    Rotates n*n matrix by 90 degree
    :param matrix: input matrix
    :return:
    """
    if not matrix:
        return matrix

    row_len = len(matrix)
    col_len = len(matrix[0])

    # Step 1: Transpose matrix
    for r in range(row_len):
        for c in range(r, col_len):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # step 2: Reverse the columns
    for r in range(col_len):
        for c in range(row_len//2):
            matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]

    return matrix


def print_matrix(matrix):
    print_str = ""
    for row in matrix:
        print_str += str(row) + '\n'
    return print_str


if __name__ == "__main__":

    input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(f"\nInput matrix:\n{print_matrix(input_matrix)}\n")
    matrix_rotate_90(input_matrix)
    print(f"Rotated matrix:\n{print_matrix(input_matrix)}")


# OUTPUT:
# ================
#
# Input matrix:
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]
# [13, 14, 15, 16]
#
#
# Rotated matrix:
# [13, 9, 5, 1]
# [14, 10, 6, 2]
# [15, 11, 7, 3]
# [16, 12, 8, 4]
