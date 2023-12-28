a=[4,7,6,2]
def add(var,i=0):
    if len (a)-1==i:
        return var[i]
    return var[i]+add(var,i+1)
out=add(a)
print(out)