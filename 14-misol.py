number = int(input("sonni kiriting:"))#number obyektiga butun qiymat ta`minlaymiz

for i in range(1, number + 1):#for loop orqali 1dan boshlab numberga cha bo`lgan barcha qiymatlarni aylantiramiz`
    if number % i == 0:#agar i numberga bo`linsa u holda i ni ekranga chiqaramiz`
        print(i, end=" ")