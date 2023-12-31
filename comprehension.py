a="ABCDEF"
out=''
b=enumerate(a)
c={a[i]:i for i in range(len(a)) if i%2==0}
print(c)

