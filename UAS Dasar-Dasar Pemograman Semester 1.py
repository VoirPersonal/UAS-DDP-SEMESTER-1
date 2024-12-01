from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore,Style
import pwinput
import csv

kesempatan = 3

biasa = "member biasa.csv"
vip = "member vip.csv"

gems = 0

global penggunaan_vouucher
penggunaan_vouucher = 1

# menu makanan normal tanpa diskon
global bubur, nasi_kuning, pempek, siomay, martabak, terang_bulan
# menu pagi
bubur = 3
nasi_kuning = 4
soto = 3

# menu siang
pempek = 7
siomay = 5
batagor = 3

# menu malam
martabak = 5
terang_bulan = 5
pisang_bakar = 8

def waktu():
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour

    if 5 <= jam < 10:
        salam = "Selamat Pagi"
    elif 10 <= jam < 18:
        salam = "Selamat Siang"
    else:
        salam = "Selamat Malam"
    return salam

def menu_voucher_vip():
    global gems, diskon, bubur, nasi_kuning, pempek ,siomay, martabak, terang_bulan, penggunaan_vouucher
    diskon = 0
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour

    masukkan_voucher = input("Silahkan Masukkan Voucher Anda! : ")
    
    if masukkan_voucher == "PAGI123" and penggunaan_vouucher > 0 and 8 <= jam < 10:
        penggunaan_vouucher -= 1
        diskon = 2
        bubur -= diskon
        nasi_kuning -= diskon
        print(Fore.GREEN + f"\nSelamat Voucher {masukkan_voucher} Berhasil Digunakan!" + Style.RESET_ALL)
        menu_VIP()
    
    elif masukkan_voucher == "SIANG23" and penggunaan_vouucher > 0 and 10 <= jam < 18:
        penggunaan_vouucher -= 1
        diskon = 3
        pempek -= diskon
        siomay -= diskon
        print(Fore.GREEN + f"\nSelamat Voucher {masukkan_voucher} Berhasil Digunakan!" + Style.RESET_ALL)
        menu_VIP()

    elif masukkan_voucher == "MALAM14" and penggunaan_vouucher > 0  and 18 <= jam < 20:
        penggunaan_vouucher -= 1
        diskon = 4
        martabak -= diskon
        terang_bulan -= diskon
        print(Fore.GREEN + f"\nSelamat Voucher {masukkan_voucher} Berhasil Digunakan!" + Style.RESET_ALL)
        menu_VIP()

    else:
        if penggunaan_vouucher == 0:
            print(Fore.RED + "\nVoucher Telah Digunakan!" + Style.RESET_ALL)
            menu_VIP()

        print(Fore.RED + "\nMohon Maaf Kode Voucher Tidak Dapat Digunakan!" + Style.RESET_ALL)
        menu_VIP()

def menu_voucher():
    global gems, bubur, nasi_kuning, pempek ,siomay, martabak, terang_bulan, penggunaan_vouucher
    diskon = 0
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour

    masukkan_voucher = input("Silahkan Masukkan Voucher Anda! : ")
    
    if masukkan_voucher == "PAGI123" and penggunaan_vouucher > 0 and 8 <= jam < 10:
        penggunaan_vouucher -= 1
        diskon = 2
        bubur -= diskon
        nasi_kuning -= diskon
        print(Fore.GREEN + f"\nSelamat Voucher {masukkan_voucher} Berhasil Digunakan!" + Style.RESET_ALL)
        menu_user()
    
    elif masukkan_voucher == "SIANG23" and penggunaan_vouucher > 0 and 10 <= jam < 18:
        penggunaan_vouucher -= 1
        diskon = 3
        pempek -= diskon
        siomay -= diskon
        print(Fore.GREEN + f"\nSelamat Voucher {masukkan_voucher} Berhasil Digunakan!" + Style.RESET_ALL)
        menu_user()

    elif masukkan_voucher == "MALAM14" and penggunaan_vouucher > 0  and 18 <= jam < 20:
        penggunaan_vouucher -= 1
        diskon = 4
        martabak -= diskon
        terang_bulan -= diskon
        print(Fore.GREEN + f"\nSelamat Voucher {masukkan_voucher} Berhasil Digunakan!" + Style.RESET_ALL)
        menu_user()

    else:
        if penggunaan_vouucher == 0:
            print(Fore.RED + "\nVoucher Telah Digunakan!" + Style.RESET_ALL)
            menu_user()

        print(Fore.RED + "\nMohon Maaf Kode Voucher Tidak Dapat Digunakan!" + Style.RESET_ALL)
        menu_user()

