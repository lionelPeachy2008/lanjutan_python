# width and multiline

#string multiline kutip 3
nama = "Lionel theodore"
umur = 18
tinggi = 160
hobi = "lari"
data = f""" 
nama   = {nama:>10}
umur   = {umur:>10} 
tinggi = {tinggi:>10}
hobi   = {hobi:>10}
"""
print(data)