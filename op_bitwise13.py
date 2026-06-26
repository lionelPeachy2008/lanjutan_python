#operator bitwise

a = 9
b = 5

#bitwise OR |
c = a | b 
print("\n=====OR=====")
print("Nilai :",a, "Binary :",format(a,"08b"))
print("Nilai :",b, "Binary :",format(b,"08b"))
print("-------------------------------------")
print("Nilai :",c, "Binary :",format(c,"08b"))
print("\n")

#bitwise AND &
c = a & b 
print("\n=====AND=====")
print("Nilai :",a, "Binary :",format(a,"08b"))
print("Nilai :",b, "Binary :",format(b,"08b"))
print("-------------------------------------")
print("Nilai :",c, "Binary :",format(c,"08b"))
print("\n")

#bitwise XOR ^
c = a ^ b 
print("\n=====XOR=====")
print("Nilai :",a, "Binary :",format(a,"08b"))
print("Nilai :",b, "Binary :",format(b,"08b"))
print("-------------------------------------")
print("Nilai :",c, "Binary :",format(c,"08b"))
print("\n")

#bitwise NOT ~
c = ~a
print("\n=====NOT=====")
print("Nilai :",a, "Binary :",format(a,"08b"))
print("Nilai :",c, "Binary :",format(c,"08b"))
print("-------------------------------------")
d = 0b0000001001
e = 0b1111111111
print("Nilai :",e^d, "Binary :",format(e^d,"08b"))
print("\n")

#shifting
#shift right (>>)
c = a >> 2
print("\n=====SHIFT RIGHT=====")
print("Nilai :",a, "Binary :",format(a,"08b"))
print("Nilai :",c, "Binary :",format(c,"08b"))

#shift left (<<)
c = a << 2
print("\n=====SHIFT LEFT=====")
print("Nilai :",a, "Binary :",format(a,"08b"))
print("Nilai :",c, "Binary :",format(c,"08b"))
print("\n")