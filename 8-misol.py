matn = input("matn ni kiriting: ")#matn nomli obyectiga qiymat ta`minlaymiz

array = matn.split()#matndagi barcha so`zlarini split() methodi yordamida bir o`chamli massiv elementlari sifatida taminlab oldik va ularni  array taminladik
for i in range(len(array)):#arraydagi barcha elementlarni yangi qatordan elon qilish 
    print(array[i])