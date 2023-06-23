#function
def hitung_luas_persegi(sisi):
    hasil = sisi*sisi
    return hasil

print("Luas persegi: %d" %hitung_luas_persegi(10))

#prosedur
def hitung_luas_segitiga(alas,tinggi):
    hasil = (alas * tinggi) / 2
    print("Luas segitiga: %d" %hasil)

hitung_luas_segitiga(10,5)

#parameter
# def fungsi(parameter):
#     print parameter

#parameter
def salam(ucapan):
    print (ucapan)  
#fungsi
salam("halo, selamat pagi!")

#parameter 2
def luas_segitiga(alas,tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)
#masukkan fungsi
luas_segitiga(2,2)
