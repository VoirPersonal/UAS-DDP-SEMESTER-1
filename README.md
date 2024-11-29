# Ujian Akhir Semester Dasar-Dasar Pemograman Semester 1

<p> Selamat datang di proyek Toko Makanan Dengan Waktu! 🎉 <br>
Ini adalah sebuah aplikasi sederhana yang memungkinkan pengguna untuk membeli makanan dengan menggunakan sistem gems dan voucher diskon.  Aplikasi ini dirancang untuk memberikan pengalaman berbelanja yang menyenangkan, tergantung pada waktu.

# Fitur-Fitur 🕹️
#### 1. Sistem Gems
   - Pengguna dapat mengisi saldo gems mereka dan menggunakannya untuk membeli makanan.
   - Setiap menu makanan memiliki harga dalam gems, jadi pastikan kamu punya cukup sebelum membeli!.
#### 2. Menu Berdasarkan Waktu
   - Terdapat menu yang berbeda untuk pagi, siang, dan malam. Misalnya, di pagi hari kamu bisa membeli Bubur Ayam atau Nasi Kuning, sedangkan di malam hari ada Martabak dan Terang Bulan.
#### 3. Penggunaan Voucher Diskon
   - Pengguna dapat memasukkan kode voucher untuk mendapatkan diskon pada menu tertentu, tergantung pada waktu.
   - Misalnya, jika kamu memasukkan voucher "PAGI123" di pagi hari, kamu akan mendapatkan diskon untuk menu sarapan.
#### 4. Login Untuk Pengguna Biasa dan VIP
   - Ada dua jenis pengguna: biasa dan VIP. Pengguna VIP memiliki akses ke menu yang lebih eksklusif dan mungkin mendapatkan lebih banyak keuntungan.

# Cara Menggunakan 🔧
   - Saat aplikasi dijalankan, kamu akan diminta untuk login menggunakan username dan password.
   - Setelah berhasil login, pilih menu yang ingin digunakan:
        - Beli Makanan
        - Isi Gems
        - Gunakan Voucher
   - Ikuti instruksi di layar untuk melakukan pembelian atau mengisi saldo gems.
# Penjelesan Baris Kode 📃
``` python
from datetime import datetime
from colorama import Fore, Style
import csv
```
- datetime: Digunakan untuk mendapatkan waktu saat ini (jam, tanggal).
- colorama: Menambahkan warna pada output di terminal.
- csv: Untuk membaca dan menulis file CSV, seperti data pengguna.

``` python
  kesempatan = 3
biasa = "member biasa.csv"
vip = "member vip.csv"
gems = 0
```
- kesempatan: Jumlah kesempatan login pengguna (default 3 kali).
- biasa dan vip: Nama file CSV yang menyimpan data pengguna untuk tipe pengguna biasa dan VIP.
- gems: Menyimpan saldo pengguna, default-nya adalah 0.

```python
global penggunaan_vouucher
penggunaan_vouucher = 1
```
- penggunaan_vouucher: Menyimpan status apakah voucher sudah digunakan (1: belum, 0: sudah).

```python
global bubur, nasi_kuning, pempek, siomay, martabak, terang_bulan
```
- Deklarasi Menu dan Harga:
  #### 1.  Menu pagi:
    - Bubur (3 gems)
    - Nasi Kuning (4 gems)
    - Soto (3 gems)
  #### 2. Menu siang:
    -  Pempek (7 gems)
    -  Siomay (5 gems)
    -  Batagor (3 gems)
  #### 3. Menu malam:
    -  Martabak (5 gems)
    -  Terang Bulan (5 gems)
    -  Pisang Bakar (4 gems)
 
```python
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
```
- Menentukan salam kepada user sesuai dengan waktu real-time

```python
def menu_voucher():
    global gems, penggunaan_vouucher, bubur, nasi_kuning, pempek, siomay, martabak, terang_bulan
    masukkan_voucher = input("Silahkan Masukkan Voucher Anda! : ")
```
- Pengguna memasukkan kode voucher.

```pyhton
    if masukkan_voucher == "PAGI123" and penggunaan_vouucher > 0 and 5 <= jam < 10:
        penggunaan_vouucher -= 1
        diskon = 2
        bubur -= diskon
        nasi_kuning -= diskon
```
- Memvalidasi voucher pagi (PAGI123), mengurangi 2 gems dari menu pagi, dan menandai voucher telah digunakan.

```python
    elif masukkan_voucher == "SIANG23" and penggunaan_vouucher > 0 and 10 <= jam < 18:
        ...
```
- Sama seperti di atas, tetapi berlaku untuk voucher siang (SIANG23).

```python
    elif masukkan_voucher == "MALAM14" and penggunaan_vouucher > 0  and 18 <= jam < 20:
        ...
```
- Sama seperti di atas, tetapi untuk voucher malam (MALAM14).

```python
def menu_isi_gems():
    nominal = int(input("\nSilahkan Masukkan Nominal Gems Yang Diinginkan : "))
    if nominal <= 1:
        print(Fore.RED + "\nMohon Maaf Nominal Terlalu Kecil" + Style.RESET_ALL)
    elif nominal >= 100000:
        print(Fore.RED + "\nMohon Maaf Nominal Terlalu Besar" + Style.RESET_ALL)
    else:
        gems += nominal
        print(Fore.GREEN + "\nGems Berhasil Di Isi!" + Style.RESET_ALL)
```
- Pengguna memasukkan nominal gems yang ingin ditambahkan (maksimal 100.000).

```python
def menu_beli_makan():
    waktu_sekarang = datetime.now()
    jam = waktu_sekarang.hour

    if 5 <= jam < 10:
        print(f"\nMenu untuk Pagi ini 🍀")
        print(f"[1] Bubur Ayam, {bubur} Gems")
        print(f"[2] Nasi Kuning, {nasi_kuning} Gems")
    ...
```
- Menampilkan menu berdasarkan waktu (pagi, siang, malam).
- Pengguna memilih menu dan memastikan gems mencukupi sebelum membeli.

```python
def menu_login_user():
    global kesempatan
    while kesempatan > 0:
        username = input("\nMasukkan Username Anda! : ")
        password = input("Masukkan Password Anda! : ")

        with open(biasa, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for user in csv_reader:
                if user["username"] == username and user["password"] == password:
                    menu_user()
```
- Memvalidasi login dengan mencocokkan username dan password dari file CSV.

```python
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
```
- Memilih tipe pengguna (VIP/Biasa) atau keluar dari program.
- Untuk VIP memiliki tambahan menu.
