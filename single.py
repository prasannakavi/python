class Grand:
    a=10
    def __init__(self,b):
        self.b=b
class parent(Grand):
    def __init__(self,b,c,d):
        super().__init__(b)
        self.c=c
        self.d=d
class child(parent):
    def __init__(self,b,c,d,e):
        super().__init__(b,c,d)
        self.e=e
        
obj=child(10,11,34,67)




   