def menu_isi_gems():
    global gems
    try:
        nominal = int(input("\nSilahkan Masukkan Nominal Gems Yang Diinginkan : "))
        min = 1
        max = 100000
        if nominal <= min:
            print(Fore.RED + "\nMohon Maaf Nominal Terlalu Kecil" + Style.RESET_ALL)
            menu_isi_gems()
        elif nominal >= max:
            print(Fore.RED + "\nMohon Maaf Nominal Terlalu Besar" + Style.RESET_ALL)
            menu_isi_gems()
        else:
            gems += nominal
            print(Fore.GREEN + "\nGems Berhasil Di Isi!" + Style.RESET_ALL)
            menu_user()
    except ValueError:
        print(Fore.RED + "Silahkan masukan angka!" + Style.RESET_ALL)
        menu_isi_gems()

def menu_isi_gems_VIP():
    global gems
    try:
        nominal = int(input("\nSilahkan Masukkan Nominal Gems Yang Diinginkan : "))
        min = 1
        max = 100000
        if nominal <= min:
            print(Fore.RED + "\nMohon Maaf Nominal Terlalu Kecil" + Style.RESET_ALL)
            menu_isi_gems()
        elif nominal >= max:
            print(Fore.RED + "\nMohon Maaf Nominal Terlalu Besar" + Style.RESET_ALL)
            menu_isi_gems()
        else:
            gems += nominal
            print(Fore.GREEN + "\nGems Berhasil Di Isi!" + Style.RESET_ALL)
            menu_VIP()
    except ValueError:
        print(Fore.RED + "Silahkan masukan angka!" + Style.RESET_ALL)
        menu_isi_gems()

def menu_beli_makan():
    global gems
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour

    if 8 <= jam < 10:
        pagi = "Pagi"
        menu_pagi = [("1","Bubur Ayam",bubur),("2","Nasi Kuning",nasi_kuning)]
        print(Fore.BLUE + f"\nMenu untuk {pagi} ini 🍀")
        print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)

        tabel_pagi = PrettyTable()
        tabel_pagi.field_names = ["No","Makanan","Harga"]
        for makanan in menu_pagi:
            tabel_pagi.add_row(makanan)
        tabel_pagi.add_row(["3", "Keluar", "-"])
        print(tabel_pagi)
        try:
            pilihan = int(input("\nSilahkan Pilih (1/2/3) : "))
        except ValueError:
            print(Fore.RED + "Pilihan Tidak Ada!" + Style.RESET_ALL)
        if pilihan == 1 and gems >= 4:
            gems -= bubur
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Bubur!" + Style.RESET_ALL)
            menu_beli_makan()
        elif pilihan == 2 and gems >= 4:
            gems -= nasi_kuning
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Nasi Kuning!" + Style.RESET_ALL)
            menu_beli_makan()
        elif pilihan == 3:
            print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
            menu_user()
        else:
            print(Fore.RED + "\nPilihan Tidak Valid atau Gems Kurang!" + Style.RESET_ALL)
            menu_beli_makan()

    elif 10 <= jam < 18:
        siang= "Siang"
        menu_siang = [("1","Pempek",pempek),("2","Siomay",siomay)]
        print(Fore.BLUE + f"\nMenu untuk {siang} ini ☀️")
        print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)

        tabel_siang = PrettyTable()
        tabel_siang.field_names = ["No","Makanan","Harga"]
        for makanan in menu_siang:
            tabel_siang.add_row(makanan)
        tabel_siang.add_row(["3", "Keluar", "-"])
        print(tabel_siang)
        try:
            pilihan = int(input("\nSilahkan Pilih (1/2/3) : "))
        except ValueError:
            print(Fore.RED + "Pilihan Tidak Ada!" + Style.RESET_ALL)
        if pilihan == 1 and gems >= 7:
            gems -= pempek
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Pempek!" + Style.RESET_ALL)
            menu_beli_makan()
        elif pilihan == 2 and gems >= 5:
            gems -= siomay
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Siomay!" + Style.RESET_ALL)
            menu_beli_makan()
        elif pilihan == 3:
            print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
            menu_user()
        else:
            print(Fore.RED + "\nPilihan Tidak Valid atau Gems Kurang!" + Style.RESET_ALL)
            menu_beli_makan()

    elif 18 <= jam < 20:
        malam= "Malam"
        menu_malam = [("1","Martabak",martabak),("2","Terang Bulan",terang_bulan)]
        print(Fore.BLUE + f"\nMenu untuk {malam} ini 🌙")
        print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)

        tabel_malam = PrettyTable()
        tabel_malam.field_names = ["No","Makanan","Harga"]
        for makanan in menu_malam:
            tabel_malam.add_row(makanan)
        tabel_malam.add_row(["3", "Keluar", "-"])
        print(tabel_malam)
        try:
            pilihan = int(input("\nSilahkan Pilih (1/2/3) : "))
        except ValueError:
            print(Fore.RED + "Pilihan Tidak Ada!" + Style.RESET_ALL)
        if pilihan == 1 and gems >= 5:
            gems -= martabak
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Martabak!" + Style.RESET_ALL)
            menu_beli_makan()
        elif pilihan == 2 and gems >= 6:
            gems -= terang_bulan
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Terang Bulan!" + Style.RESET_ALL)
            menu_beli_makan()
        elif pilihan == 3:
            print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
            menu_user()
        else:
            print(Fore.RED + "\nPilihan Tidak Valid atau Gems Kurang!" + Style.RESET_ALL)
            menu_beli_makan()
    else:
        print(Fore.BLUE + "Mohon Maaf Toko Kami Sedang Tutup 🙏" + Style.RESET_ALL)
        menu_user()

