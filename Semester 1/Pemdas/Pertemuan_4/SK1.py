def potongan(diskon, hargaAwal, jumlahTiket):
    jumlahBeli = hargaAwal * jumlahTiket
    totalPotongan = jumlahBeli * (diskon / 100)

    return int(totalPotongan)

#Constant
SBY = 300000 #Surabaya
BL = 350000 #Bali
LMP = 500000 #Lampung
DISC = 10

print("========================")
print("JURUSAN YANG TERSEDIA")
print("------------------------")
print("SBY")
print("BL")
print("LMP")
print("========================")


#Input
print("Input nama anda\t")
nama = str(input("> "))
print("Jumlah Tiket")
jumlahTiket = int(input("> "))
print("No HP Anda")
noHP = int(input("> "))
print("Jurusan yang dituju")
jurusan = str(input("> "))

diskon = -1
# jurusanTuju = {"SBY": "Surabaya", "BL": "Bali", "LMP": "Lampung"}

if(jumlahTiket >= 3):
    if(jurusan == "SBY"):
       jurusanTuju = "SBY"
       totalHarga = SBY * jumlahTiket
       diskon = totalHarga - potongan(DISC, SBY, jumlahTiket)
    elif(jurusan == "BL"):
        jurusanTuju = "BL"
        totalHarga = BL * jumlahTiket
        diskon = totalHarga - potongan(DISC, BL, jumlahTiket)
    elif(jurusan == "LMP"):
        jurusanTuju = "LMP"
        totalHarga = LMP * jumlahTiket
        diskon = totalHarga - potongan(DISC, LMP, jumlahTiket)
    else:
        print("Jurusan tidak tersedia")
else:
    if(jurusan == "SBY"): totalHarga = SBY * jumlahTiket
    elif(jurusan == "BL"): totalHarga = BL * jumlahTiket
    elif(jurusan == "LMP"): totalHarga = LMP * jumlahTiket
    else: print("Jurusan tidak tersedia")

if(diskon != -1):
    print("STRUK PEMBAYARAN TIKET")
    print("-----------------------------")
    print("Nama\t\t\t: {}".format(nama))
    print("No. HP\t\t\t: 0{}".format(noHP))
    print("Jumlah Tiket\t\t: {} tiket".format(jumlahTiket))
    print("Jurusan yang dituju\t: {} ({})".format(jurusan, jurusanTuju))
    print("-----------------------------")
    print("SELAMAT ANDA MENDAPATKAN POTONGAN 10%")
    print("Harga sebelum Potongan\t: Rp.{}".format(totalHarga))
    print("Harga setelah Potongan\t: Rp.{}".format(diskon))
    uangBayar = int(input("Input Uang Bayar: "))
    if(uangBayar < diskon):
        print("Maaf uang anda kurang Rp.{}, tidak cukup untuk melanjutkan pembayaran".format(diskon - uangBayar))
    else:
        print("Uang Kembali Rp.{}".format(uangBayar - diskon))

else:
    print("STRUK PEMBAYARAN TIKET")
    print("-----------------------------")
    print("Nama\t\t\t: {}".format(nama))
    print("No. HP\t\t\t: 0{}".format(noHP))
    print("Jumlah Tiket\t\t: {} tiket".format(jumlahTiket))
    print("Jurusan yang dituju\t: {} ({})".format(jurusan, jurusanTuju))
    print("-----------------------------")
    print("Total yang harus anda bayarkan sebesar Rp.{}".format(totalHarga))
    uangBayar = int(input("Input Uang Bayar: "))
    if(uangBayar < totalHarga):
        print("Maaf, uang anda kurang Rp.{}, tidak cukup untuk melanjutkan pembayaran".format(totalHarga - uangBayar))
    else: 
        print("Uang Kembali Rp.{}".format(uangBayar - totalHarga))
