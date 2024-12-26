number = int(input("son kiriting: "))#number obyektiga int turidagi ma`lumotni ta`minlaymiz
i = 2#tub sonlarimiz 2 dan boshlangani uchun i nomli obyekt yaratib olamiz va uni qiymatini 2 ga tenglaymiz
count = 0#tub sonni aniqlash uchun count nomli obyekt yaratamiz va uni qiymatini 0 ga tenlaymiz
while i <= number:#biz kiritgan songa cha bo`lgan holatgacha while loopini aylantiramiz
    for j in range(1, i + 1):#har bitta i obyektimizni tub yoki tub emasligini for loop orqali aniqlaymiz
        if i % j == 0:#agar j i ga qoldiqsiz bo`linsa count ni birga oshiramiz 
            count +=1

    if count <= 2:#for loop tugagandan kn countni 2 dan kichik yoki tenglikga tekshiramiz agar kichik bo`lsa i tub son aks holda tub son emas
        print(i, end=" ")# va tub sonni ekranga chiqaramiz
        count = 0#har bitta aylanishda count ni qiymatini 0 ga tenglashimiz ga to`g`ri keladi
    count = 0
    i+=1#while loop tugashi va kiyingi sonni tikshirish uchun i ni 1 ga oshiramiz`