def menu_beli_makan_vip():
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour
    global gems

    if 8 <= jam < 10:
        pagi = "Pagi"
        menu_pagi = [("1","Bubur Ayam",bubur),("2","Nasi Kuning",nasi_kuning),("3","Soto",soto)]
        print(Fore.BLUE + f"\nMenu untuk {pagi} ini 🍀")
        print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)

        tabel_pagi = PrettyTable()
        tabel_pagi.field_names = ["No","Makanan","Harga"]
        for makanan in menu_pagi:
            tabel_pagi.add_row(makanan)
        tabel_pagi.add_row(["4", "Keluar", "-"])
        print(tabel_pagi)
        try:
            pilihan = int(input("Silahkan Pilih (1/2/3/4) : "))
        except ValueError:
            print(Fore.RED + "Pilihan Tidak Ada!" + Style.RESET_ALL)

        if pilihan == 1 and gems >= 4:
            gems -= bubur
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Bubur!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 2 and gems >= 4:
            gems -= nasi_kuning
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Nasi Kuning!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 3 and gems >= 4:
            gems -= soto
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Soto!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 4:
            print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
            menu_VIP()
        else:
            print(Fore.RED + "\nPilihan Tidak Valid atau Gems Kurang!" + Style.RESET_ALL)
            menu_beli_makan_vip()

    elif 10 <= jam < 18:
        siang= "Siang"
        menu_siang = [("1","Pempek",pempek),("2","Siomay",siomay),("4","Batagor",batagor)]
        print(Fore.BLUE + f"\nMenu untuk {siang} ini ☀️")
        print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)

        tabel_siang = PrettyTable()
        tabel_siang.field_names = ["No","Makanan","Harga"]
        for makanan in menu_siang:
            tabel_siang.add_row(makanan)
        tabel_siang.add_row(["4", "Keluar", "-"])
        print(tabel_siang)
        try:
            pilihan = int(input("Silahkan Pilih (1/2/3/4) : "))
        except ValueError:
            print(Fore.RED + "Pilihan Tidak Ada!" + Style.RESET_ALL)

        if pilihan == 1 and gems >= 7:
            gems -= pempek
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Pempek!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 2 and gems >= 5:
            gems -= siomay
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Siomay!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 3 and gems >= 3:
            gems -= batagor
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Batagor!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 4:
            print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
            menu_VIP()
        else:
            print(Fore.RED + "\nPilihan Tidak Valid atau Gems Kurang!" + Style.RESET_ALL)
            menu_beli_makan_vip()

    elif 18 <= jam < 20:
        malam= "Malam"
        menu_malam = [("1","Martabak",martabak),("2","Terang Bulan",terang_bulan),("3","Pisang Bakar",pisang_bakar)]
        print(Fore.BLUE + f"\nMenu untuk {malam} ini 🌙")
        print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)

        tabel_malam = PrettyTable()
        tabel_malam.field_names = ["No","Makanan","Harga"]
        for makanan in menu_malam:
            tabel_malam.add_row(makanan)
        tabel_malam.add_row(["4", "Keluar", "-"])
        print(tabel_malam)
        try:
            pilihan = int(input("Silahkan Pilih (1/2/3/4) : "))
        except ValueError:
            print(Fore.RED + "Pilihan Tidak Ada!" + Style.RESET_ALL)
        
        if pilihan == 1 and gems >= 5:
            gems -= martabak
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Martabak!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 2 and gems >= 6:
            gems -= terang_bulan
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Terang Bulan!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 3 and gems >= 4:
            gems -= pisang_bakar
            print(Fore.GREEN + "\nSelamat Anda Telah Membeli Pisang Bakar!" + Style.RESET_ALL)
            menu_beli_makan_vip()
        elif pilihan == 4:
            print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
            menu_VIP()
        else:
            print(Fore.RED + "\nPilihan Tidak Valid atau Gems Kurang!" + Style.RESET_ALL)
            menu_beli_makan_vip()
    else:
        print(Fore.BLUE + "Mohon Maaf Toko Kami Sedang Tutup 🙏" + Style.RESET_ALL)
        menu_VIP()

