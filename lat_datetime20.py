# latihan date and time 

import datetime as dt

hariini = dt.date.today()
print(hariini)

print(f"hari ini adalah hari = {hariini:%A}")

print("Masukan tanggal, bulan, dan tahun kelahiran anda: ")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(f"harinya adalah hari : {tanggal_lahir:%A}")

umur_hari = hariini - tanggal_lahir
print(f"umur dalam hari = {umur_hari}")
umur_tahun = umur_hari.days // 365
print(f"umur anda sekarang adalah : {umur_tahun} tahun")