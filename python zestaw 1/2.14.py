line = "Ala ma kota"
L = line.split()
x = 0
IsLongest = ""
for x in range(len(L)):
    if len(L[x]) > len(L[x-1]):
        IsLongest = L[x]               
    else:
        IsLongest = L[x-1]
print("(a)Najdluzszy wyraz to: ",IsLongest)
print("(b)Jego dlugosc to : ", len(IsLongest))
