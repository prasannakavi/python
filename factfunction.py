def frequency(a,b):
    count=0
    for i in a:
        for j in b:
            if i==j:
                count+=1
    print(count)
frequency('harika','prasanna')

