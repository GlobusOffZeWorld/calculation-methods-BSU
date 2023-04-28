from service import *
import numpy as np


def func(x: float):
    return (((np.power(x, 9) + np.pi) * np.cos(np.log(np.power(x, 2) + 1))) / (np.power(np.e, np.power(x, 2))) - (x) / 2022)


def dfunc(x: float):
    return (-(2 * np.power(np.e, -np.power(x, 2)) * (np.power(x, 9) + np.pi) * x * np.sin((np.log(np.power(x, 2) + 1)))) / (np.power(x, 2) + 1) - 2 * np.power(np.e, -np.power(x, 2)) * (np.power(x, 9) + np.pi) * np.cos((np.log(np.power(x, 2) + 1))) + 9 * (np.power(np.e, -np.power(x, 2)) * np.power(x, 8) * np.cos(np.log(np.power(x, 2) + 1))) - 1/2022)


def bisection(f, left: float, right: float, eps: float):
    while np.abs(right - left) > eps:
        inverse = False
        if f(left) < 0:
            inverse = True
        x = (right + left) / 2
        if (f(x) > 0):
            if inverse:
                right = x
            else:
                left = x
        else:
            if inverse:
                left = x
            else:
                right = x
    return left

def newton(x: float, f, df, eps: float):
    result = x + eps + 1 
    while np.abs(result - x) > eps:
        result = x
        x -= f(x) / df(x)
    return result


def main():
    matrix_A1 = [
        [1, -2, 1, 0, -1, 1, -2, 2, 0, -2],
        [0, 2, 0, 0, 2, 1, -1, -1, -1, -2],
        [0, 1, 0, -1, 1, -1, 0, -1, 1, -1],
        [-2, -1, 2, -1, 0, 0, 0, 0, 1, 0],
        [1, -2, 0, 1, 0, -2, -1, 0, 2, 2],
        [-2, -2, 0, -2, 0, 1, 1, -2, 1, 1],
        [-1, -2, -1, -1, -2, -1, -2, 1, -1, 2],
        [-2, 1, 2, -2, 0, 2, 1, -1, -2, 2],
        [0, 1, 0, 1, 1, -2, 2, 0, 1, 1],
        [0, 0, 2, -1, -1, 0, -2, 2, -1, -1]]
    matrix_A2 = [
        [-1, 1, -1, 0, -1, 0, -1, 1, 1, -1, 0, -1, -1, 1, 0, 0, 1, 1, 1, 1],
        [-1, 0, -1, 1, -1, 0, 0, 0, 0, -1, 0, 0, -1, 1, 0, -1, 1, -1, -1, 0],
        [1, 0, -1, 1, 0, 1, -1, -1, -1, 0, -1, -1, 1, -1, 1, 1, -1, 1, -1, 0],
        [-1, 1, 0, 0, -1, 0, 0, -1, 0, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 0],
        [1, 0, -1, 0, 0, -1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, -1, 0, 0, 1],
        [0, 0, 0, 0, -1, 1, 1, 0, 0, 1, 1, 0, -1, 0, 1, 1, 0, 1, 0, 0],
        [-1, 0, 1, 1, 1, -1, -1, 0, -1, 1, -1, -1, -1, 0, -1, 0, 0, 0, -1, 1],
        [0, 0, -1, -1, 0, 1, 1, 1, 1, -1, 0, 0, -1, 1, 1, 1, 1, 0, 0, -1],
        [0, 0, 1, 1, 0, 1, 1, 0, 1, -1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, -1, 0, 0, 1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 1, -1, 0, 0, 1, 1],
        [1, -1, 1, -1, -1, -1, 1, 0, -1, 0, 1, 1, -1, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, -1, 0, 1, 0, 1, 0, 0, 1, 1, -1, -1, 0, -1, 1, 1, -1],
        [-1, -1, -1, -1, 0, 1, -1, 0, 0, -1, 0, 0, 0, 1, 1, 0, 0, 0, -1, 0],
        [-1, 0, 1, 0, -1, 0, 0, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 0],
        [1, -1, 0, -1, -1, 0, -1, -1, 0, 0, 1, 0, 1, 1, -1, 1, 0, 0, -1, 0],
        [-1, -1, 1, 0, -1, 1, 1, -1, 1, 0, 0, -1, 1, -1, -1, 0, 0, 1, 1, 1],
        [0, 0, -1, 0, 0, 0, 0, -1, 1, 1, 0, -1, 1, -1, 0, 0, 0, -1, -1, 1],
        [-1, 0, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 0, -1, 0, -1],
        [-1, 0, 1, 0, 0, 0, 0, -1, 1, -1, 1, -1, 0, -1, -1, 1, 0, 1, 0, 0],
        [0, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 0, -1, -1, 0, 1, 0, -1, -1]
    ]

    y01 = [
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1]
    ]
    y02 = [
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1]
    ]
   
    eigen_value, eigen_vector = Matrix.max_eigen_value(matrix_A1, y01, 0.00001)
    print("A1 max eigen value",eigen_value)
    print(Matrix.display(eigen_vector, "A1 eigen vector"))

    eigen_value, eigen_vector = Matrix.max_eigen_value(matrix_A2, y02, 0.00001)
    print("A2 max eigen value", eigen_value)
    print(Matrix.display(eigen_vector, "A2 eigen vector"))

    # bisection_answer = bisection(func,0, 2,1e-4)
    # print(bisection_answer)
    # print(newton(bisection_answer, func, dfunc, 1e-14))



if __name__ == "__main__":
    main()
