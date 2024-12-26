matn = input("matn kirit: ")#matn nomli obyekt yaratamiz va unga qiymat ta`minlaymiz
count = 1#bilgilarimizni sanash uchun boshlangich qiymati 1 ga teng bo`lgan count nomli obyekt yaratib olamiz
count_matn = matn[0]#count_matn nomli obyekt yaratamiz va uni qiymatini kiritgan matn nimizni 1-bilgisiga ta`minlaymiz

for i in range(1,len(matn)):#for loop orqali barcha bilgi larimizni solishtiramiz
    if matn[i - 1] == matn[i]:#dastlabki bilgi va unga qo`shbi bo`lgan bilgini solishtiramiz 
        count+=1#agar ular teng bo`lsa count ni 1 ga oshiramiz 
    else:
        if count > 1: #agar teng bo`lmasa count 1 dan kattami yo`qmi shuni so`raymiz
            print("{}{}".format(matn[i - 1],count), end="")#agar katta bo`lsa bir biriga qo`shni bo`lgan bilgilar teng bo`lgan bo`ladi
        count = 1 #va har doim count ni qiymatini 1 ga ta`minlab qo`yamiz
if count > 1:#va har doim so`zimizni oxirida ham count ni qiymatini tekshirib olamiz
    print("{}{}".format(matn[i - 1],count), end="")#agar katta bo`lsa bir biriga qo`shni bo`lgan bilgilar teng bo`lgan bo`ladi
        