print("Latihan Komparasi dan Logika","\n")

angka = int(input("Masukan angka <5 / >10 : "))

# ++++5---------
kurangdari = angka <5
print("apakah kurang dari 5 : ",kurangdari)

# ---------10++++
lebihdari = angka >10
print("apakah lebih dari 10 : ",lebihdari)

# +++++5-------10+++++++
gabung = kurangdari or lebihdari
print("apakah kurang dari 5 atau lebih dari 10: ",gabung)

# -----5++++++10--------
# kasus irisan
print("\n", "IRISAN","\n")
angka = int(input("Masukan angka >5 dan <10 : "))

kurangdari = angka <10
lebihdari = angka >5

tengah = kurangdari and lebihdari
print("apakah kurang dari 10 dan lebih dari 5: ",tengah)

print("\n","Latihan","\n")

number = int(input("Masukan angka :"))

lebihdarinol = number >0
kurangdarilima = number <5

tengahlimanol = lebihdarinol and kurangdarilima 
print("Apakah angka anda lebih dari nol dan kurang dari lima: ",tengahlimanol)

lebihdaridelapan = number >8
kurangdarisebelas = number <11

tengahdelapansebelas = lebihdaridelapan and kurangdarisebelas
print("Apakah angka anda lebih dari 8 dan kurang dari 11: ",tengahdelapansebelas)
      
gabungan = tengahlimanol or tengahdelapansebelas
print("\n","Hasil gabungannya : ",gabungan)

print("tes")





