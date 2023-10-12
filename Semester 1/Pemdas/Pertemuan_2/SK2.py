def totalAkhir(harga, total):
    return harga * total

print("PROGRAM PENJUALAN BARANG")
print("-------------------------")
codeBarang = str(input("Input Kode Barang: "))
namaBarang = str(input("Input Nama Barang: "))
hargaBarang = int(input("Input Harga Barang: "))
totalBeli = int(input("Input Barang yang dibeli: "))

# totalAkhir = hargaBarang * totalBeli

print("STRUK PEMBAYARAN BARANG")
print("------------------------")
print("Kode Barang\t: {}".format(codeBarang))
print("Nama Barang\t: {}".format(namaBarang))
print("Harga Barang\t: Rp.{}".format(hargaBarang))
print("JUmlah Barang\t: {}".format(totalBeli))
print("-------------------------")
print("Total Harga\t: {}".format(totalAkhir(hargaBarang, totalBeli)))