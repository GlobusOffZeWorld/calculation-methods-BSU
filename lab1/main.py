import math
from pprint import pprint
import random
import numpy as np
import time

# VARIANT_NUMBER = 2**(14 / 4)
VARIANT_NUMBER = 11.313708498984761


def fill_matrix(matrix_size: int):

    matrix = [[0] * matrix_size for _ in range(matrix_size)]
    for i in range(matrix_size):
        aii = 0
        for j in range(i + 1, matrix_size):
            is_negative = random.randrange(-1, 2, 2)
            current_number = random.random() * VARIANT_NUMBER * is_negative
            matrix[i][j] = current_number
            matrix[j][i] = current_number
            aii += math.fabs(current_number)
        for j in range(0, i):
            aii += math.fabs(matrix[i][j])
        matrix[i][i] = aii + 1
    return matrix


def fill_vector(vector_size: int):
    vector = []
    for _ in range(vector_size):
        is_negative = random.randrange(-1, 2, 2)
        vector.append([random.random() * VARIANT_NUMBER * is_negative])
    return vector


def matrix_copy(matrix: list):
    return [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]


def print_matrix(matrix: list, matrix_name: str):
    print("Matrix: " + matrix_name + "{")
    for i in matrix:
        for j in i:
            print("{0:10.3f} ".format(j), end="")
        print()
    print("}")


def matrix_dot(matrix_1: list, matrix_2: list):
    final_matrix = []
    for i in range(len(matrix_1)):
        final_matrix.append([])
        for j in range(len(matrix_2[i])):
            temp_sum = 0
            for k in range(len(matrix_1[i])):
                temp_sum += matrix_1[i][k] * matrix_2[k][j]
            final_matrix[i].append(temp_sum)
    return final_matrix


