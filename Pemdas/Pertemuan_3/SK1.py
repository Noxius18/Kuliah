def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

print("PERHITUNGAN SEDERHANA")
print("-----------------------")
a = int(input("Input Nilai A: "))
b = int(input("Input Nilai B: "))
print("------------------------")

#Proses
"""
c = a + b
d = a - b
"""

print("HASIL PERHITUNGAN")
print("-------------------")
print("{} + {} = {}".format(a, b, tambah(a, b)))
print("{} - {} = {}".format(a, b, kurang(a, b)))
print("{} * {} = {}".format(a, b, kali(a, b)))
print("-------------------")