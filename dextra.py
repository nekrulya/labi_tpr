import random, math


def create_matrixs():
    global n, s, d
    d.append([[0] * n for i in range(n)]) #создаем матрицу расстояний, заполненую нулями
    s.append([[0] * n for i in range(n)]) #создаем матрицу последовательности узлов, заполненную нулями
    for i in range(n):
        for j in range(n):
            if i != j:
                s[0][i][j] = j + 1
            else:
                s[0][i][j] = '-'


#создание симмтеричной матрицы
def fill_matrix_symmetrically():
    global n, s, d
    for i in range(n):
        for j in range(i, n):
            if i == j:
                d[0][i][j] = "-"
            elif i == 0 and j not in binded:
                d[0][i][j] = 10000
                d[0][j][i] = 10000
            else:
                d[0][i][j] = random.randint(1, 20)
                d[0][j][i] = d[0][i][j]


#создание асимметричной матрицы
def fill_matrix_asymmetrically():
    global n, s, d, binded
    for i in range(n):
        for j in range(i, n):
            if i == j:
                d[0][i][j] = "-"
            elif i == 0 and j not in binded:
                d[0][i][j] = 10000
                d[0][j][i] = 10000
            else:
                d[0][i][j] = random.randint(10, 20)
                d[0][j][i] = d[0][i][j] - random.randint(1, 9)


n = int(input('Введите размерность матрицы: '))
binded = input('Введите (через пробел) вершины, с которыми связана начальная: ').split()
binded = [int(vertex) - 1 for vertex in binded]