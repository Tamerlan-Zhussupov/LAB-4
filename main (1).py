from random import randint
a = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range (0, 5):
    for j in range (0, 5):
        a[i][j]=randint(-50, 100)

sum = 0
count1 = 0
for i in range (0, 5):
    for j in range (0, 5):
        if i != j and j < i:
            count1 = count1 + 1
            sum = sum + a[i][j]

ar = sum / count1
print("Среднеарифметическое массива: ")
print(ar)
min = a[0][0];
max = a[0][0];
for i in range (0, 5):
    for j in range (0, 5):
        if a[i][j] < min:
            min = a[i][j]
            
        if a[i][j] > max:
            max = a[i][j]
print("Massive: ")
print(a)
print("MIN: ")
print(min)
print("MAX: ")
print(max)
ar2 = (min + max) / 2
print("Среднеарифметическое MIN/MAX: ")
print(ar2)