def menu_user():
    print (Fore.LIGHTMAGENTA_EX + f"\nHalo, {waktu()}")
    print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)
    print ("\n[1] Beli Makanan")
    print ("[2] Isi Gems")
    print ("[3] Voucher")
    print ("[4] Keluar")
    pilihan = int(input("Silahkan Pilih (1/2/3/4) : "))

    if pilihan == 1:
        menu_beli_makan()
    elif pilihan == 2:
        menu_isi_gems()
    elif pilihan == 3:
        menu_voucher()
    elif pilihan == 4:
        print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
        menu_login()
    else:
        print(Fore.RED + "Pilihan Tidak Valid" + Style.RESET_ALL)
        menu_user()

def menu_VIP():
    print (Fore.LIGHTMAGENTA_EX + f"\nHalo, {waktu()}")
    print (f"Gems Anda Sekarang adalah {gems}" + Style.RESET_ALL)
    print ("\n[1] Beli Makanan")
    print ("[2] Isi Gems")
    print ("[3] Voucher")
    print ("[4] Keluar")
    pilihan = int(input("Silahkan Pilih (1/2/3) : "))

    if pilihan == 1:
        menu_beli_makan_vip()
    elif pilihan == 2:
        menu_isi_gems_VIP()
    elif pilihan == 3:
        menu_voucher()
    elif pilihan == 4:
        print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
        menu_login()
    else:
        print(Fore.RED + "Pilihan Tidak Valid" + Style.RESET_ALL)
        menu_VIP()

def menu_login_user():
    global kesempatan
    while kesempatan > 0:
        global username
        username = input("\nSilahkan Masukkan Username Anda! : ")
        password = pwinput.pwinput(prompt = "Silahkan Masukkan Password Anda! : ")

        found = False

        with open (biasa, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for user in csv_reader:
                if user ["username"] == username and user ["password"] == password:
                    found = True
                    menu_user()

            if not found:
                if kesempatan == 0:
                    exit()

                kesempatan -= 1
                print(Fore.RED + f"Username Atau Password Tidak Sesuai. Sisa {kesempatan} Percobaan!" + Style.RESET_ALL)
                menu_login_user()
        break

def menu_login_VIP():
    global kesempatan
    while kesempatan > 0:
        global username_vip
        username_vip = input("\nSilahkan Masukkan Username Anda! : ")
        password_vip = pwinput.pwinput(prompt="Silahkan Masukkan Password Anda! : ")

        found = False

        with open (vip, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for user in csv_reader:
                if user ["username"] == username_vip and user ["password"] == password_vip:
                    found = True
                    menu_VIP()

            if not found:
                if kesempatan == 0:
                    exit

                kesempatan -= 1
                print(Fore.RED + f"Username Atau Password Tidak Sesuai. Sisa {kesempatan} Percobaan!" + Style.RESET_ALL)
                menu_login_VIP()
        break

def menu_login():
    print("\n[1] VIP")
    print("[2] Biasa")
    print("[3] Keluar")
    jenis_user = int(input("Silahkan Pilih! (1/2/3) : "))
    if jenis_user == 1:
        menu_login_VIP()
    elif jenis_user == 2:
        menu_login_user()
    elif jenis_user == 3:
        print(Fore.LIGHTBLUE_EX + "\nBaiklah!" + Style.RESET_ALL)
        exit()
    else:
        print(Fore.RED + "Pilihan Tidak Valid!" + Style.RESET_ALL )
        menu_login()
menu_login()
