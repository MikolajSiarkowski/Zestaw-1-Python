napis = " Ala Cebula Banan Cud Bp"
L = napis.split()
print("oryginalny napis : ",napis)
print("alfabetycznie : ",sorted(L))
print("pod wzgledem dlugosci : ",sorted(L, key = len))
