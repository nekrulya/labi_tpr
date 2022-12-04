import math
from random import randint
from prettytable import PrettyTable


def create_matrixs():
    global matrix, n
    matrix = ([[0] * n for i in range(n)]) #создаем матрицу расстояний, заполненую нулями


#создание симмтеричной матрицы
def fill_matrix_symmetrically():
    global matrix, blocks, n
    for block in blocks.values():
        for i in block:
            for j in block:
                if i == j:
                    matrix[i][j] = "-"
                else:
                    matrix[i][j] = randint(1, 10)
                    matrix[j][i] = matrix[i][j]


#создание асимметричной матрицы
def fill_matrix_asymmetrically():
    global matrix, blocks, n
    for block in blocks.values():
        for i in block:
            for j in block:
                if i == j:
                    matrix[i][j] = "-"
                else:
                    matrix[i][j] = randint(1, 10)


n = 7
matrix = []
create_matrixs()
blocks = {
    'block1': [0, 1, 2, 3],
    'block2': [2, 3, 4, 5],
    'block3': [4, 5, 6]
}


fill_matrix_asymmetrically()

for row in matrix:
    print(row)

mytable = PrettyTable()
fx = {}
x_star = {}

fx["f6(x6) - 5"] = matrix[4][6]
fx["f6(x6) - 6"] = matrix[5][6]
mytable.field_names = ["x6", "x7 = 6", "f6(x6)", "x7*"]
mytable.add_row(["5", str(matrix[4][6]), str(matrix[4][6]), "7"])
mytable.add_row(["6", str(matrix[5][6]), str(matrix[5][6]), "7"])

print(mytable)

fx["f5(x5) - 5"] = min(matrix[4][5] + fx["f6(x6) - 5"], matrix[4][6])
fx["f5(x5) - 6"] = min(matrix[5][4] + fx["f6(x6) - 5"], matrix[5][6])

mytable = PrettyTable()

if matrix[4][5] < matrix[4][6]:
    x_star['6* - 5'] = "6"
else:
    x_star['6* - 5'] = "7"

if matrix[5][6] < matrix[5][6]:
    x_star['6* - 6'] = "5"
else:
    x_star['6* - 6'] = "7"

mytable.field_names = ["x5", "x6 = 5", "x6 = 6", "x7 = 7", "f5(x5)", "x6*"]
mytable.add_row(["5", "-", str(matrix[4][5] + fx["f6(x6) - 5"]), str(matrix[4][6]), str(fx["f5(x5) - 5"]), x_star['6* - 5']])
mytable.add_row(["6", str(matrix[5][4] + fx["f6(x6) - 5"]), "-", str(matrix[5][6]), str(fx["f5(x5) - 6"]), x_star['6* - 6']])

print(mytable)

fx["f4(x4) - 3"] = min(matrix[2][4] + fx["f5(x5) - 5"], matrix[2][5] + fx["f5(x5) - 6"])
fx["f4(x4) - 4"] = min(matrix[3][4] + fx["f5(x5) - 5"], matrix[3][5] + fx["f5(x5) - 6"])

if matrix[2][4] + fx["f5(x5) - 5"] < matrix[2][5] + fx["f5(x5) - 6"]:
    x_star['5* - 3'] = "5"
else:
    x_star['5* - 3'] = "6"

if matrix[3][4] + fx["f5(x5) - 5"] < matrix[3][5] + fx["f5(x5) - 6"]:
    x_star['5* - 4'] = "5"
else:
    x_star['5* - 4'] = "6"

mytable = PrettyTable()
mytable.field_names = ["x4", "x5 = 5", "x5 = 6", "f4(x4)", "x5*"]
mytable.add_row(["3", str(matrix[2][4] + fx["f5(x5) - 5"]), str(matrix[2][5] + fx["f5(x5) - 6"]),  str(fx["f4(x4) - 3"]), x_star['5* - 3']])
mytable.add_row(["4", str(matrix[3][4] + fx["f5(x5) - 5"]), str(matrix[3][5] + fx["f5(x5) - 6"]), str(fx["f4(x4) - 4"]), x_star['5* - 4']])

print(mytable)

fx["f3(x3) - 3"] = min(matrix[2][3] + fx["f4(x4) - 3"], matrix[2][4] + fx["f5(x5) - 5"])
fx["f3(x3) - 4"] = min(matrix[3][2] + fx["f4(x4) - 4"], matrix[3][4] + fx["f5(x5) - 5"])

