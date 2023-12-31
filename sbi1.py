class Sbi:
    branch='palamaner'
    ifsc='sbi00026'
    manager='jagan'
    loc='chittor'
    def __init__(self,name,mob,acc,pan,bal):
        self.name=name
        self.mobile=mob
        self.account=acc
        self.pan=pan
        self.balance=bal
    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
        @classmethod
        def change_mgr(cls,new):
             cls.manager=new  
        @staticmethod
        def add(a,b):
            return a+b      
chandra=sbi('nara chandra',899657354,7764357,'CBNT00000N',1)
lokesh=sbi('nara lokesh',5368274373,776543,'CBNT00000W',2)