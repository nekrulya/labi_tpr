import random


solutions = int(input('Введите количество решений: '))
states = int(input('Введите количество состояний: '))

matrix_start = [[0]*states for i in range(solutions)]


for i in range(solutions):
    for j in range(states):
        matrix_start[i][j] = random.randint(1, 100)

for i in range(solutions):
    print(matrix_start[i])

matrix_for_gurvic = matrix_start.copy()
matrix_for_BL = matrix_start.copy()
print('')


def gurvic(matrix_for_gurvic):
    print('Решение методом Гурвица: ')
    index_list = []
    e_list = []
    c = float(input('Введите значение весового коэффициента: '))
    for i in range(solutions):
        minimum = min(matrix_for_gurvic[i])
        maximum = max(matrix_for_gurvic[i])
        e = round(c * minimum + (1-c) * maximum, 2)
        e_list.append(e)
        matrix_for_gurvic[i].append(e)
        print(matrix_for_gurvic[i])

    for i in range(len(e_list)):
        if e_list[i] == max(e_list):
            index_list.append(i+1)

    print('Значения нового столбца: ')

    for i in range(solutions):
        print(e_list[i])
        matrix_for_gurvic[i].pop(-1)


    print('Оптимальные решения методом Гурвица: ')

    for i in range(len(index_list)):
        print(f'E{index_list[i]}', end=' ')
        print(matrix_for_gurvic[index_list[i]], '\n')


def BL(matrix_for_BL):
    index_list = []
    e_list = []
    q = round(1 / states, 2)
    for i in range(solutions):
        e = 0
        for j in range(states):
            e += q * matrix_for_BL[i][j]
        e_list.append(round(e, 2))
        matrix_for_BL[i].append(round(e, 2))
        print(matrix_for_BL[i])

    for i in range(len(e_list)):
        if e_list[i] == max(e_list):
            index_list.append(i + 1)

    print('Значения нового столбца: ')
    for i in range(solutions):
        print(e_list[i])
        matrix_for_BL[i].pop(-1)

    print('Оптимальные решения методом Байеса-Лапласа: ')

    for i in range(len(index_list)):
        print(f'E{index_list[i]}', end=' ')
        print(matrix_for_BL[i - 1])


if __name__ == '__main__':
    gurvic(matrix_for_gurvic)
    BL(matrix_for_BL)
