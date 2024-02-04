import math

#batas library doang h3h3

#input bil. oktal
oktal = []
bil = input("masukkan angka oktal: ")

#mengubah menaruh tiap bilangan oktal ke array
for i in range(len(bil)):
    oktal.append(bil[i])

print("bilangan oktalnya =", oktal)

#proses konversi
hasilTotal = ""
for each in oktal:
    if(int(each) >= 8):
        print("\n", each, "\ntomlol")
    elif(int(each) >= 4):
        print("\n",each)
        print(each, ": 2 =", math.floor(int(each)/2), "sisa", int(each)%2)
        dua = math.floor(int(each)/2)
        print(dua, ": 2 =", math.floor(int(dua)/2), "sisa", int(dua)%2)
        hasilEach = str(math.floor(int(dua)/2)) + str(int(dua)%2) + str(int(each)%2)
        hasilTotal = hasilTotal + hasilEach
        print(hasilEach)
    elif(int(each) == 0):
        print("\n", each, "\n\n\n000")
        hasilEach = "000"
        hasilTotal = hasilTotal + hasilEach
    elif(int(each) < 4):
        print("\n",each)
        print(each, ": 2 =", math.floor(int(each)/2), "sisa", int(each)%2)
        dua = math.floor(int(each)/2)
        print("")
        hasilEach = "0" + str(math.floor(int(each)/2)) + str(int(each)%2)
        hasilTotal = hasilTotal + hasilEach
        print(hasilEach)
    
#output hasil konversi
print(bil, "(8) =",hasilTotal,"(2)")
