import math
import random

VARIANT_NUMBER = 2**(14 / 4)


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


def print_matrix(matrix: list, matrix_name: str):
    print("Matrix: " + matrix_name + "{")
    for i in matrix:
        for j in i:
            print("{0:20.16f} ".format(j), end="")
        print()
    print("}")


def multiply_matrix(matrix_1, matrix_2):
    final_vector = []
    for i in range(len(matrix_1)):
        temp_sum = 0
        for j in range(len(matrix_1[0])):
            temp_sum += matrix_1[i][j] * matrix_2[j][0]
        final_vector.append([temp_sum])
    return final_vector


def main():

    matrix = fill_matrix(4)
    print_matrix(matrix, "A")
    vector = fill_vector(4)
    print_matrix(vector, "y")
    final_vector = multiply_matrix(matrix, vector)
    print_matrix(final_vector, "b")

if __name__ == "__main__":
    main()