def inverse_matrix_gauss_jordan(matrix: list):
    matrix_size = len(matrix)
    temp_matrix = matrix_copy(matrix)
    inverse_matrix = [[0] * matrix_size for _ in range(matrix_size)]

    for i in range(matrix_size):
        inverse_matrix[i][i] = 1

    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):
            leader_element = temp_matrix[j][i] / temp_matrix[i][i]
            for k in range(0, matrix_size):
                temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
                inverse_matrix[j][k] -= inverse_matrix[i][k] * leader_element

    for i in range(matrix_size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            leader_element = temp_matrix[j][i] / temp_matrix[i][i]
            for k in range(matrix_size - 1, -1, -1):
                temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
                inverse_matrix[j][k] -= inverse_matrix[i][k] * leader_element

    inverse_matrix = [[inverse_matrix[i][j] / temp_matrix[i][i]
                       for j in range(matrix_size)] for i in range(matrix_size)]

    return inverse_matrix


def solve_by_gauss(matrix: list, vector: list):
    matrix_size = len(matrix)
    temp_matrix = matrix_copy(matrix)
    expanded_vector = matrix_copy(vector)

    for i in range(matrix_size):

        column_max = temp_matrix[i][i]
        change_row = i

        for j in range(i, matrix_size):
            if math.fabs(temp_matrix[j][i]) > math.fabs(column_max):
                change_row = j
                column_max = temp_matrix[j][i]

        for j in range(matrix_size):
            temp_matrix[i][j], temp_matrix[change_row][j] = temp_matrix[change_row][j], temp_matrix[i][j]
        expanded_vector[i][0], expanded_vector[change_row][0] = expanded_vector[change_row][0], expanded_vector[i][0]

        for j in range(i + 1, matrix_size):
            leader_element = temp_matrix[j][i] / temp_matrix[i][i]
            expanded_vector[j][0] -= expanded_vector[i][0] * leader_element
            for k in range(0, matrix_size):
                temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
    answer = [[0] for _ in range(matrix_size)]
    for i in range(matrix_size - 1, -1, -1):
        x = expanded_vector[i][0]
        for j in range(matrix_size - 1, i, -1):
            x -= temp_matrix[i][j] * answer[j][0]
        x /= temp_matrix[i][i]
        answer[i] = [x]
    return temp_matrix


def LUP(matrix: list, vector: list):
    matrix_size = len(matrix)
    temp_matrix = matrix_copy(matrix)
    expanded_vector = matrix_copy(vector)
    L = [[0] * matrix_size for _ in range(matrix_size)]
    U = []
    P = [i for i in range(matrix_size)]

    for i in range(matrix_size):
        L[i][i] = 1

    for i in range(matrix_size):
        row_max = temp_matrix[i][i]
        change_column = i
        for j in range(i, matrix_size):
            if math.fabs(temp_matrix[i][j]) > math.fabs(row_max):
                change_column = j
                row_max = temp_matrix[i][j]
        for j in range(matrix_size):
            temp_matrix[j][i], temp_matrix[j][change_column] = temp_matrix[j][change_column], temp_matrix[j][i]
        P[i], P[change_column] = P[change_column], P[i]

        for j in range(i + 1, matrix_size):
            leader_element = temp_matrix[j][i] / temp_matrix[i][i]
            expanded_vector[j][0] -= expanded_vector[i][0] * leader_element
            for k in range(i, matrix_size):
                temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
            L[j][i] = leader_element

    U = matrix_copy(temp_matrix)
    y = [[0] for _ in range(matrix_size)]
    for i in range(matrix_size):
        x = vector[i][0]
        for j in range(i):
            x -= L[i][j] * y[j][0]

        y[i] = [x]

    z = [[0] for _ in range(matrix_size)]
    for i in range(matrix_size - 1, -1, -1):
        x = y[i][0]
        for j in range(matrix_size - 1, i, -1):
            x -= U[i][j] * z[j][0]
        x /= U[i][i]
        z[i] = [x]

    answer = [[0] for _ in range(matrix_size)]

    for i in range(matrix_size):
        answer[P[i]] = z[i]

    return answer


def LDLt(matrix: list, vector: list):
    matrix_size = len(matrix)
    temp_matrix = matrix_copy(matrix)
    L = [[0] * matrix_size for _ in range(matrix_size)]

    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):
            leader_element = temp_matrix[j][i] / temp_matrix[i][i]
            for k in range(i, matrix_size):
                temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
            L[j][i] = leader_element
    D = [[0] * matrix_size for _ in range(matrix_size)]

    for i in range(matrix_size):
        D[i][i] = temp_matrix[i][i]
        for j in range(i):
            D[i][j] = L[i][j]
            D[j][i] = L[i][j]
    return D


def square_root(matrix: list, vector: list):
    matrix_size = len(matrix)
    temp_matrix = matrix_copy(matrix)
    L = [[0] * matrix_size for _ in range(matrix_size)]

    for i in range(matrix_size):
        L[i][i] = 1

    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):
            leader_element = temp_matrix[j][i] / temp_matrix[i][i]
            for k in range(i, matrix_size):
                temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
            L[j][i] = leader_element

    G = [[0] * matrix_size for _ in range(matrix_size)]
    E = [0 for _ in range(matrix_size)]
    for i in range(matrix_size):
        dii = math.sqrt(math.fabs(temp_matrix[i][i]))
        for j in range(i, matrix_size):
            G[i][j] = L[j][i] * dii
            G[j][i] = L[j][i] * dii

        if temp_matrix[i][i] > 0:
            E[i] = 1
        else:
            E[i] = -1

    y = [[0] for _ in range(matrix_size)]
    for i in range(matrix_size):
        x = vector[i][0]
        for j in range(i):
            x -= G[i][j] * y[j][0]
        x /= G[i][i]
        y[i] = [x]

    z = [[0] for _ in range(matrix_size)]
    for i in range(matrix_size):
        z[i] = [E[i] * y[i][0]]

    answer = [[0] for _ in range(matrix_size)]

    for i in range(matrix_size - 1, -1, -1):
        x = z[i][0]
        for j in range(matrix_size - 1, i, -1):
            x -= G[i][j] * answer[j][0]
        x /= G[i][i]
        answer[i] = [x]
    return answer


