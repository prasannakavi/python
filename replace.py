a=input('enter a string')
i=0
out=''
while i<len(a):
    if  not ('A'<=a[i]<='Z' or 'a'<=a[i]<='z' or '0'<=a[i]<='9'):
         out=out+'_'
    else:
        out=out+a[i]
    i+=1
print(out)

    