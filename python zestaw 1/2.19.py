L=[1,23,155]
y=0
for y in range(len(L)):
	wynik = str(L[y])
	result = wynik.zfill(3)
	L[y] = result
print(L)

