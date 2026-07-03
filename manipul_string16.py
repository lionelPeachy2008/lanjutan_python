# 1. menyambung string
nper = "Lionel"
nked = "De"
nket = "Dore"

nama_lengkap = nper + ' ' + nked + ' ' + nket 
print("Nama lengkap : ", nama_lengkap)


# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("banyak kata" + nama_lengkap + ": " + str(panjang))

# 3. operator string
# mengecek char/string di string
kata = "De"
status = kata in nama_lengkap
print('apakah' + ' ' + kata + ' ' + "ada di" + ' ' + nama_lengkap + ' :', status)

kata = "De"
status = kata not in nama_lengkap
print('apakah' + ' ' + kata + ' ' + "ada di" + ' ' + nama_lengkap + ' :', status)

# 4. pengulangan string
print("Ha"*5)

#indexing(mulai dari 0)
print("index ke-0 dari " + nama_lengkap + ' : ',nama_lengkap[0] )
print("index ke-(-1) dari " + nama_lengkap + ' : ',nama_lengkap[-1] )
print("index ke-(0:5) dari " + nama_lengkap + ' : ',nama_lengkap[0:6] )
print("index ke-(4:8) dari " + nama_lengkap + ' : ',nama_lengkap[4:9] )
print("index ke-(0,2,4,6,8,10) dari " + nama_lengkap + ' :',nama_lengkap[0:14:2])

# huruf paling kecil
print("paling kecil : " + min(nama_lengkap))
# huruf paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord("L")
print("ASCII code untuk 'L' adalah : " + str(ascii_code))
data = 76
print("char untuk asii code 76 adalah : " + chr(data))

# 4. operator dalam bentuk method
data_huruf = "otong surotong porototong"
jumlah = data_huruf.count("o")
print("Jumlah huruf O pada " + data_huruf + " :" + str(jumlah))