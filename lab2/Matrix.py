import random
import math
import numpy as np

VARIANT_NUMBER = 2**(14 / 4)

class Matrix:
    def __init__(self) -> None:
        pass

    @staticmethod
    def display(matrix: list, matrix_name: str):
        output = ""
        output += "Matrix: " + matrix_name + "{\n"
        for i in matrix:
            for j in i:
                output += "{0:5.3f} ".format(j)
            output += "\n"
        output += "}"
        return output

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
    def sum(matrix_1: list, matrix_2: list):
        result_matrix = Matrix.copy(matrix_1)
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[i])):
                result_matrix[i][j] += matrix_2[i][j]
        return result_matrix

    @staticmethod
    def scalar_multiply(matrix_1: list, lyamda: list):
        result_matrix = Matrix.copy(matrix_1)
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[i])):
                result_matrix[i][j] *= lyamda
        return result_matrix


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
    def cubic_norm_index(vector: list):
        norm = vector[0][0]
        index = 0
        for i in range(len(vector)):
            if math.fabs(vector[i][0]) > norm:
                norm = vector[i][0]
                index = i
        return index

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

    @staticmethod
    def condition(matrix: list):
        return Matrix.cubic_norm(matrix) * Matrix.cubic_norm(Matrix.inverse(matrix))
    
    @staticmethod
    def vector_difference(vector_1: list, vector_2: list):
        answer = [0 for _ in range(len(vector_1))]
        for i in range(len(vector_1)):
            answer[i] = [vector_1[i][0] - vector_2[i][0]]
        return answer
    @staticmethod
    def write_matrix(matrix: list, filename: str):
        with open(filename, "w") as file:
            text = ""
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    text += str(matrix[i][j]) + " "
            file.write(text)


    @staticmethod
    def scan_matrix(filename: str, matrix_size: int):
        matrix = [[0] * matrix_size for _ in range(matrix_size)]
        with open(filename, "r") as file:
            text = file.read().split(" ")
            for i in range(matrix_size):
                for j in range(matrix_size):
                    matrix[i][j] = float(text[matrix_size * i + j])
        return matrix
    
    @staticmethod 
    def normalize(matrix: list):
        norm = Matrix.cubic_norm(matrix)
        result_matrix = Matrix.copy(matrix)
        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[i])):
                result_matrix[i][j] /= norm
        return result_matrix
        
    @staticmethod
    def max_eigen_value(matrix: list, y0: list, eps: float):
        ITER_COUNT = 100
        first_case = True
        answer_vectors = []
        y = Matrix.dot(matrix, y0)
        answer_vectors.append(y)
        prev_y_norm_index = Matrix.cubic_norm_index(y0)
        lyamda = answer_vectors[0][prev_y_norm_index][0] / y0[prev_y_norm_index][0]

        for i in range(1, ITER_COUNT):
            prev_y_norm_index = Matrix.cubic_norm_index(y)
            y = Matrix.dot(matrix, y)
            answer_vectors.append(y)
            lyamdai = answer_vectors[i][prev_y_norm_index][0] / answer_vectors[i - 1][prev_y_norm_index][0]

            if math.fabs(lyamdai - lyamda) < eps:
                return lyamdai, Matrix.normalize(answer_vectors[i])
            lyamda = lyamdai
        # return lyamda, Matrix.normalize(Matrix.sum(answer_vectors[len(answer_vectors) - 1], Matrix.scalar_multiply(answer_vectors[len(answer_vectors) - 2], lyamdai)))
        
        prev_y_norm_index = Matrix.cubic_norm_index(y0)
        lyamda = math.sqrt(math.fabs(answer_vectors[1][prev_y_norm_index][0] / y0[prev_y_norm_index][0]))

        for i in range(2, len(answer_vectors)):
            prev_y_norm_index = Matrix.cubic_norm_index(answer_vectors[i - 2])
            lyamdai = math.sqrt(math.fabs(answer_vectors[i][prev_y_norm_index][0] / answer_vectors[i - 2][prev_y_norm_index][0]))
            if math.fabs(lyamdai - lyamda) < eps:
                return lyamdai, Matrix.normalize(Matrix.sum(answer_vectors[len(answer_vectors) - 1], Matrix.scalar_multiply(answer_vectors[len(answer_vectors) - 2], lyamdai)))
            lyamda = lyamdai
        
        return lyamda, Matrix.normalize(Matrix.sum(answer_vectors[len(answer_vectors) - 1], Matrix.scalar_multiply(answer_vectors[len(answer_vectors) - 2], lyamdai)))



