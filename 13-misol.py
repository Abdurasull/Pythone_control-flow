from math import sqrt

number = int(input("son kiriting: "))
i = 2
count = 0
while i <= number:
    for j in range(1, i + 1):
        if i % j == 0:
            count +=1

    if count <= 2:
        print(i, end=" ")
        count = 0
    count = 0
    i+=1
