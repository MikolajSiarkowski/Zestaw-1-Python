liczba = 123045603200000000120
napis = str(liczba)
suma = 0;
for x in range(len(napis)):
    if(napis[x] == '0'):
        suma += 1
print(suma)
