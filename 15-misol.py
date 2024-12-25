number_count = int(input("nichta son kiritmoqchisiz: "))
i = 0
while number_count:
    i+=1
    number = int(input("{}-sonni kiriting: ".format(i)))
    if  number % 2 == 1 and number % 3 == 0:
        print("✅✅✅✅✅✅ {} 🙃".format(number))
    number_count-=1