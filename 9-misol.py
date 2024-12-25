number = int(input("Sonni kiriting: "))

s = 0
while number:
    s+=number
    number-=1
print("result {} ".format(s))