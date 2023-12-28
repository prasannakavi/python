def data(a):

        if type(a) in (int,float,complex,bool):
            return True
        else:
            return False
out=filter(data,[1,2,2,4])
print(list(out))