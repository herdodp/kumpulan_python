from tkinter import*
import random


root = Tk()
root.geometry("1500x550")
root.title("acak anggota kelompok tugas pak rektor kelas pagi (SI TK)")

textin = StringVar()

def acak():
    listnama = ["zulfikar", "meilisa","adam anwar","nova eko","iin maharani","naisha","moh nur arif","nazir","diva","khayza","dita puji", "herdo","tapha","yurna sari","aditya p","riyan AA","silviyana","jihan","ardifa","fadillah A","satriya adi","BUDI TK","AZMA TK","ANDIKA TK","PUTRI TK","OKTAVIA TK","AGNES TK","JEREMY TK", "ARVY TK", "RICKY TK", "RAHMADI TK"]
    nama = random.choice(listnama)

    text_d.config(state=NORMAL)
    
    if text_d.get("1.0", END):
    	text_d.delete("1.0", END)

    text_d.insert("1.0", nama)
    text_d.config(state=DISABLED)

top_frame = Frame()
top_frame.pack(fill=BOTH, expand=1)

bot_frame = Frame()
bot_frame.pack(fill=BOTH, expand=1)

daftar_nama_frame = Frame(top_frame)
daftar_nama_frame.pack(side=LEFT, fill=BOTH, expand=1, padx=15, anchor='w')

frame_1 = Frame(daftar_nama_frame)
frame_1.pack(anchor='w')

frame_2 = Frame(daftar_nama_frame, pady=10)
frame_2.pack(anchor='w')

frame_3 = Frame(daftar_nama_frame)
frame_3.pack(anchor='w')

Label(frame_1, text="Nama mahasiswa kelas pagi : ").pack(side=LEFT ,anchor='w')
Label(frame_3, text="KOTAK DEATH NOTE").pack(side=LEFT, pady=10)

display_name = Frame(top_frame)
display_name.pack(side=LEFT, fill=BOTH, expand=1)

text_d = Text(display_name, height=20, width=80, state=DISABLED)
text_d.pack()

daftar_nama = ["1. Muhammad zulfikar", "2. Meilisa keisa makalew", "3. Adam anwar", "4. Nova eko prastyo", "5. iin maharani",
"6. Naisha", "7. Moh nur arif", "8. M. nazir", "9. Diva rahma S", "10. khayza aulia","11. dita puji",
"12. Herdo dimas",
"13. tapha I",
"14. Yurna sari",
"15. Aditya pratama",
"16. Riyan anugrah",
"17. Silviyana",
"18. Jihan S",
"19. Ardifa",
"20. Fadillah A",
"21. Satriya adi F",
"22. BUDI TK",
"23. AZMA TK",
"24. ANDIKA TK",
"25. PUTRI TK",
"26. OKTAVIA TK",
"27. AGNES TK",
"28. JEREMY TK",
"29. ARVY TK",
"30. RICKY TK",
"31. RAHMADI TK",
]

cur_row = 0
cur_col = 0

for x in range(len(daftar_nama)):
	if x % 15 == 0:
		cur_row = 0
		cur_col += 1
	Label(frame_2, text=daftar_nama[x]).grid(row=cur_row, column=cur_col, sticky='w')
	cur_row += 1


tombolacak = Button(daftar_nama_frame, text="ACAK LORD", bg="black", fg="red", width=20, activebackground="black", activeforeground="yellow", relief=RAISED,bd=5,command=acak)
tombolacak.pack(anchor='w')




root.mainloop()