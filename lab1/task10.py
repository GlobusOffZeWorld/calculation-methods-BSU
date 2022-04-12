from cProfile import label
from service import *



def task_solution():
    n = 14

    A1 = Matrix.scan_matrix("doc/max_condition_matrix.txt", 256)
    y1 = Matrix.fill_vector(256)
    b1 = Matrix.dot(A1, y1)

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
    

    A1_LUP = SolveMethods.LUP(A1)
    A2_LUP = SolveMethods.LUP(A2)

    A1_LUP_solution = SolveMethods.solve_LUP(A1_LUP, b1)
    A2_LUP_solution = SolveMethods.solve_LUP(A2_LUP, b2)


    A1_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A1_LUP_solution, y1))/Matrix.cubic_norm(y1)
    A2_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A2_LUP_solution, y2))/Matrix.cubic_norm(y2)

    task10_1 = """------------------------------------
    relative difference norm A1(started) by LUP {0:.3e}
    relative difference norm A2(started) by LUP {1:.3e}
    ------------------------------------""".format(A1_norm_difference, A2_norm_difference)

    for i in range(len(b1)):
        b1[i][0] +=0.0001
        
    for i in range(len(b2)):
        b2[i][0] +=0.0001

    A1_LUP_solution = SolveMethods.solve_LUP(A1_LUP, b1)
    A2_LUP_solution = SolveMethods.solve_LUP(A2_LUP, b2)


    A1_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A1_LUP_solution, y1))/Matrix.cubic_norm(y1)
    A2_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A2_LUP_solution, y2))/Matrix.cubic_norm(y2)

    task10_2 = """------------------------------------
    relative difference norm A1 with b1 += 0.0001 by LUP {0:.3e}
    relative difference norm A2 with b2 += 0.0001 by LUP {1:.3e}
    ------------------------------------""".format(A1_norm_difference, A2_norm_difference)
    
    for i in range(len(b1)):
        b1[i][0] *=1.00001
        
    for i in range(len(b2)):
        b2[i][0] *=1.00001

    A1_LUP_solution = SolveMethods.solve_LUP(A1_LUP, b1)
    A2_LUP_solution = SolveMethods.solve_LUP(A2_LUP, b2)


    A1_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A1_LUP_solution, y1))/Matrix.cubic_norm(y1)
    A2_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A2_LUP_solution, y2))/Matrix.cubic_norm(y2)

    task10_3 = """------------------------------------
    relative difference norm A1 with b1 *=1.00001 by LUP {0:.3e}
    relative difference norm A2 with b2 *=1.00001 by LUP {1:.3e}
    ------------------------------------""".format(A1_norm_difference, A2_norm_difference)

    

    for i in range(len(b1)):
        b1[i][0] +=156
        
    for i in range(len(b2)):
        b2[i][0] +=156

    A1_LUP_solution = SolveMethods.solve_LUP(A1_LUP, b1)
    A2_LUP_solution = SolveMethods.solve_LUP(A2_LUP, b2)

    A1_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A1_LUP_solution, y1))/Matrix.cubic_norm(y1)
    A2_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(A2_LUP_solution, y2))/Matrix.cubic_norm(y2)

    task10_4 = """------------------------------------
    relative difference norm A1 with b1 += 100 by LUP {0:.3e}
    relative difference norm A2 with b1 += 100 by LUP {1:.3e}
    ------------------------------------""".format(A1_norm_difference, A2_norm_difference)

    b1 = Matrix.dot(A1, y1)
    b2 = Matrix.dot(A2, y2)

    A1_x_current1, A1_iter_count1, A1_iteration_values1 = SolveMethods.relaxation(A1, b1, 0.8)
    A1_x_current2, A1_iter_count2, A1_iteration_values2 = SolveMethods.relaxation(A1, b1, 1)
    A1_x_current3, A1_iter_count3, A1_iteration_values3 = SolveMethods.relaxation(A1, b1, 1.2)

    A1_norm1 = []
    for i in range(len(A1_iteration_values1)):
        A1_norm1.append(Matrix.cubic_norm(Matrix.vector_difference(A1_iteration_values1[i], y1)))
    A1_norm2 = []
    for i in range(len(A1_iteration_values2)):
        A1_norm2.append(Matrix.cubic_norm(Matrix.vector_difference(A1_iteration_values2[i], y1)))
    A1_norm3 = []
    for i in range(len(A1_iteration_values3)):
        A1_norm3.append(Matrix.cubic_norm(Matrix.vector_difference(A1_iteration_values3[i], y1)))

    A2_x_current1, A2_iter_count1, A2_iteration_values1 = SolveMethods.relaxation(A2, b2, 0.8)
    A2_x_current2, A2_iter_count2, A2_iteration_values2 = SolveMethods.relaxation(A2, b2, 1)
    A2_x_current3, A2_iter_count3, A2_iteration_values3 = SolveMethods.relaxation(A2, b2, 1.2)

    A2_norm1 = []
    for i in range(len(A2_iteration_values1)):
        A2_norm1.append(Matrix.cubic_norm(Matrix.vector_difference(A2_iteration_values1[i], y2)))
    A2_norm2 = []
    for i in range(len(A2_iteration_values2)):
        A2_norm2.append(Matrix.cubic_norm(Matrix.vector_difference(A2_iteration_values2[i], y2)))
    A2_norm3 = []
    for i in range(len(A2_iteration_values3)):
        A2_norm3.append(Matrix.cubic_norm(Matrix.vector_difference(A2_iteration_values3[i], y2)))
    
    
    plt.loglog(A1_norm1, label="w = 0.8")
    plt.loglog(A1_norm2, label="w = 1.0")
    plt.loglog(A1_norm3, label="w = 1.2")
    plt.xlabel("Iterations count")
    plt.ylabel("error")
    plt.legend()
    plt.title("matrix with max condition number from task 8")
    plt.show()

    plt.loglog(A2_norm1, label="w = 0.8")
    plt.loglog(A2_norm2, label="w = 1.0")
    plt.loglog(A2_norm3, label="w = 1.2")
    plt.xlabel("Iterations count")
    plt.ylabel("error")
    plt.legend()
    plt.title("A2 matrix")
    plt.show()

    with open("doc/task10.txt", "w") as file:
        file.write(task10_1)
        file.write(task10_2)
        file.write(task10_3)
        file.write(task10_4)