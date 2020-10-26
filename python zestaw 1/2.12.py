line = "Ala ma koty i psy"
L = line.split()
print("napis: " ,line)
x = 0
wynik1 = ""
wynik2 = ""
for x in range(len(L)):
    wynik1 += L[x][0:1]
    wynik2 += L[x][len(L[x])-1:len(L[x])]
print("napis stworzony z pierwszych znakow: ",wynik1)
print("napis stworzony z ostatnich znakow: ",wynik2)
