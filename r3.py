import random
from prettytable import PrettyTable

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def GenMatrix(peaks, typeMatrix, block_or_tape, ways):
    #создаем двумерный массив заполненный нулями
    Matrica = []
    for i in range(peaks):
        row = []
        for j in range(peaks):
            row.append(0)
        Matrica.append(row)
    print(Matrica)
    if typeMatrix == '1' and block_or_tape == '1': #симметричная ленточная
        tape_width = int(input("Введите ширину ленты: "))
        for i in range(peaks):
            #идем из [0][0] пока длина ленты не упрется в конец матрицы
            if i + tape_width < peaks:
                for j in range(i, i + tape_width + 1):
                    Matrica[i][j] = random.randint(1, 10)
                    Matrica[j][i] = Matrica[i][j]
            #уперлись в стенку матрицы -> идем до конца без ширины
            else:
                for j in range(i, peaks):
                    Matrica[i][j] = random.randint(1, 10)
                    Matrica[j][i] = Matrica[i][j]
            #зануляем отсутсвующие дороги
            for j in range(peaks):
                if i == 0 and not j in ways:
                    Matrica[i][j] = 0
                    Matrica[j][i] = Matrica[i][j]
            #зануляем главную диагональ
            for j in range(peaks):
                if i == j:
                    Matrica[i][j] = 0

    elif typeMatrix == '2' and block_or_tape == '1': #несимметричная ленточная
        tape_width = int(input("Введите ширину ленты: "))
        for i in range(peaks):
            # идем из [0][0] пока длина ленты не упрется в конец матрицы
            if i + tape_width < peaks:
                for j in range(i, i + tape_width + 1):
                    Matrica[i][j] = random.randint(5, 10)
                    Matrica[j][i] = Matrica[i][j] - random.randint(-4, 4)
            # уперлись в стенку матрицы -> идем до конца без ширины
            else:
                for j in range(i, peaks):
                    Matrica[i][j] = random.randint(5, 10)
                    Matrica[j][i] = Matrica[i][j] - random.randint(-4, 4)
            # зануляем отсутсвующие дороги
            for j in range(peaks):
                if i == 0 and not j in ways:
                    Matrica[i][j] = 0
                    Matrica[j][i] = Matrica[i][j]
            # зануляем главную диагональ
            for j in range(peaks):
                if i == j:
                    Matrica[i][j] = 0

    elif typeMatrix == '1' and block_or_tape == '2': #симметричная блочная
        block_list = []
        num_blocks = int(input('Введите количество блоков: '))
        for i in range(num_blocks):
            #Ввод значений индексов блоков: str -> int -> list -> уменьшение значений на 1 для записи в индексы матрицы -> list
            block_list.append(list(map(lambda block: block - 1, list(map(int, input(f'Введите через запятую индексы элементов {i + 1} блока: ').split(','))))))
        for i in range(len(Matrica)):
            for j in range(i, len(Matrica)):
                if i == 0 and j in ways:
                    Matrica[i][j] = random.randint(5, 10)
                    Matrica[j][i] = Matrica[i][j]
                for el in block_list:
                    if i in el and j in el:
                        Matrica[i][j] = random.randint(5, 10)
                        Matrica[j][i] = Matrica[i][j]
                if i == j:
                    Matrica[i][j] = 0
        # print(block_list)

    elif typeMatrix == '1' and block_or_tape == '2': #несимметричная блочная
        block_list = []
        num_blocks = int(input('Введите количество блоков: '))
        for i in range(num_blocks):
            # Ввод значений индексов блоков: str -> int -> list -> уменьшение значений на 1 для записи в индексы матрицы -> list
            block_list.append(list(map(lambda block: block - 1, list(
                map(int, input(f'Введите через запятую индексы элементов {i + 1} блока: ').split(','))))))
        for i in range(len(Matrica)):
            for j in range(i, len(Matrica)):
                if i == 0 and j in ways:
                    Matrica[i][j] = random.randint(5, 10)
                    Matrica[j][i] = Matrica[i][j] - random.randint(-4, 4)
                for el in block_list:
                    if i in el and j in el:
                        Matrica[i][j] = random.randint(5, 10)
                        Matrica[j][i] = Matrica[i][j] - random.randint(-4, 4)
                if i == j:
                    Matrica[i][j] = 0
    else:
        print("Ошибка ввода")
    print_matrix(Matrica)
    return Matrica


