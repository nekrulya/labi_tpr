import math
import random
from prettytable import PrettyTable


def GenMass():
    N = int(input("Введите количество вершин: "))
    array_row = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        array_row.append(row)

    for i in range(len(array_row)):
        for j in range(i, len(array_row)):
            if i == 0 and j in [2, 3]:
                array_row[i][j] = random.randint(1, 100)
                array_row[j][i] = array_row[i][j]
            if i in [1, 2] and j in [1, 2]:
                array_row[i][j] = random.randint(1, 100)
                array_row[j][i] = array_row[i][j]
            if i in [2, 3, 4] and j in [2, 3, 4]:
                array_row[i][j] = random.randint(1, 100)
                array_row[j][i] = array_row[i][j]
            if i in [4, 5, 6] and j in [4, 5, 6]:
                array_row[i][j] = random.randint(1, 100)
                array_row[j][i] = array_row[i][j]
            if i in [6, 7, 8, 9] and j in [6, 7, 8, 9]:
                array_row[i][j] = random.randint(1, 100)
                array_row[j][i] = array_row[i][j]
            if i == j:
                array_row[i][j] = 0

    for i in array_row:
        print(i)
    return array_row


def FindAllPaths():
    new_arr = GenMass()
    d = {}
    for i in range(len(new_arr)):
        d[i] = dict()
    for j in range(i, len(new_arr)):
    if new_arr[i][j] != 0:
    d[i].update({j: new_arr[i][j]})
    #print("-------------------------")
    #print(d)
    print("-------------------------")
    return d


def GetKeys(l_keys, paths):
n_keys = []
for i in l_keys:
arr_keys = paths[i].keys()
for j in list(arr_keys):
if j > i:
n_keys.append(j)
return n_keys


def Algorithm():

paths = FindAllPaths()
start = 0 #Начальная вершина
stop = 10 #Конечная вершина

d_p = solution(paths, start)

last_keys = [start]
flag = True
k = 2
last_f = [0]
min_for_last = 100000
while flag:
new_keys = GetKeys(last_keys, paths)

arr_for_field = ["x" + str(k)]
field_keys = sorted(set(last_keys))
#Заполнение шапки таблицы
for i in field_keys:
arr_for_field.append("x" + str(k - 1) + " = " + str(i + 1))
arr_for_field.append("f" + str(k) + "(x" + str(k) + ")")
arr_for_field.append("x" + str(k - 1) + "*")

x = PrettyTable()
x.field_names = arr_for_field

#Заполнение строк таблицы
new_keys = sorted(set(new_keys))

minimumi = []

for i in new_keys:
arr_for_row = [i + 1]
min_arr = 10000000
index = -1
z = 0
for j in last_keys:
if i == j:
paths[j][i] = 0
if paths[j].setdefault(i) is not None:
arr_for_row.append(paths[j].setdefault(i) + last_f[z])
else:
arr_for_row.append(paths[j].setdefault(i))
if paths[j].setdefault(i) is not None and paths[j].setdefault(i) + last_f[z] < min_arr:
min_arr = paths[j].setdefault(i) + last_f[z]
index = j + 1
z += 1

#if i == 10 and min_arr < min_for_last:
# min_for_last = min_arr

if min_arr < min_for_last:
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

stop = 9 # делай - 1, если из 5ки в 9ку, то стоп равен 8
way = [stop]
length = d_p[0][stop]

flag = True
while flag:
if d_p[1][way[-1]] == start:
way.append(start)
flag = False
else:
way.append(d_p[1][way[-1]])

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
m=0
minimum=w[0]
for i in range(len(w)):
if w[i]<minimum:
minimum=w[i]
m=i
return Q[m]


def solution(G, s):
Q = [s]
p = {s:None}
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
Algorithm()


if __name__ == "__main__":
main()