def relaxation(matrix, vector):
    matrix_size = len(matrix)

    x_current = [[1] for _ in range(matrix_size)]
    w = 1 - 14/40
    eps = 10 ** -15
    x_prev = []
    while True:
        norm = 0
        x_prev = matrix_copy(x_current)
        for i in range(matrix_size):
            sum = vector[i][0]
            for j in range(0, i):
                sum -= matrix[i][j] * x_current[j][0]
            for j in range(i+1, matrix_size):
                sum -= matrix[i][j] * x_prev[j][0]
            sum *= w
            sum /= matrix[i][i]
            sum += (1 - w) * x_prev[i][0]
            x_current[i] = [sum]
            if current_norm := math.fabs(x_current[i][0] - x_prev[i][0]) > norm:
                norm = current_norm
        if norm < eps:
            break
    return x_current


def cubic_norm(matrix: list):
    norm = 0
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += math.fabs(element)
        if row_sum > norm:
            norm = row_sum
    return norm


def matrix_transpose(matrix: list):
    matrix_size = len(matrix)
    temp_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            temp_matrix[i][j] = matrix[j][i]
    return temp_matrix


def main():

    matrix = fill_matrix(256)
    # matrix = [[16.646, 11.159, -0.908, 3.579], [11.159, 29.096, 7.663, 9.274],
    #           [-0.908, 7.663, 19.163, 9.591], [3.579, 9.274, 9.591, 23.444]]
    # matrix = [[6.646, 11.159, -0.908, 3.579], [11.159, 9.096, 7.663, 9.274],
    #           [-0.908, 7.663, 1.163, 9.591], [3.579, 9.274, 9.591, 3.444]]
    vector = fill_vector(256)
    # vector = [[-10.017], [3.737], [-5.090], [3.270]]
    final_vector = matrix_dot(matrix, vector)
    start_time = time.time()
    inverse_matrix = inverse_matrix_gauss_jordan(matrix)
    print(time.time() - start_time)

    # matrix_condition = cubic_norm(matrix) * cubic_norm(inverse_matrix)
    # gauss_solution = solve_by_gauss(matrix, final_vector)
    # lup_solution = LUP(matrix, final_vector)
    # transposed_matrix = matrix_transpose(matrix)
    # print_matrix(matrix, "A")
    # print_matrix(vector, "y")
    # print_matrix(final_vector, "b")
    # print_matrix(inverse_matrix, "Gauss-Jordan")
    # print("Matrix A condition: {0:8.5f}".format(matrix_condition))
    # print_matrix(gauss_solution, "Gauss")
    # print_matrix(lup_solution, "LUP")
    # LDLT_matrix = LDLt(matrix, final_vector)
    # print_matrix(LDLT_matrix, "LDLt")

    # sqare_root = square_root(matrix, final_vector)
    # print_matrix(sqare_root, "square_root")

    # relaxation_solution = relaxation(matrix, final_vector)
    # print_matrix(relaxation_solution, "relaxation")

    # print_matrix(transposed_matrix, "transposed_matrix_A")
    # print_matrix(matrix_dot(matrix, inverse_matrix), "E")


if __name__ == "__main__":
    main()

# 16.646   11.159   -0.908    3.579
# 11.159   29.096    7.663    9.274
# -0.908    7.663   19.163    9.591
# 3.579    9.274    9.591   23.444

# -10.017
# 3.737
# -5.090
# 3.270

# -108.717
# -11.727
# -28.445
# 26.650


#  1.000    0.000    0.000    0.000
#   -0.815    1.000    0.000    0.000
#   -0.687   -0.213    1.000    0.000
#   -0.831   -1.231   -1.347    1.000


# Matrix: G{
#      2.578      0.000      0.000      0.000
#      4.329      3.105      0.000      0.000
#     -0.352     -2.959      3.130      0.000
#      1.388     -1.051      4.215      3.891
# }
# Matrix: y{
#     -3.886
#      6.620
#      4.196
#     -0.529
# }

# Matrix: square_root{
#     -3.886
#     -6.620
#      4.196
#      0.529
# }