if matrix[2][3] + fx["f4(x4) - 3"] < matrix[2][4] + fx["f5(x5) - 5"]:
    x_star['4* - 3'] = "4"
else:
    x_star['4* - 3'] = "5"

if matrix[3][2] + fx["f4(x4) - 4"] < matrix[3][4] + fx["f5(x5) - 5"]:
    x_star['4* - 4'] = "3"
else:
    x_star['4* - 4'] = "5"

mytable = PrettyTable()
mytable.field_names = ["x3", "x4 = 3", "x4 = 4", "x4 = 5", "f3(x3)", "x4*"]
mytable.add_row(["3", "-", str(matrix[2][3] + fx["f4(x4) - 3"]), str(matrix[2][4] + fx["f5(x5) - 5"]),  str(fx["f3(x3) - 3"]), x_star['4* - 3']])
mytable.add_row(["4", str(matrix[3][2] + fx["f4(x4) - 4"]), "-", str(matrix[3][4] + fx["f5(x5) - 5"]), str(fx["f3(x3) - 4"]), x_star['4* - 4']])

print(mytable)

fx["f2(x2) - 1"] = min(matrix[0][2] + fx["f3(x3) - 3"], matrix[0][3] + fx["f3(x3) - 4"])
fx["f2(x2) - 2"] = min(matrix[1][2] + fx["f3(x3) - 3"], matrix[1][3] + fx["f3(x3) - 4"])

if matrix[0][2] + fx["f3(x3) - 3"] < matrix[0][3] + fx["f3(x3) - 4"]:
    x_star['3* - 1'] = "3"
else:
    x_star['3* - 1'] = "4"

if matrix[1][2] + fx["f3(x3) - 4"] < matrix[1][3] + fx["f3(x3) - 4"]:
    x_star['3* - 2'] = "3"
else:
    x_star['3* - 2'] = "4"

mytable = PrettyTable()
mytable.field_names = ["x2", "x3 = 3", "x3 = 4", "f2(x2)", "x3*"]
mytable.add_row(["1", str(matrix[0][2] + fx["f3(x3) - 3"]), str(matrix[0][3] + fx["f3(x3) - 4"]),  str(fx["f2(x2) - 1"]), x_star['3* - 1']])
mytable.add_row(["2", str(matrix[1][2] + fx["f3(x3) - 3"]), str(matrix[1][3] + fx["f3(x3) - 4"]), str(fx["f2(x2) - 2"]), x_star['3* - 2']])

print(mytable)

fx["f1(x1) - 1"] = min(matrix[0][1] + fx["f2(x2) - 2"], matrix[0][2] + fx["f3(x3) - 3"], matrix[0][3] + fx["f3(x3) - 4"])
fx["f1(x1) - 2"] = min(matrix[1][2] + fx["f3(x3) - 3"], matrix[1][3] + fx["f3(x3) - 4"])

if matrix[0][1] + fx["f2(x2) - 2"] < matrix[0][2] + fx["f3(x3) - 3"] and matrix[0][1] + fx["f2(x2) - 2"] < matrix[0][3] + fx["f1(x1) - 1"]:
    x_star['2* - 1'] = "2"
elif matrix[0][2] + fx["f3(x3) - 3"] < matrix[0][1] + fx["f2(x2) - 2"] and matrix[0][2] + fx["f3(x3) - 3"] < matrix[0][3] + fx["f1(x1) - 1"]:
    x_star['2* - 1'] = "3"
else:
    x_star['2* - 1'] = "4"

if matrix[1][2] + fx["f3(x3) - 3"] < matrix[1][3] + fx["f3(x3) - 4"]:
    x_star['2* - 2'] = "3"
else:
    x_star['2* - 2'] = "4"


mytable = PrettyTable()
mytable.field_names = ["x1", "x2 = 2", "x2 = 3", "x2 = 4", "f1(x1)", "x2*"]
mytable.add_row(["1", str(matrix[0][1] + fx["f2(x2) - 2"]), str(matrix[0][2] + fx["f3(x3) - 3"]), str(matrix[0][3] + fx["f3(x3) - 4"]), str(fx["f1(x1) - 1"]), x_star['2* - 1']])
# mytable.add_row(["2", "-", str(matrix[1][2] + fx["f3(x3) - 3"]), str(matrix[1][3] + fx["f3(x3) - 4"]), str(fx["f1(x1) - 2"]), x_star['2* - 2']])

print(mytable)

print(f"Кратчайший путь: ")