# luas dan keliling dari persegi
# method function
def hitung_luas(sisi):
    return sisi * 2

def hitung_keliling(sisi):
    return sisi * 4

sisi = int(input("Masukkan panjang sisi persegi: "))

luas = hitung_luas(sisi)
keliling = hitung_keliling(sisi)

print("Luas persegi:", luas)
print("Keliling persegi:", keliling)

# method prosedur
def keliling_luas_persegi(sisi):
    keliling = 4 *sisi
    luas = sisi * sisi
    print("Keliling persegi: %d" %keliling)
    print("Luas persegi: %d" %luas)

panjang = int(input("Masukkan panjang sisi persegi: "))
keliling_luas_persegi(panjang)

# perbandingan bilangan
def banding(nilai1, nilai2):
    if (nilai1 > nilai2):
        print(nilai1)
    elif (nilai1 == nilai2):
        print("Tidak ada")
    else:
        print(nilai2)

bil1 = int(input("masukkan bilangan 1: "))
bil2= int(input("masukkan bilangan 2: "))
print("bilangan yang lebih besar adalah ")
banding(bil1, bil2)