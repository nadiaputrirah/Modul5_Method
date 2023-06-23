import math

# Metode Procedure
print("==== Metode Prosedur ====")
def hitung_luas_keliling_lingkaran(jari_jari):
    luas = math.pi * jari_jari * jari_jari
    keliling = 2 * math.pi * jari_jari

    lb = round(luas, 1)
    kb = round(keliling, 1)

    print("Luas lingkaran:", lb)
    print("Keliling lingkaran:", kb)

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

hitung_luas_keliling_lingkaran(jari_jari)


# Metode Function
print("==== Metode Function ====")
def hitung_lingkaran(jari_jari):
    luas = math.pi * jari_jari * jari_jari
    keliling = 2 * math.pi * jari_jari

    lb = round(luas, 1)
    kb = round(keliling, 1)

    return lb, kb

# Input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Panggil metode function
luas, keliling = hitung_lingkaran(jari_jari)

print("Keliling lingkaran:", keliling)
print("Luas lingkaran:", luas)

