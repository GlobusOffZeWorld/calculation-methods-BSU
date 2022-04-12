import time
import math
import pprint
from Matrix import *
from SolveMethods import *

# VARIANT_NUMBER = 11.313708498984761


def time_to_run(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time


def main():

    # A = Matrix.fill(4)
    # A =
    A = [[0.646, 11.159, -0.908, 3.579], [11.159, 29.096, 7.663, 9.274],
              [-0.908, 7.663, 19.163, 9.591], [3.579, 9.274, 9.591, 23.444]]
    # y = [[6.646, 11.159, -0.908, 3.579], [11.159, 9.096, 7.663, 9.274],
    #           [-0.908, 7.663, 1.163, 9.591], [3.579, 9.274, 9.591, 3.444]]
    y = Matrix.fill_vector(4)
    # vector = [[-10.017], [3.737], [-5.090], [3.270]]
    b = Matrix.dot(A, y)
    # with open("output.txt", "w") as file:
    #     file.write()

    print(Matrix.display(A, "A"))
    print(Matrix.display(y, "y"))
    print(Matrix.display(b, "b"))
    for matrix in SolveMethods.LUP(A):
        print(Matrix.display(matrix, ""))
    print(Matrix.display(SolveMethods.solve_LUP(SolveMethods.LUP(A), b), "SolveLUP"))

    # A_matrix_list = [Matrix.fill(256) for _ in range(100)]
    # b_matrix_list = [Matrix.fill_vector(256) for _ in range(100)]

    max_condition_index = 0
    # max_condition_index = A_matrix_list[0]
    max_condition_value = -1
    min_condition_value = math.inf

    average_time_inverse = 0
    average_time_gauss = 0
    average_time_LUP = 0
    average_time_LUP_solution = 0
    average_time_square_root = 0
    average_time_relaxation= 0

    # for i in range(len(A_matrix_list)):
    #     cond = Matrix.condition(A_matrix_list[i])
    #     if cond > max_condition_value:
    #         max_condition_value = cond
    #         max_condition_index = i
    #     elif cond < min_condition_value:
    #         min_condition_value = cond

    #     average_time_inverse += time_to_run(Matrix.inverse, A)
    # with open("max_condition_matrix.txt", "w") as file:
    #     file.write(Matrix.display(A_matrix_list[max_condition_index], "A"))

    # task8_1 = "------------\nmax_condition_value: {0:10.6f}\nmin_condition_value: {1:10.6f}\n------------".format(
    #     max_condition_value, min_condition_value)
    # task8_2 = """------------\naverage time to inverse matrix: {0:10.6f}\n------------""".format(
    #     average_time_inverse / len(A_matrix_list))
    # with open("answers.txt", "w") as file:
    #     file.write(task8_1)
    #     file.write(task8_2)

    # print("max_condition_value: {0:10.6f}".format(max_condition_value))
    # print("min_condition_value: {0:10.6f}".format(min_condition_value))
    # print("min_condition_matrix: {0:10.6f}".format(
    #     Matrix.condition(A_matrix_list[max_condition_index])))
    # print("function execution time: {0:10.6f}".format(time_to_run(SolveMethods.gauss, A, b)))
if __name__ == "__main__":
    main()
