from Matrix import Matrix
from SolveMethods import SolveMethods

def task_solution():
    n = 14

    A1 = [[n**2 + 15, n-1, -1, -2],
          [n-1, -15-n**2, -n+4, -4],
          [-1, -n+4, n**2+8, -n],
          [-2, -4, -n, n**2+10]]
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

    y1 = Matrix.fill_vector(4)
    y2 = Matrix.fill_vector(8)

    b1 = Matrix.dot(A1, y1)
    b2 = Matrix.dot(A2, y2)

    A1_cond = Matrix.condition(A1)
    A2_cond = Matrix.condition(A2)

    x1_gauss = SolveMethods.gauss(A1, b1)
    x2_gauss = SolveMethods.gauss(A2, b2)

    A1_LUP = SolveMethods.LUP(A1)
    A2_LUP = SolveMethods.LUP(A2)

    x1_LUP_solution = SolveMethods.solve_LUP(A1_LUP, b1)
    x2_LUP_solution = SolveMethods.solve_LUP(A2_LUP, b2)

    x1_square_root = SolveMethods.square_method(A1, b1)
    x2_square_root = SolveMethods.square_method(A2, b2)

    A1_LDLt = SolveMethods.LDLt(A1)
    A2_LDLt = SolveMethods.LDLt(A2)

    x1_relaxation, iter_count_1 = SolveMethods.relaxation(A1, b1)
    x2_relaxation, iter_count_2 = SolveMethods.relaxation(A2, b2)

    x1_gauss_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x1_gauss, y1))
    x2_gauss_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x2_gauss, y2))/Matrix.cubic_norm(y2)
    task9_3 = """------------------------------------
    A1 condition{0:.3e}
    A2 condition {1:.3e}
    ------------------------------------""".format(A1_cond, A2_cond)
    task9_4 = """------------------------------------
    relative difference norm to solve A1 by gauss {0:.3e}
    relative difference norm to solve A2 by gauss {1:.3e}
    ------------------------------------""".format(x1_gauss_norm_difference, x2_gauss_norm_difference)

    x1_LUP_solution_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x1_LUP_solution, y1))
    x2_LUP_solution_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x2_LUP_solution, y2))/Matrix.cubic_norm(y2)

    L1, U1, P1 = A1_LUP
    L2, U2, P2 = A2_LUP
    task9_5_m = """------------------------------------
    LUP decomposition for A1: 
    {0}
    {1}
    {2}
    LUP decomposition for A2 
    {3}
    {4}
    {5}
    ------------------------------------""".format(Matrix.display(L1, "L1"), Matrix.display(U1, "U1"), Matrix.display(P1, "P1"),
                                                   Matrix.display(L2, "L2"), Matrix.display(U2, "U2"), Matrix.display(P2, "P2"))

    task9_5 = """------------------------------------
    relative difference norm to solve A1 by LUP {0:.3e}
    relative difference norm to solve A2 by LUP {1:.3e}
    ------------------------------------""".format(x1_LUP_solution_norm_difference, x2_LUP_solution_norm_difference)

    x1_square_root_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x1_square_root, y1))
    x2_square_root_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x2_square_root, y2))/Matrix.cubic_norm(y2)

    L1, D1 = A1_LDLt
    L2, D2 = A2_LDLt

    task9_6_m = """------------------------------------
    LDLt decomposition for A1: 
    {0}
    {1}
    {2}
    LDLt decomposition for A2 
    {3}
    {4}
    {5}
    ------------------------------------""".format(Matrix.display(L1, "L1"), Matrix.display(D1, "D1"), Matrix.display(Matrix.transpose(L1), "L1t"),
                                                   Matrix.display(L2, "L2"), Matrix.display(D2, "D2"), Matrix.display(Matrix.transpose(L2), "L2t"))
    task9_6 = """------------------------------------
    relative difference norm to solve A1 by square_root {0:.3e}
    relative difference norm to solve A2 by square_root {1:.3e}
    ------------------------------------""".format(x1_square_root_norm_difference, x2_square_root_norm_difference)

    x1_relaxation_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x1_relaxation, y1))
    x2_relaxation_norm_difference = Matrix.cubic_norm(
        Matrix.vector_difference(x2_relaxation, y2))/Matrix.cubic_norm(y2)

    task9_7 = """------------------------------------
    relative difference norm to solve A1 by relaxation {0:.3e}
    relative difference norm to solve A2 by relaxation {1:.3e}
    ------------------------------------""".format(x1_relaxation_norm_difference, x2_relaxation_norm_difference)

    with open("task9.txt", "w") as file:
        file.write(Matrix.display(A1, "A1")+"\n")
        file.write(Matrix.display(y1, "y1")+"\n")
        file.write(Matrix.display(b1, "b1")+"\n")
        file.write("\n\n")
        file.write(Matrix.display(A2, "A2")+"\n")
        file.write(Matrix.display(y2, "y2")+"\n")
        file.write(Matrix.display(b2, "b2")+"\n")
        file.write(task9_5_m)
        file.write(task9_6_m)
        file.write(task9_3)
        file.write(task9_4)
        file.write(task9_5)
        file.write(task9_6)
        file.write(task9_7)