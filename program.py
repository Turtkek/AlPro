import mysql.connector
import matplotlib.pyplot as plt
import os

# Bagian ini untuk menghubungkan program ke DATABASE
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="login"
)


# Sebuah Fungsi Untuk Membel Diamond ML
def ml():
    while True:
        os.system("cls")
        print("="*40)
        print("Top Up Diamond Mobile legend")
        print("="*40)
        print("Masukkan User & Id")
        User = input("Masukkan Username ID : ")
        Id = int(input("Masukkan ID Server : "))
        print("="*40)

        print("Pilih Nomial Top Up")
        print("="*40)
        dm =int(input("Masukkan Jumlah Diamond Yang Ingin di Top Up : "))
        harga = 300
        total = harga * dm

        print("-"*40)
        print("Pilih Metode Pembayaran")
        print("1. OVO")
        print("2. Virtual Account")
        print("3. GoPay")
        print("-"*40)
        pilih = input("Pilih Metode Pembayaran : ")

        if pilih == "1":
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID         :{User} ({Id})")
            print(f"DIAMOND yang Dibeli : {dm}")
            print(f"Total Harga         : Rp.{total}")
            print(f"Metode Pembayaran   : OVO")
            print(f"Status Pembayaran   : Belum Dibayar")
            print("-"*40)
            os.system("pause")
            bayar = input("Masukkan Nominal Pembayaran : ")
            print("\n")
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID                 : {User} ({Id})")
            print(f"DIAMOND yang Dibeli         : {dm}")
            print(f"Total Harga                 : Rp.{total}")
            print(f"Nominal Yang Anda Bayarkan  : Rp.{bayar}")
            print(f"Metode Pembayaran           : OVO")
            print(f"Status Pembayaran           : Sudah Di Bayar")
            print("-"*40)
        elif pilihan == "2":
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID         :{User} ({Id})")
            print(f"DIAMOND yang Dibeli : {dm}")
            print(f"Total Harga         : Rp.{total}")
            print(f"Metode Pembayaran   : VA")
            print(f"Status Pembayaran   : Belum Dibayar")
            print("-"*40)
            os.system("pause")
            bayar = input("Masukkan Nominal Pembayaran : ")
            print("\n")
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID                 :{User} ({Id})")
            print(f"DIAMOND yang Dibeli         : {dm}")
            print(f"Total Harga                 : Rp.{total}")
            print(f"Nominal Yang Anda Bayarkan  : Rp.{bayar}")
            print(f"Metode Pembayaran           : VA")
            print(f"Status Pembayaran           : Sudah Di Bayar")
            print("-"*40)
        elif pilihan == "3":
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID         :{User} ({Id})")
            print(f"DIAMOND yang Dibeli : {dm}")
            print(f"Total Harga         : Rp.{total}")
            print(f"Metode Pembayaran   : GoPay")
            print(f"Status Pembayaran   : Belum Dibayar")
            print("-"*40)
            os.system("pause")
            bayar = input("Masukkan Nominal Pembayaran : ")
            print("\n")
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID                 :{User} ({Id})")
            print(f"DIAMOND yang Dibeli         : {dm}")
            print(f"Total Harga                 : Rp.{total}")
            print(f"Nominal Yang Anda Bayarkan  : Rp.{bayar}")
            print(f"Metode Pembayaran           : Gopay")
            print(f"Status Pembayaran           : Sudah Di Bayar")
            print("-"*40)
        else:
            print("pilihan Tidak ada")

        pilihan = input("Mau Pesan lagi :) y/t :")
        if pilihan == "y":
            continue
        elif pilihan == "t":
            print("Terima Kasih sudah Top Up :)")
            menu()
        else:
            print("Tidak Ada Pilihan")
            break




