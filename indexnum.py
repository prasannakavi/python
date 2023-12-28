def index_vowel(a):
    out=[]
    i=0
    for var in range (0,len(a)):
        if a[var] in 'aeiouAEIOU':
            out=out+[i]
            i=i+1
    return out
out=index_vowel("happy new year")
print(out)