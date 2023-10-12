def persen(gajiPokok, bonusPersen):
    return gajiPokok * (bonusPersen / 100)

def tunjanganJabatan(gajiPokok, golongan):
    if(golongan == 1): return persen(gajiPokok, 5)
    elif(golongan == 2): return persen(gajiPokok, 10)
    elif(golongan == 3): return  persen(gajiPokok, 15)

def tunjanganPendidikan(gajiPokok, jenjang):
    jenjang = jenjang.upper()

    if(jenjang == "SMA"): return persen(gajiPokok, 2.5)
    elif(jenjang == "D1"): return persen(gajiPokok, 5)
    elif(jenjang == "D3"): return persen(gajiPokok, 20)
    elif(jenjang == "S1"): return persen(gajiPokok, 30)

def honorLembur(jamTerbang):
    uangLembur = 0

    if(jamTerbang > 8):
        for x in range(jamTerbang):
            uangLembur += 3500

    return uangLembur

def totalGajiAkhir(gajiPokok, jabatan, pendidikan, lembur):
    return gajiPokok + jabatan + pendidikan + lembur

GAJIPOKOK = 300000

print("=" * 20)
print("PROGRAM HITUNG GAJI KARYAWAN")
print("=" * 20)
namaKaryawan = str(input("Nama Karyawan\t\t: "))
golonganJabatan = int(input("Golongan Jabatan\t: "))
jenjangPendidikan = str(input("Jenjang Pendidikan\t: "))
totalJamKerja = int(input("Total Jam Kerja\t\t: "))
print("-" * 20)

#Proses Hitung tunjangan
tunjanganJabatan = tunjanganJabatan(GAJIPOKOK, golonganJabatan)
tunjanganPendidikan = tunjanganPendidikan(GAJIPOKOK, jenjangPendidikan)
honorLembur = honorLembur(totalJamKerja)
totalGajiAkhir = totalGajiAkhir(GAJIPOKOK, tunjanganJabatan, tunjanganPendidikan, honorLembur)

print("Karyawan yang bernama {}".format(namaKaryawan))
print("Honor yang diterima: ")
print("\tTunjangan Jabatan\t: {}".format(tunjanganJabatan))
print("\tTunjangan Pendidikan\t: {}".format(tunjanganPendidikan))
print("\tHonor Lembur\t\t: {}".format(honorLembur))
print("\tGaji Pokok\t\t: {}".format(GAJIPOKOK))
print("-" * 50, "+")
print("Total Gaji yang diterima\t: Rp.{}".format(totalGajiAkhir))