matn = input("matn kirit: ")
count = 1
count_matn = matn[0]

for i in range(1,len(matn)):
    if matn[i - 1] == matn[i]:
        count+=1
    else:
        if count > 1:
            print("{}{}".format(matn[i - 1],count), end="")
        count = 1
if count > 1:
            print("{}{}".format(matn[i - 1],count), end="")
        