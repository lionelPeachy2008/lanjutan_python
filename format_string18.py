# format string

nama = "lionel"
format = f"halo {nama},gimana kabarmu"
print(format)

#boolean
bool = True
format_bool = f"itu {bool}"
print(format_bool)

# angka 
angka = 20.15
format_angka = f"angka = {angka}"
print(format_angka)

# bilangan bulat
angka = 12
format_bil = f"bilangan bulat = {angka:d}"
print(format_bil)

# bilangan ribuan
angka = 12000
format_bil = f"bilangan bulat = {angka:,}"
print(format_bil)

# bilangan desimal
angka = 12.8321
format_bil = f"bilangan desimal = {angka:.1f}"
print(format_bil)

# menampilkan leading zero
angka = 12.8321
format_bil = f"bilangan desimal = {angka:07.1f}"
print(format_bil)

# menampilkan tanda + atau -
a_plus = 10
a_minus = -10
format_plus = f"plus = {a_plus:+d}"
format_minus = f"minus = {a_minus}"

print(format_plus)
print(format_minus)

# memformat persen 
persen = 0.02
format_persen = f"persen = {persen:.3%}"
print(format_persen)

# aritmatika di kurung kurawal
harga = 1000
jumlah = 5
format_brg = f"Harga total = Rp.{harga*jumlah:,}"
print(format_brg)

# format angka lain (binary,octal,hexadecimal)
angka = 150
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)