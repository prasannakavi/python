def list(a):
    num=0
    for var in a:
        if type(var)==int:
            num+=var
    print(num)
list([1,2,3,'a','b',5])


