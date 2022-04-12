import time
import math
import pprint
from Matrix import *
from SolveMethods import *

# VARIANT_NUMBER = 11.313708498984761


def time_to_run(func, *args):
    start_time = time.time()
    x = func(*args)
    return (time.time() - start_time, x)


def vector_difference(vector_1: list, vector_2: list):
    answer = [0 for _ in range(len(vector_1))]
    for i in range(len(vector_1)):
        answer[i] = [vector_1[i][0] - vector_2[i][0]]
    return answer


class MinAvgMax:
    def __init__(self, min, avg, max):
        self.min = min
        self.avg = avg
        self.max = max


def main():

    # A = Matrix.fill(4)
    # A =
    # A = [[0.646, 11.159, -0.908, 3.579], [11.159, 29.096, 7.663, 9.274],
    #           [-0.908, 7.663, 19.163, 9.591], [3.579, 9.274, 9.591, 23.444]]
    # y = [[6.646, 11.159, -0.908, 3.579], [11.159, 9.096, 7.663, 9.274],
    #           [-0.908, 7.663, 1.163, 9.591], [3.579, 9.274, 9.591, 3.444]]
    # y = Matrix.fill_vector(4)
    # vector = [[-10.017], [3.737], [-5.090], [3.270]]
    # print(Matrix.cubic_norm(vector))
    # b = Matrix.dot(A, y)
    # with open("output.txt", "w") as file:
    #     file.write()

    # print(Matrix.display(A, "A"))
    # print(Matrix.display(y, "y"))
    # print(Matrix.display(b, "b"))
    # print(Matrix.display(SolveMethods.solve_LUP(SolveMethods.LUP(A), b), "SolveLUP"))
    MATRIX_SIZE = 25
    MATRIX_COUNT = 100
    A_matrix_list = [Matrix.fill(MATRIX_SIZE) for _ in range(MATRIX_COUNT)]
    y_matrix_list = [Matrix.fill_vector(MATRIX_SIZE)
                     for _ in range(MATRIX_COUNT)]
    b_matrix_list = [Matrix.dot(A_matrix_list[i], y_matrix_list[i])
                     for i in range(MATRIX_COUNT)]

    max_condition_index = 0
    max_condition_value = -1
    min_condition_value = math.inf

    full_time_inverse = 0

    full_time_gauss = 0
    gauss_difference = MinAvgMax(math.inf, 0, 0)

    full_time_LUP = 0
    full_time_LUP_solution = 0
    LUP_solution_difference = MinAvgMax(math.inf, 0, 0)

    full_time_square_root = 0
    square_root_difference = MinAvgMax(math.inf, 0, 0)

    full_time_relaxation = 0
    relaxation_difference = MinAvgMax(math.inf, 0, 0)
    relaxation_iter_count = MinAvgMax(math.inf, 0, 0)

    for i in range(MATRIX_COUNT):
        cond = Matrix.condition(A_matrix_list[i])
        if cond > max_condition_value:
            max_condition_value = cond
            max_condition_index = i
        elif cond < min_condition_value:
            min_condition_value = cond
        ttr_inverse, x_inverse = time_to_run(Matrix.inverse, A_matrix_list[i])
        full_time_inverse += ttr_inverse

        ttr_gauss, x_gauss = time_to_run(
            SolveMethods.gauss, A_matrix_list[i], b_matrix_list[i])
        full_time_gauss += ttr_gauss

        temp1 = Matrix.cubic_norm(vector_difference(x_gauss, y_matrix_list[i]))
        gauss_difference.avg += temp1
        if temp1 > gauss_difference.max:
            gauss_difference.max = temp1
        elif temp1 < gauss_difference.min:
            gauss_difference.min = temp1

        ttr_LUP, x_LUP = time_to_run(SolveMethods.LUP, A_matrix_list[i])
        full_time_LUP += ttr_LUP

        ttr_LUP_solution, x_LUP_solution = time_to_run(
            SolveMethods.solve_LUP, x_LUP, b_matrix_list[i])
        full_time_LUP_solution += ttr_LUP_solution

        temp2 = Matrix.cubic_norm(vector_difference(
            x_LUP_solution, y_matrix_list[i]))
        LUP_solution_difference.avg += temp2
        if temp2 > LUP_solution_difference.max:
            LUP_solution_difference.max = temp2
        elif temp2 < LUP_solution_difference.min:
            LUP_solution_difference.min = temp2

        ttr_square_root, x_square_root = time_to_run(
            SolveMethods.square_method, A_matrix_list[i], b_matrix_list[i])
        full_time_square_root += ttr_square_root

        temp3 = Matrix.cubic_norm(vector_difference(
            x_square_root, y_matrix_list[i]))
        square_root_difference.avg += temp3
        if temp3 > square_root_difference.max:
            square_root_difference.max = temp3
        elif temp3 < square_root_difference.min:
            square_root_difference.min = temp3

        ttr_relaxation, (x_relaxation, iter_count) = time_to_run(
            SolveMethods.relaxation, A_matrix_list[i], b_matrix_list[i])
        full_time_relaxation += ttr_relaxation

        temp4 = Matrix.cubic_norm(vector_difference(
            x_relaxation, y_matrix_list[i]))
        relaxation_difference.avg += temp4
        if temp4 > relaxation_difference.max:
            relaxation_difference.max = temp4
        elif temp4 < relaxation_difference.min:
            relaxation_difference.min = temp4

        relaxation_iter_count.avg += iter_count
        if iter_count > relaxation_iter_count.max:
            relaxation_iter_count.max = iter_count
        elif iter_count < relaxation_iter_count.min:
            relaxation_iter_count.min = iter_count

    with open("max_condition_matrix.txt", "w") as file:
        file.write(Matrix.display(A_matrix_list[max_condition_index], "A"))

    task8_1 = """------------------
    max_condition_value: {0:10.6f}
    min_condition_value: {1:10.6f}
    ------------------""".format(
        max_condition_value, min_condition_value)

    task8_2 = """------------------
    average time to inverse matrix: {0:10.6f}
    ------------------""".format(
        full_time_inverse / MATRIX_COUNT)
    
    task8_3 = """------------------
    min difference norm to solve by gauss: {0:.3e}
    avg difference norm to solve by gauss: {1:.3e}
    max difference norm to solve by gauss: {2:.3e}\n
    min difference norm to solve by LUP_solution: {3:.3e}
    avg difference norm to solve by LUP_solution: {4:.3e}
    max difference norm to solve by LUP_solution: {5:.3e}\n
    min difference norm to solve by square_root: {6:.3e}
    avg difference norm to solve by square_root: {7:.3e}
    max difference norm to solve by square_root: {8:.3e}\n
    min difference norm to solve by relaxation: {9:.3e}
    avg difference norm to solve by relaxation: {10:.3e}
    max difference norm to solve by relaxation: {11:.3e}
    ------------------""".format(gauss_difference.min,
                           gauss_difference.avg / MATRIX_COUNT,
                           gauss_difference.max,
                           LUP_solution_difference.min,
                           LUP_solution_difference.avg / MATRIX_COUNT,
                           LUP_solution_difference.max,
                           square_root_difference.min,
                           square_root_difference.avg / MATRIX_COUNT,
                           square_root_difference.max,
                           relaxation_difference.min,
                           relaxation_difference.avg / MATRIX_COUNT,
                           relaxation_difference.max)

    task8_4 = """------------------
    average time to solve by gauss: {0:10.6f}
    ------------------""".format(
        full_time_gauss / MATRIX_COUNT)

    task8_5 = """------------------
    average time to find LUP: {0:10.6f}
    ------------------""".format(
        full_time_LUP / MATRIX_COUNT)

    task8_6 = """------------------
    average time to solve by LUPx = b: {0:10.6f}
    ------------------""".format(
        full_time_LUP_solution / MATRIX_COUNT)

    task8_7 = """------------------
    average time to solve by relaxation: {0:10.6f}
    ------------------""".format(
        full_time_relaxation / MATRIX_COUNT)

    task8_8 = """------------------
    min iter_count to solve by relaxation: {0:10.6f}
    avg iter_count to solve by relaxation: {1:10.6f}
    max iter_count to solve by relaxation: {2:10.6f}
    ------------------""".format(relaxation_iter_count.min,
                           relaxation_iter_count.avg / MATRIX_COUNT,
                           relaxation_iter_count.max)
    with open("answers.txt", "w") as file:
        file.write(task8_1)
        file.write(task8_2)
        file.write(task8_3)
        file.write(task8_4)
        file.write(task8_5)
        file.write(task8_6)
        file.write(task8_7)
        file.write(task8_8)

    # print("max_condition_value: {0:10.6f}".format(max_condition_value))
    # print("min_condition_value: {0:10.6f}".format(min_condition_value))
    # print("min_condition_matrix: {0:10.6f}".format(
    #     Matrix.condition(A_matrix_list[max_condition_index])))
    # print("function execution time: {0:10.6f}".format(time_to_run(SolveMethods.gauss, A, b)))
if __name__ == "__main__":
    main()
