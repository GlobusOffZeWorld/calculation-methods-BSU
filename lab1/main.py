import math
import random
import time

VARIANT_NUMBER = 2**(14 / 4)
# VARIANT_NUMBER = 11.313708498984761


class Matrix:
    def __init__(self) -> None:
        pass

    @staticmethod
    def display(matrix: list, matrix_name: str):
        print("Matrix: " + matrix_name + "{")
        for i in matrix:
            for j in i:
                print("{0:10.3f} ".format(j), end="")
            print()
        print("}")

    @staticmethod
    def transpose(matrix: list):
        matrix_size = len(matrix)
        temp_matrix = [[0] * matrix_size for _ in range(matrix_size)]
        for i in range(matrix_size):
            for j in range(matrix_size):
                temp_matrix[i][j] = matrix[j][i]
        return temp_matrix

    @staticmethod
    def copy(matrix: list):
        return [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]

    @staticmethod
    def dot(matrix_1: list, matrix_2: list):
        final_matrix = []
        for i in range(len(matrix_1)):
            final_matrix.append([])
            for j in range(len(matrix_2[i])):
                temp_sum = 0
                for k in range(len(matrix_1[i])):
                    temp_sum += matrix_1[i][k] * matrix_2[k][j]
                final_matrix[i].append(temp_sum)
        return final_matrix

    @staticmethod
    def cubic_norm(matrix: list):
        norm = 0
        for row in matrix:
            row_sum = 0
            for element in row:
                row_sum += math.fabs(element)
            if row_sum > norm:
                norm = row_sum
        return norm

    @staticmethod
    def fill(matrix_size: int):
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

    @staticmethod
    def fill_vector(vector_size: int):
        vector = []
        for _ in range(vector_size):
            is_negative = random.randrange(-1, 2, 2)
            vector.append([random.random() * VARIANT_NUMBER * is_negative])
        return vector

    @staticmethod
    def inverse(matrix: list):
        matrix_size = len(matrix)
        temp_matrix = Matrix.copy(matrix)
        inverse_matrix = [[0] * matrix_size for _ in range(matrix_size)]

        for i in range(matrix_size):
            inverse_matrix[i][i] = 1

        for i in range(matrix_size):
            for j in range(i + 1, matrix_size):
                leader_element = temp_matrix[j][i] / temp_matrix[i][i]
                for k in range(0, matrix_size):
                    temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
                    inverse_matrix[j][k] -= inverse_matrix[i][k] * \
                        leader_element

        for i in range(matrix_size - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                leader_element = temp_matrix[j][i] / temp_matrix[i][i]
                for k in range(matrix_size - 1, -1, -1):
                    temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
                    inverse_matrix[j][k] -= inverse_matrix[i][k] * \
                        leader_element

        inverse_matrix = [[inverse_matrix[i][j] / temp_matrix[i][i]
                           for j in range(matrix_size)] for i in range(matrix_size)]

        return inverse_matrix


class SolveMethods:
    def __init__(self) -> None:
        pass

    @staticmethod
    def gauss(matrix: list, vector: list):
        matrix_size = len(matrix)
        temp_matrix = Matrix.copy(matrix)
        expanded_vector = Matrix.copy(vector)

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
        x_current = [[0] for _ in range(matrix_size)]
        for i in range(matrix_size - 1, -1, -1):
            x = expanded_vector[i][0]
            for j in range(matrix_size - 1, i, -1):
                x -= temp_matrix[i][j] * x_current[j][0]
            x /= temp_matrix[i][i]
            x_current[i] = [x]
        return x_current

    @staticmethod
    def LUP(matrix: list, vector: list):
        matrix_size = len(matrix)
        temp_matrix = Matrix.copy(matrix)
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
                for k in range(i, matrix_size):
                    temp_matrix[j][k] -= temp_matrix[i][k] * leader_element
                L[j][i] = leader_element

        U = Matrix.copy(temp_matrix)
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

        x_current = [[0] for _ in range(matrix_size)]

        for i in range(matrix_size):
            x_current[P[i]] = z[i]

        return x_current

    @staticmethod
    def LDLt(matrix: list, vector: list):
        matrix_size = len(matrix)
        temp_matrix = Matrix.copy(matrix)
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

    @staticmethod
    def square_method(matrix: list, vector: list):
        matrix_size = len(matrix)
        temp_matrix = Matrix.copy(matrix)
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

        x_current = [[0] for _ in range(matrix_size)]

        for i in range(matrix_size - 1, -1, -1):
            x = z[i][0]
            for j in range(matrix_size - 1, i, -1):
                x -= G[i][j] * x_current[j][0]
            x /= G[i][i]
            x_current[i] = [x]
        return x_current

    @staticmethod
    def relaxation(matrix, vector):
        matrix_size = len(matrix)
        x_current = [[1] for _ in range(matrix_size)]
        w = 1 - 14/40
        eps = 10 ** -15
        x_prev = []
        while True:
            norm = 0
            x_prev = Matrix.copy(x_current)
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


def main():

    A = Matrix.fill(4)
    # matrix = [[16.646, 11.159, -0.908, 3.579], [11.159, 29.096, 7.663, 9.274],
    #           [-0.908, 7.663, 19.163, 9.591], [3.579, 9.274, 9.591, 23.444]]
    # matrix = [[6.646, 11.159, -0.908, 3.579], [11.159, 9.096, 7.663, 9.274],
    #           [-0.908, 7.663, 1.163, 9.591], [3.579, 9.274, 9.591, 3.444]]
    y = Matrix.fill_vector(4)
    # vector = [[-10.017], [3.737], [-5.090], [3.270]]
    b = Matrix.dot(A, y)
    Matrix.display(b, "b")


if __name__ == "__main__":
    main()
