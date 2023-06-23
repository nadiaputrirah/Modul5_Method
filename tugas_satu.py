# Metode Function
print("===== Metode Function ====")
def cek_bil(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

input_angka = int(input("Masukkan bilangan: "))
hasil_cek = cek_bil(input_angka)
print("Bilangan", input_angka, "adalah bilangan", hasil_cek)

# Metode prosedur
print("===== Metode Prosedur ====")
def cek_angka(bil):
    if bil % 2 == 0:
        print("Bilangan", bil, "adalah bilangan Genap")
    else:
        print("Bilangan", bil, "adalah bilangan Ganjil")

input_bil = int(input("Masukkan Bilangan : "))
cek_angka(input_bil)
