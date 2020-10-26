line = "line of line"
print("line = ", line)
L=line.split()
x = 0
suma = 0
for x in range(len(L)):
    suma += len(L[x])
print("suma = ", suma)
