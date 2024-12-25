matn = input("Matinni kiriting: ")#matn nomli obyektimizni qiymat bn ta`minlaymiz

matn_array = matn.split()#matn_array nomli massiv yaratib olamiz va unga split function orqali matn obyektimizga tegizli bo lgan barcha so`zlarni massiv ni elementlari sifatida qabul qilamiz

max_array = matn_array[0]#max_array nomli obyekt yaratib olamiz va uning qiymatini massivimizning 0 - chi indexining qiymatiga tenglaymiz 

for i in matn_array:#for loop orqali eng uzun so`zni aniqlaymiz
    if len(max_array) < len(i):
        max_array = i
print("result: {}".format(max_array))#va natijani ekranga chiqaramiz