def FindAllPaths(peaks):
    # ввод вершин до которых есть пути: str -> int -> list -> уменьшение элементов списка на один для подставления в индексы -> list
    ways = list(map(lambda way: way - 1, list(
        map(int, input("Введите через запятую вершины с которыми связана первая вершина: ").split(',')))))

    print(ways)

    typeMatrix = input("Выберите тип матрицы:\n1) Симметричная\n2) Несимметричная\n")
    block_or_tape = input("Выберите:\n1) Ленточная\n2) Блочно-диагональная\n")
    New_Matrica = GenMatrix(peaks, typeMatrix, block_or_tape, ways)
    dict_ways = {}
    for i in range(len(New_Matrica)):
        dict_ways[i] = dict()
        for j in range(i, len(New_Matrica)):
            if New_Matrica[i][j] != 0:
                dict_ways[i].update({j: New_Matrica[i][j]})
    print("-------------------------")
    print(dict_ways)
    print("-------------------------")
    return dict_ways


def GetKeys(l_keys, paths): #возвращает связные вершины
    n_keys = []
    for i in l_keys:
        arr_keys = paths[i].keys()
        for j in list(arr_keys):
            if j > i:
                n_keys.append(j)
    return n_keys


def Algorithm(peaks):

    paths = FindAllPaths(peaks)
    start = 0
    stop = peaks - 1

    min_paths_list = solution(paths, start)

    last_keys = [start]
    flag = True
    k = 2
    last_f = [0] #предыдущее f (например f2)
    min_for_last = 1000000
    while flag:
        new_keys = GetKeys(last_keys, paths)

        arr_for_field = ["x" + str(k)]
        field_keys = sorted(set(last_keys))
        # Заполнение шапки таблицы
        for i in field_keys:
            arr_for_field.append("x" + str(k - 1) + " = " + str(i + 1))
        arr_for_field.append("f" + str(k) + "(x" + str(k) + ")")
        arr_for_field.append("x" + str(k - 1) + "*")

        x = PrettyTable()
        x.field_names = arr_for_field

        # Заполнение строк таблицы
        new_keys = sorted(set(new_keys))

        minimumi = []

        for i in new_keys:
            arr_for_row = [i + 1]
            min_arr = 10000000
            index = -1
            z = 0
            for j in last_keys:
                if i == j:
                    paths[i][j] = 0
                if paths[j].setdefault(i) is not None:
                    arr_for_row.append(paths[j].setdefault(i) + last_f[z])
                else:
                    arr_for_row.append(paths[j].setdefault(i))
                if paths[j].setdefault(i) is not None and paths[j].setdefault(i) + last_f[z] < min_arr:
                    min_arr = paths[j].setdefault(i) + last_f[z]
                    index = j + 1
                z += 1

            if i == 10 and min_arr < min_for_last:
                min_for_last = min_arr

            minimumi.append(min_arr)
            arr_for_row.append(min_arr)
            arr_for_row.append(index)
            x.add_row(arr_for_row)
        last_f.clear()
        last_f = minimumi.copy()
        k += 1
        last_keys.clear()
        last_keys = new_keys.copy()
        if len(last_keys) == 1:
            flag = False
        print(x)

    stop = peaks - 1 #последняя вершина
    way = [stop]
    length = min_paths_list[0][stop]

    flag = True
    while flag:
        if min_paths_list[1][way[-1]] == start:
            way.append(start)
            flag = False
        else:
            way.append(min_paths_list[1][way[-1]])

    way = way[::-1]
    res = ''

    for i in range(len(way) - 1):
        res += str(way[i] + 1) + " -> "
    res += str(way[-1] + 1)

    print("Кратчайший путь: " + str(res))
    print("-------------------------------")
    print("Кратчайшее расстояние: " + str(length))
    print("-------------------------------")


def find_min(Q, w):
    m = 0
    minimum = w[0]
    for i in range(len(w)):
        if w[i] < minimum:
            minimum = w[i]
            m = i
    return Q[m]


def solution(G, s):
    Q = [s]
    p = {s: None}
    w = [0]
    d = {}
    for i in G:
        d[i] = float('inf')
        Q.append(i)
        w.append(d[i])
    d[s]=0
    while Q:
        u = find_min(Q, w)
        Q.remove(u)
        for v in G[u]:
            if d[v] >= d[u]+G[u][v]:
                d[v] = d[u]+G[u][v]
                p[v] = u
    return d, p


def main():
    peaks = int(input("Введите количество вершин: "))
    Algorithm(peaks)


if __name__ == '__main__':
    main()
