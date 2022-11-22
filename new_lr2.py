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


def floyd():
    global d, s
    for k in range(len(d[0])):
        for i in range(k):
            for j in range(k):
                if i != j and j != k and i != k:
                    if d[0][i][k] + d[0][k][j] < d[0][i][j]:
                        d[0][i][j] = d[0][i][k] + d[0][k][j]
                        s[0][i][j] = k + 1
            for q in range(k + 1, len(d[0])):
                if i != q and q != k and i != k:
                    if d[0][i][k] + d[0][k][q] < d[0][i][q]:
                        d[0][i][q] = d[0][i][k] + d[0][k][q]
                        s[0][i][q] = k + 1
        for p in range(k + 1, len(d[0])):
            for j in range(k):
                if p != j and j != k and p != k:
                    if d[0][p][k] + d[0][k][j] < d[0][p][j]:
                        d[0][p][j] = d[0][p][k] + d[0][k][j]
                        s[0][p][j] = k + 1
            for q in range(k + 1, len(d[0])):
                if p != q and q != k and p != k:
                    if d[0][p][k] + d[0][k][q] < d[0][p][q]:
                        d[0][p][q] = d[0][p][k] + d[0][k][q]
                        s[0][p][q] = k + 1




n = int(input('Введите размерность матрицы: '))
binded = input('Введите (через пробел) вершины, с которыми связана начальная: ').split()
binded = [int(vertex) - 1 for vertex in binded]

d = []
# [['-', 14, 12, 10000, 10000],
# [9, '-', 19, 11, 14],
# [3, 12, '-', 11, 13],
# [10000, 7, 5, '-', 20],
# [10000, 10, 10, 13, '-']]
s = []
create_matrixs()

is_symm = input('Матрица симметричная? Да/Нет: ')

if is_symm == 'Да':
    fill_matrix_symmetrically()
else:
    fill_matrix_asymmetrically()

print("----------------D0----------------")
for i in d[0]:
    print(i)
print("----------------S0----------------")
for i in s[0]:
    print(i)

floyd()
print(f"----------------D{n}----------------")
for i in d[0]:
    print(i)
print(f"----------------S{n}----------------")
for i in s[0]:
    print(i)

start = int(input('Введите начальную вершину: ')) - 1
end = int(input('Введите конечную вершину: '))

path = []
while s[0][start][end - 1] != end:
    path.append(end)
    end = s[0][start][end - 1]

else:
    path.append(s[0][start][end - 1])
    path.append(1)
path.reverse()

for i in range(len(path) - 1):
    print(path[i], end=" -> ")
print(path[len(path) - 1])
print(path)
path_length = 0
for i in range(len(path) - 1):
    path_length += d[0][path[i] - 1][path[i + 1] - 1]
print('Длина пути равна:', path_length)