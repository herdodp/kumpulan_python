from tkinter import*
import math
from tkinter.font import BOLD, Font


# Fungsi menu
def dropdown() :
    print("menu klik 1")

# Frame tkinter
root = Tk()
root.title('konversi OKTAL-BINER-DESIMAL-HEXADESIMAL herdo')
root.geometry('600x550')
root.resizable(0,0)
root.config(bg='pale green')



# menu bar
menu = Menu(root)
root.config(menu = menu)
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label = "konversi", menu = submenu)
submenu.add_command(label = "biner-desimal", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "biner - hexa", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "desimal - biner", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "desimal - hexa", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "desimal - oktal", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "hexa - biner", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "hexa - desimal", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "hexa - oktal", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "oktal - biner", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "oktal - desimal", command = dropdown)
submenu.add_separator()
submenu.add_command(label = "oktal - hexa", command = dropdown)

guide = Menu(menu, tearoff=0)
menu.add_cascade(label = "about", menu = guide)
guide.add_command(label = "tentang aplikasi", command = dropdown)
guide.add_command(label = "license", command = dropdown)




# PROSES KONVERSI
oktal = []

textin = StringVar(root)
ambil = StringVar(root)


def konversi():
    bil = ambil.get()

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
            
        textin.set(hasilTotal)
       
def clear():
    textin.set('')
    ambil.set('')
    oktal.clear() 

# widget
judul = Label(root, text='konversi bilangan oktal ke biner', bg='pale green', font=('calibri',20, 'bold' ))
judul.pack(anchor=CENTER)

teksangka = Label(root, text='Masukkan angka oktal', bg='pale green', font=('calibri',15, 'bold' ))
teksangka.pack(anchor=CENTER)

inputangka = Entry(root,width=20, font=('calibri', 20, 'bold'), bd=10, bg='DeepSkyBlue',textvariable=ambil, selectbackground="yellow", selectforeground='red')
inputangka.pack(anchor=CENTER)

frame_2 = Frame(root, bg='pale green')
frame_2.pack(pady=5)

tombolkonversi = Button(frame_2, text='KONVERSI', padx=8, pady=8, bg='red', bd=10, command=konversi)
tombolkonversi.pack(anchor=W, side=LEFT)

tombolprint = Button(frame_2, text='CLEAR', padx=10, bg='green',bd=10, command=clear)
tombolprint.pack(anchor=W, side=LEFT, padx=10)

kolomhasil = Label(root, height=10,width=45, bd=5, textvariable=textin, font=('calibri', 15, 'bold'))
kolomhasil.place(x=50, y=200)

#frame_3 = Frame(root)
#frame_3.pack()

#kolomhasil = Text(frame_3, height=10, width=45, font=('calibri', 15, 'bold'))
#kolomhasil.pack(side=BOTTOM)


root.mainloop()