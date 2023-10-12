print("-" * 30)
print('PENDAFTARAN MAHASISWA BARU')
print("-" * 30)
print("Input Nama Anda")
namaMahasiwa = str(input("> "))
print("Input NIS anda")
nis = int(input("> "))
print("Input Jurusan yang diinginkan")
kodeJurusan = str(input("> "))

harga = 0
jurusan = ""

if(kodeJurusan.upper() == "SI"):
    jurusan = "Sistem Informasi"
    harga = 2400000
elif(kodeJurusan.upper() == "SIA"):
    jurusan = "Sistem Informasi Akuntansi"
    harga = 2000000
else:
    jurusan = "Kode Kaprog Salah"
    harga = 0

print("Nama Mahasiswa\t\t: {}".format(namaMahasiwa))
print("NIS\t\t\t: {}".format(nis))
print("Jurusan yang dipilih\t: {}".format(jurusan))
print("Harga yang harus dibayar: {}".format(harga))