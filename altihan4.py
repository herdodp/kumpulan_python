import time

name = "herdo"
kunci = 123


time.sleep(1)
def login() :
    nama = input("masukkan nama : ")
    password = int(input("masukkan password : "))
    if nama == name and password == kunci :
        print("login sukses")
    else :
        print("login gagal")

login() 