from random import randint


def massiv_null():
    for i in range(n):
        for j in range(n):
            massiv[i][j] = -1
    for i in range(n):
        x_pred[i] = -1
    for i in range(n):
        x[i] = -1


def gener_massiv():
    massiv[0][1] = randint(1, 91)
    massiv[0][2] = randint(1, 91)
    massiv[1][1] = randint(1, 91)
    massiv[2][0] = randint(1, 91)

    for i in range(n):
        j = i + 1
        while j < shir_lent + i + 1 and j < n:
            massiv[i][j] = randint(1, 91)
            massiv[j][i] = randint(1, 91)
            j += 1
    for j in range(n):
        i = j + 1
        while i < shir_lent + j + 1 and i < n:
            massiv[i][j] = randint(1, 91)
            i += 1
    print(' ')
    for i in range(n):
        print(i + 1)
    print('')
    print(' ')
    for i in range(n):
        print("----")
    print('')
    for i in range(n):
        print(i + 1, "|")
        for j in range(n):
            if massiv[i][j] == -1:
                print('-')
            else:
                print(massiv[i][j])
        print('')
    print("_____________________________________________________________")
    print('')


def versh(k):
    global x_kol
    for i in range(k+1, n):
        if massiv[k][i] != -1:
            flag = False
            for j in range(x_kol):
                if x[j] == i:
                    flag = True
            if not flag:
                x[x_kol] = i
                x_kol += 1


def shag(k):
    print(' ')
    for i in range(17):
        print("----")
    print('')
    print('x' + str(k))
    x_kol = 0
    for i in range(x_pred_kol):
        versh(x_pred[i])
        print('x' + str(k - 1) + "=" + x_pred[i] + 1)
    print("f" + str(k) + "(x" + str(k) + ")")
    print("оптимальное х")
    for i in range(17):
        print("----")
    for i in range(x_kol):
        print(x[i] + 1)
        min = 1000
        for j in range(x_pred_kol):
            if x[i] > x_pred[j]:
                if massiv[x_pred[j][x[i]] == -1]:
                    print("-")
                else:
                    r = massiv[x_pred[j][x[i]] + massiv1[k-2][j][1]]
                    if r > 0:
                        print(r)
                        if r < min:
                            min = r
                            massiv1[k - 1][i][1] = min
                            massiv1[k - 1][i][2] = x_pred[j]
            else:
                print("-")
        massiv1[k - 1][i][0] = x[i]
        massiv1_length[k - 1] = x_kol
        print(massiv1[k -1][i][1])
        print(massiv1[k -1][i][2] + 1)


def poisk(i):
    global massiv1_length
    k = massiv1_length[i] - 1
    print(massiv1[i][k][0] + 1)
    while True:
        i -= 1
        for j in range(massiv1_length[i]):
            if massiv1[i][j][0] == massiv1[i + 1][k][2]:
                print(" <- ", end="")
                k = j
                break
        if i == 0:
            break


def optim_resh():
    global massiv1_length
    k = 2
    x_pred[0] = 0
    x_predkol = 1
    for j in range(n):
        shag(k)
        for i in range(n):
            if x[i] == n:
                x[i] = -1
                x_kol -= 1
            else:
                x_pred[i] = x[i]
                x[i] -= 1
        x_pred_kol = x_pred_kol
        x_kol = 0
        k += 1
    min = 100000
    for i in range(n - 2, -1, -1):
        if massiv1[i][massiv1_length[i] - 1][0]  == n - 1:
            if massiv1[i][massiv1_length[i] - 1][1] < min:
                min = massiv1[i][massiv1_length[i] - 1][1]
    num = 0
    for i in range(n - 2, -1, -1):
        if massiv1[i][massiv1_length[i] - 1][0] == n - 1:
            if massiv1[i][massiv1_length[i] - 1][1] == min:
                num += 1
                print('Кратчайший путь из...', end="")
                poisk(i)
                print('Длина кратчайшего пути', massiv1[i][massiv1_length[i] - 1][1])
                print("____________________________________")



def main():
    massiv_null()
    gener_massiv()
    optim_resh()


massiv = []
massiv1 = []
n = 7
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    massiv.append(row)
# massiv.append([[0] * n for i in range(n)])
massiv1.append([[[0] * n for j in range(n)] * n for i in range(n)])
x_kol = 0
x_pred = []
x = []
shir_lent = 2
x_pred_kol = 0
massiv1_length = []
main()
























