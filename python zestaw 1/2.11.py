line = "word"
result=""
print("before: ", line)
for x in line:
    result+=x+"_"
x=len(result)-1
print(result[0:x])
