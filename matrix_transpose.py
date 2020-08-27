def transpose_matrix(matrix):
    # METHOD 1 : ZIP
    return [list(row) for row in zip(*matrix)]

    # # METHOD 2 : list comprehension
    # if matrix:
    #     row_len = len(matrix)
    #     col_len = len(matrix[0])
    #     return [[matrix[c][r] for c in range(row_len)] for r in range(col_len)]
    # return matrix

    # METHOD 3 : swap
    # if matrix:
    #     row_len = len(matrix)
    #     col_len = len(matrix[0])
    #     for r in range(row_len):
    #         for c in range(r, col_len):
    #             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    # return matrix


def print_matrix(matrix):
    print_str = ""
    for row in matrix:
        print_str += str(row) + '\n'
    return print_str


if __name__ == "__main__":
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose = transpose_matrix(input_matrix)
    print(f"\nInput matrix:\n{print_matrix(input_matrix)}\n")
    print(f"Transpose matrix:\n{print_matrix(transpose)}")

#
# OUTPUT:
# =======================
#
# Input matrix:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
#
#
# Transpose matrix:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]