#login
def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 't':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')

def main_menu():
    # membuat daftar menu pada kasir
    print('=' * 10, 'MAIN MENU APLIKASI KASIR', '=' * 10)
    print('selamat datang di aplikasi kasir')
    print('=' * 20, 'masukan input aplikasi', '=' * 20)
    print('1. Program kasir')
    print('0. exit program')

    # input pilihan
    pilihan = input('pilih menu: ')

    # pilihan menu
    if pilihan == '1':
        kasir()

    else:
        print("Program terhenti")
        exit()


def kasir():
    total1 = 0
    jenis1 = ""
    porsi = 0
    gelas = 0
    b = []
    nama = []
    a = 0
    data = int(input("masukkan banyak data : "))
    for i in range(data):
        a = input("masukkan nama pembeli : ")
        nama.append(a)

    def panggilnama():
        for each in nama:
            print('\t\t','-',each)
            
        
        
    total2 = 0
    jenis2 = ""
    c = []
    print("\n~~~~Menu Makanan~~~~")
    print("1. Nasi Goreng - Rp. 15000")
    print("2. Soto Medan  - Rp. 9000 ")
    print("3. Mie Ayam    - Rp. 11000")
    print("=" * 50)
    nomor = int(input(" Masukkan Pilihanmu : "))
    porsi = int(input(" Berapa Porsi       : "))

    for i in range(data):
        b.append(porsi)
    if nomor == 1:
        total1 = b[i] * 15000
        print(porsi, "Porsi Nasi Goreng = Rp.", total1)
        jenis1 = ("Nasi Goreng")
    elif nomor == 2:
        total1 = b[i] * 9000
        print(porsi, "Porsi Soto = Rp.", total1)
        jenis1 = ("Soto Medan")
    elif nomor == 3:
        total1 = b[i] * 11000
        print(porsi, "Porsi Mie Ayam = Rp.", total1)
        jenis1 = ("Mie Ayam")
    else:
        print("pilihan tidak ada, silahkan masukan lagi!")

    print("\n~~~~Menu Minuman~~~~")
    print("1. Es teh - Rp2000")
    print("2. Es jeruk - Rp3500")
    print("3. Es kopi - Rp4000")
    print("=" * 50)
    nomor = int(input(" Masukan Pilihan : "))
    gelas = int(input(" Berapa Gelas    : "))
    for i in range(data):
        c.append(gelas)
    if nomor == 1:
        total2 = c[i] * 2000
        print(gelas, "Es Teh = Rp.", total2)
        jenis2 = ("Es Teh")
    elif nomor == 2:
        total2 = c[i] * 3500
        print(gelas, "Es Jeruk = Rp.", total2)
    elif nomor == 3:
        total2 = c[i] * 4000
        print(gelas, "Es Kopi = Rp.", total2)
    else:
        print("pilihan tidak ada, silahkan masukan lagi")

    for i in range(data):
        totalsemua = 0
        totalsemua = total1 + total2
        print("\nTotal harus Dibayar : Rp.", totalsemua)
        uang = int(input("Uang Tunai Pembeli : Rp."))
        if uang > totalsemua:
            kembalian = int(uang - totalsemua)
            print("Kembalian :", kembalian)

            print("\n=================================")
            print("======= S T R U K   B E L I =====")
            print("=================================")
            print(" Nama         :" )
            print(''.format(panggilnama()))
            print(" Beli         :", b[i], jenis1, "-", total1)
            print("               ", c[i], jenis2, "-", total2)
            print(" Tagihan      : Rp.", totalsemua)
            print(" Uang         : Rp.", uang)
            print(" Kembalian    : Rp.", kembalian)
            print("=================================")
            print("=================================")
            tanya()

        elif uang == totalsemua:
            kembalian = int(uang - totalsemua)
            print("Uang anda pas, terimakasih telah berbelanja")

            print("\n=================================")
            print("======= S T R U K   B E L I =====")
            print("=================================")
            print(" Nama         :" )
            print(''.format(panggilnama())) 
            print(" Beli         :", b[i], jenis1, "-", total1)
            print("               ", c[i], jenis2, "-", total2)
            print(" Tagihan      : Rp.", totalsemua)
            print(" Uang         : Rp.", uang)
            print(" Kembalian    : Rp.", kembalian)
            print("=================================")
            print("=================================\n")
            tanya()

        else:
            print("maaf uang anda tidak cukup")
            main_menu()

def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')

    if username == 'admin' and password == 'adminpass':
        print('login berhasil...\n\n')
        main_menu()
    else:
        print('login gagal coba lagi..')
        get_login()

get_login()







