import time
from Matrix import Matrix
from SolveMethods import SolveMethods
import task8
import task9
import matplotlib.pyplot as plt
import seaborn as sns
VARIANT_NUMBER = 2**(14 / 4)


def time_to_run(func, *args):
    start_time = time.time()
    x = func(*args)
    return (time.time() - start_time, x)


class MinAvgMax:
    def __init__(self, min, avg, max):
        self.min = min
        self.avg = avg
        self.max = max


def main():
    # task8.task_solution()
    # task9.task_solution()

    n = 14

    A2_ = [[1, 1+n, 2+n, 3+n, 4+n, 5+n, 6+n, 7+n],
           [100*n, 1000*n, 10000*n, 100000*n, -1000*n, -10000*n, -100000*n, 1],
           [n, -1+n, -2+n, -3+n, -4+n, -5+n, -6+n, -7+n],
           [n-1000, 10*n-1000, 100*n-1000, 1000*n -
               1000, 10000*n-1000, -n, -n+1, -n+2],
           [-2*n, 0, -1, -2, -3, -4, -5, -6],
           [n-2019, -n+2020, n-2021, -n+2022, n-2023, -n+2024, n-2025, -n+2026],
           [2*n-2000, 4*n-2005, 8*n-2010, 16*n-2015,
               32*n-2020, 2019*n, -2020*n, 2021*n],
           [1020-2*n, -2924+896*n, 1212+9808*n, -2736 + 98918*n, 1404 - 11068*n, -1523-8078*n, 2625 - 102119*n, -1327 + 1924*n]]
    A2 = Matrix.dot(Matrix.transpose(A2_), A2_)

    y2 = Matrix.fill_vector(8)
    b2 = Matrix.dot(A2, y2)



    max_condition_matrix = Matrix.scan_matrix("max_condition_matrix.txt", 256)


if __name__ == "__main__":
    main()
