nama = []
p1 = []
p2 = []
print("\tProgram pemilihan reksadana yang cocok menurut profil resiko")

data = int(input("Masukan banyak data:"))

for i in range(data):
    a = input("\nMasukan Nama anda:")
    nama.append(a)

    print("\n{} silahkan jawab pertanyaan dibawah ini".format(nama[i]))

    print("\nDalam Investasi apa yang paling penting")
    print("1.Memaksimalkan Keuntungan")
    print("2.Menghindari Kerugian")
    print("3.Keduanya sama penting")

    b = int(input("\nMasukan jawaban anda dengan memasukan angka 1-3:"))
    p1.append(b)

    print("\nPasar uang seringkali naik-turun jika nilai investasi kamu turun 15%")
    print("dalam sebulan dengan keadaan pasar yang tidak menentu, apa yang akan")
    print("kamu lakukan?")
    print("1.Jual Semua")
    print("2.Jual Sebagian")
    print("3.Simpan Semua")
    print("4.Beli Lagi")

    c = int(input("\nMasukan jawaban anda dengan memasukan angka 1-4:"))
    p2.append(c)

    if b==1 and c==1:
        pasaruang = (10/100)
        obligasi = (65/100)
        saham  = (25/100)
        level = "moderat"
    elif b==1 and c==2:
        pasaruang = (10/100)
        obligasi = (53/100)
        saham = (37/100)
        level = "konservatif"
    elif b==1 and c==3:
        pasaruang = (10/100)
        obligasi = (43/100)
        saham = (47/100)
        level = "moderat"
    elif b==1 and c==4:
        pasaruang = (10/100)
        obligasi = (34/100)
        saham = (56/100)
        level= "agresif"

    print("\n{} Profile resiko kamu di level {}".format(nama[i],level))
    print("Pasar uang {}%".format(pasaruang * 100))
    print("Obligasi {}%".format(obligasi * 100))
    print("Saham {}%".format(saham * 100))

    uang = int(input("Masukan jumlah uang yang ingin kamu investasikan:Rp."))

    print("\nReksadana Pasar Uang\t:Rp.{}".format(uang * pasaruang))
    print("Reksadana Obligasi\t:Rp.{}".format(uang * obligasi))
    print("Reksadana Saham\t\t:Rp.{}".format(uang * saham))
