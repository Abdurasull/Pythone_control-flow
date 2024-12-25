number = int(input("Sonni kiriting: "))#number obyektiga int turida qiymat taminlaymiz

s = 0#boshlang`ich qiymati 0 ga ting bolgan S nomli obyekt yaratib olamiz
while number:#while loop orqali o`zigacha bo`lgan barcha sonlarni yig`indisini hisoblaymiz
    s+=number#S nomli obyektimizga numberni boshlang`ich qiymatidan boshlab qo`shib boramiz
    number-=1#har bitta sikilimizda number ni 1 ga kamaytirib boramiz
print("result {} ".format(s))#va loop to`gagandan kn natijani ekranga chop etamiz