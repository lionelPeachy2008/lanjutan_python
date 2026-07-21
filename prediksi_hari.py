import datetime as wektu

tanggal = int(input("Masukan tanggal : "))
bulan = int(input("Masukan bulan : "))
tahun = int(input("Masukan tahun : "))

kalender = wektu.date(tahun,bulan,tanggal)
print(f"Hari ini = {kalender} \nDengan hari = {kalender:%A}")

maju = int(input("Ingin maju berapa hari : "))
majudpn = wektu.timedelta(days=maju)

tanggal_baru = kalender + majudpn
print(f"maju {maju} hari menjadi {tanggal_baru} dengan hari {tanggal_baru:%A}")