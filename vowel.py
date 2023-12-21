n=str(input('enter a string'))
i=0
out=''
while i<len(n):
    if '0'<=n[i]<='9':
        out=out+n[i]
    i+=1
print(out)



