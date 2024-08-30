import mysql.connector
import time
import belajar as bj


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password  = "",
    database = "pythondb"    
)





cursor =  mydb.cursor()


#insert username dan password
def insertdata(username, password) :
    x = ["process insert data", "." , ".", "."]
    sql = f"INSERT INTO user set username = '{username}', password = '{password}'"
    cursor.execute(sql)
    mydb.commit()
    
    for z in x :
        print(z, end=" ", flush=True)
        time.sleep(1)
    
    time.sleep(1)
    print("\n")
    print("1\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("3\n")
    print(cursor.rowcount, "berhasil insert data")
    

#cek semua record
def cekalldata(user) :

    sql =  f"SELECT id_user, username, password FROM {user}"
    cursor.execute(sql)

    getall = cursor.fetchall()

    for x in getall :
        print(x)


#cek record tertentu
def cekid(id):
    z = str(id)
    sql = f"SELECT username, password FROM user WHERE id_user = '{z}'"
    cursor.execute(sql)
    getall = cursor.fetchall()
    
    for x in getall :
        print(x)

def cekusername(username):
    sql = f"SELECT username, password FROM user WHERE username = '{username}'"
    cursor.execute(sql)
    getall = cursor.fetchall()
    
    for x in getall :
        print(x)
        

#urutan

def urut(order):
    z = order
    x =  z.lower()
    sql =  f"SELECT username, password FROM user ORDER BY {x}"
    cursor.execute(sql)
    getall = cursor.fetchall()
    
    for f in getall :
        print(f)
        

        

#panggil insert data
#insertdata("zul", "zul123")

#cek semua data 
#cekalldata("user")

#cek berdasarkan id
#cekid(1)
#cekusername("herdo")

#urutan
#urut("id_user")