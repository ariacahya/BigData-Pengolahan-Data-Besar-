print ("Hello World")

name = "STMIK"

print(name)

cars = ["Ford", "Volvo", "BMW"]
print(cars[:2])
 
#MENGELUARKAN ISISAN ARRAYGROUP JADI ATOMIK
for carItem in cars:
    print(carItem)
    if(carItem=="Ford"):
        print("oke ==> " + carItem)


#CHALLANGE
resultUts = 0
nUts = [70,60,100]
for i in range(0, len(nUts)):
    resultUts = resultUts + nUts[i]

print(str(resultUts))