def ff():
    while True:
        os.system("cls")
        print("="*40)
        print("Top Up Diamond Free Fire")
        print("="*40,"\n")
        print("Masukkan User & Id")
        User = input("Masukkan USERNAME : ")
        Id = int(input("Masukkan ID : "))

        print("="*40)
        print("Pilih Nomial Top Up")
        print("="*40)
        dm =int(input("Masukkan Jumlah Diamond Yang Ingin di Top Up : "))
        harga = 200
        total = harga * dm

        print("-"*40)
        print("Pilih Metode Pembayaran")
        print("1. OVO")
        print("2. Virtual Account")
        print("3. GoPay")
        print("-"*40)
        pilih = input("Pilih Metode Pembayaran : ")

        if pilih == "1":
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID         :{User} ({Id})")
            print(f"DIAMOND yang Dibeli : {dm}")
            print(f"Total Harga         : Rp.{total}")
            print(f"Metode Pembayaran   : OVO")
            print(f"Status Pembayaran   : Belum Dibayar")
            print("-"*40)
            os.system("pause")
            bayar = input("Masukkan Nominal Pembayaran : ")
            print("\n")
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID                 :{User} ({Id})")
            print(f"DIAMOND yang Dibeli         : {dm}")
            print(f"Total Harga                 : Rp.{total}")
            print(f"Nominal Yang Anda Bayarkan  : Rp.{bayar}")
            print(f"Metode Pembayaran           : OVO")
            print(f"Status Pembayaran           : Sudah Di Bayar")
            print("-"*40)
        elif pilihan == "2":
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID         :{User} ({Id})")
            print(f"DIAMOND yang Dibeli : {dm}")
            print(f"Total Harga         : Rp.{total}")
            print(f"Metode Pembayaran   : VA")
            print(f"Status Pembayaran   : Belum Dibayar")
            print("-"*40)
            os.system("pause")
            bayar = input("Masukkan Nominal Pembayaran : ")
            print("\n")
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID                 :{User} ({Id})")
            print(f"DIAMOND yang Dibeli         : {dm}")
            print(f"Total Harga                 : Rp.{total}")
            print(f"Nominal Yang Anda Bayarkan  : Rp.{bayar}")
            print(f"Metode Pembayaran           : VA")
            print(f"Status Pembayaran           : Sudah Di Bayar")
            print("-"*40)
        elif pilihan == "3":
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID         :{User} ({Id})")
            print(f"DIAMOND yang Dibeli : {dm}")
            print(f"Total Harga         : Rp.{total}")
            print(f"Metode Pembayaran   : GoPay")
            print(f"Status Pembayaran   : Belum Dibayar")
            print("-"*40)
            os.system("pause")
            bayar = input("Masukkan Nominal Pembayaran : ")
            print("\n")
            print("-"*40)
            print("\t","IN SPACE Top Up\n")
            print("PESANAN ANDA :\n")
            print(f"Username ID                 :{User} ({Id})")
            print(f"DIAMOND yang Dibeli         : {dm}")
            print(f"Total Harga                 : Rp.{total}")
            print(f"Nominal Yang Anda Bayarkan  : Rp.{bayar}")
            print(f"Metode Pembayaran           : GoPay")
            print(f"Status Pembayaran           : Sudah Di Bayar")
            print("-"*40)
        else:
            print("pilihan Tidak ada")

        pilihan = input("Mau Pesan lagi :) y/t :")
        if pilihan == "y":
            continue
        elif pilihan == "t":
            print("\nTerima Kasih sudah Top Up :)")
            menu()
        else:
            print("Tidak Ada Pilihan")
            break


def menu():
    print("="*40)
    print("Mau Top Up Apa Hari Ini")
    print("="*40)
    print("="*60,"\n")
    print("1. Diamond Mobile Legend")
    print("2. Diamond Free Fire")
    print("3. Lihat Perbandingan Rating IN Space Top Up")
    print("4. Kembali Ke Menu")
    print("="*60)


    while True:
        pilihan = input("Masukkan Pilihan: ")
        if pilihan == "1":
            ml()
        elif pilihan == "2":
            ff()
        elif pilihan == "3":
            rating()
        elif pilihan == "4":
            menu_login()
        else:
            print("pilihan Tidak Ada :x ")

def daftar():
    os.system("cls")
    print("="*40)
    print("Buat Username & Password")
    print("="*40,"\n")
    mycursor = mydb.cursor()
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    val = (username,password)
    sql = "INSERT INTO login (Username,Password) Values (%s,%s)"
    mycursor.execute(sql,val)
  
    mydb.commit()

    print("{} data ditambahkan".format(mycursor.rowcount))
    menu_login()


def login():
    print("\n")
    print("="*40)
    print("Masukkan Username & Passwor Anda Untuk Login")
    print("="*40)
    mycursor = mydb.cursor()
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    val = (username,password)
    sql = "SELECT * FROM login WHERE username = %s AND password = %s"
    mycursor.execute(sql,val)
    validasi = mycursor.fetchone()
    if  validasi is None:
        print('Username atau kata sandi salah')
        print('Tolong Periksa Username Dan Kata Sandi Anda\n')
        login()
    else:
        print('='*40)
        print('Selamat datang, ' + username,)
        print('='*40,"\n")
        menu()


def menu_login():
    os.system("cls")
    print("Selamat Datang Di IN SPACE Top Up")
    print("="*40)
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Keluar")
    print("="*40)
    
    while True:
        pilihan = input("Masukkan Pilihan: ",)
        print("="*40)
        print("\n")
        if pilihan == "1":
            login()
        elif pilihan == "2":
            daftar()
        elif pilihan == "3":
            print("="*50)
            print("Terima Kasih sudah Top Up Di IN SPACE Top Up :)")
            print("="*50)
            exit()
        else:
            print("pilihan Tidak Ada :x ")


def rating():
    tempat = ["CodaShop","UniPin","Dunia Games","IN SPACE Top Up","ItemKu"]
    rating =[3,4,3,5,2]


    fig = plt.figure(figsize=(6,6))
    ax = plt.axes()
    ax.pie(rating, labels = tempat, autopct='%1.0f%%',) 
    ax.set_title("Perbandingan Tempat Top Up Indonesia")
    plt.legend(title = "Tempat")
    plt.show()


if __name__ == '__main__':
    menu_login()