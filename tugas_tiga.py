# Metode Function - Penjumlahan
def penjumlahan(a, b):
    return a + b

# Metode Function - Perkalian
def perkalian(a, b):
    return a * b

# Metode Function - Pembagian
def pembagian(a, b):
    return a / b

# Metode Function - Pengurangan
def pengurangan(a, b):
    return a - b

# Metode Function - Pangkat
def pangkat(a, b):
    return a ** b

# Tampilan Menu
print("==== KALKULATOR ====")
print("1. Penjumlahan")
print("2. Perkalian")
print("3. Pembagian")
print("4. Pengurangan")
print("5. Pangkat")

# Memasukkan pilihan
pilihan = input("Masukkan pilihan: ")

# Memasukkan bilangan pertama dan kedua
bill1 = float(input("Bilangan pertama: "))
bill2 = float(input("Bilangan kedua: "))

# Menghitung hasil berdasarkan pilihan
if pilihan == '1':
    hasil = penjumlahan(bill1, bill2)
    operasi = "Penjumlahan"
elif pilihan == '2':
    hasil = perkalian(bill1, bill2)
    operasi = "Perkalian"
elif pilihan == '3':
    hasil = pembagian(bill1, bill2)
    operasi = "Pembagian"
elif pilihan == '4':
    hasil = pengurangan(bill1, bill2)
    operasi = "Pengurangan"
elif pilihan == '5':
    hasil = pangkat(bill1, bill2)
    operasi = "Pangkat"
else:
    hasil = "Pilihan tidak valid"
    operasi = "Tidak valid"

# Menampilkan hasil operasi
print("Hasil", operasi + ":", hasil)
