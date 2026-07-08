## operator dalam bentuk method

# merubah ke upper case
kataBesar = "halo"
print("Katanya : " + kataBesar)
kataBesar = kataBesar.upper()
print("Katanya : " + kataBesar)

# merubah ke lower case
kataKecil = "HALOOO"
print("Katanya : " + kataKecil)
kataKecil = kataKecil.lower()
print("Katanya : " + kataKecil)

## pengecekan dengan isX method

# pengecekan lower dan upper case
huruf = "brooo"
ceklower = huruf.islower()
print(huruf + " is lower: " + str(ceklower))

huruf = "BROOO"
ceklower = huruf.islower()
print(huruf + " is lower: " + str(ceklower))

# isalpha() untuk mengecek semua huruf
# isalnum() huruf dan angka 
# isdecimal() angka 
# isspace() spasi,tab,new line
# istitle() semua kata dimulai dari huruf besar 

judul = "How To Train Your Dragon"
cekjudul = judul.istitle()
print(judul + " is title: " + str(cekjudul))

# mengecek pakai startswith() endswith()
cek_start = "Lionel Theodore".startswith("Lionel")
print("start is " + str(cek_start))

cek_end = "Lionel Theodore".endswith("Theodore")
print("end is " + str(cek_start))

# penggabungan komponen join() split()
pisah = ['aku','lionel','theodore']
gabungan = ','.join(pisah)
print("kata pisah: ", pisah)
print("digabung jadi: ", gabungan)

gabungan = ' '.join(pisah)
print("digabung jadi: ", gabungan)

gabungan = ' R '.join(pisah)
print("digabung jadi: ", gabungan)

gabung = "sayaRlionelRtheodore"
print(gabung.split('R'))

#alokasi karakter rjust(),ljust(),center()

kanan = "kanan".rjust(10)
print("'" + kanan +"'")

kiri = "kiri".ljust(10)
print("'" + kiri +"'")

tengah = "tengah".center(20,"=")
print("'" + tengah +"'")

# kebalikan strip()

tengahhilang = tengah.strip("=")
print("'" + tengahhilang +"'")

