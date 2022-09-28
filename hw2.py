# Задача №68. Количество элементов больших обоих соседей
s = input()
array = list(map(int, (input()).split()))
n = len(array)
a = 0
for i in range(1, n - 1):
    if (array[i] > array[i - 1]) & (array[i] > array[i + 1]):
        a += 1
print(a)


#Задача №69. Переставить элементы в обратном порядке
s = input()
array = list(input().split(' '))
for i in reversed(array):
    print(i, end=' ')

#Задача №72. Максимум в массиве
myList = input().split()
print((max(myList)))
