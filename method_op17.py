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