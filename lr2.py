import random
import math
import itertools

# исключение вершин в которые нельзя попасть из первой
# записать индексы -1 к которым нет дороги
arr = [0, 1, 3, 6]


def gen_matrix(arr):
    matrix_D = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]
    matrix_S = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]

    for i in range(0, 7):
        for j in range(i, 7):
            if (i == j):
                matrix_D[i][j] = 0
            elif (i == 0 and (j in arr)):
                matrix_D[i][j] = math.inf
                matrix_D[j][i] = math.inf
            else:
                matrix_D[i][j] = random.randint(1, 10)
                matrix_D[j][i] = matrix_D[i][j]
    for i in range(0, 7):
        for j in range(0, 7):
            if i == j:
                matrix_S[i][j] = math.inf
            else:
                matrix_S[i][j] = j + 1
    return matrix_D, matrix_S


def get_path(output_matrix_D, output_matrix_S):
    v = {0, 1, 2, 3, 4, 5, 6}
    paths = itertools.combinations(v, 2)
    for comb in paths:
        u = comb[0]
        v = comb[1]
        path = [u + 1]
        while u != v:
            u = output_matrix_S[u][v] - 1
            path.append(u + 1)
        print("Путь из " + str(comb[0] + 1) + " в " + str(comb[1] + 1) + ": " + str(path) + " ---------- Длина пути: " + str(output_matrix_D[comb[0]][comb[1]]))


def floyd_algorithm(D0, S0):
    for k in range(0, len(D0)):
        for i in range(len(D0)):
            for j in range(len(D0)):
                if (i == j):
                    pass
                if D0[i][k] + D0[k][j] < D0[i][j]:
                    D0[i][j] = D0[i][k] + D0[k][j]
                    S0[i][j] = k + 1
    print("----------------D" + str(k + 1) + "----------------")
    for row in D0:
        print(row)
    print("----------------------------------\n")
    print("----------------S" + str(k + 1) + "----------------")
    for row in S0:
        print(row)
    print("----------------------------------\n")
    get_path(D0, S0)


def print_floyd(arr):
    new_matrix_D, new_matrix_S = gen_matrix(arr)
    print("----------------D0----------------")
    for row in new_matrix_D:
        print(row)
    print("----------------------------------\n")
    print("----------------S0----------------")
    for row in new_matrix_S:
        print(row)
    print("----------------------------------\n")
    floyd_algorithm(new_matrix_D, new_matrix_S)


def main():

    print_floyd(arr)


if __name__ == "__main__":
    main()
