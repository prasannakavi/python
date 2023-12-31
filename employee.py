class Employee:
    company='Tesla'
    Ceo='Elen musk'

    def insert_member(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid
anusha=Employee()
siri=Employee()
ABI=Employee()
Employee.insert_member(anusha,'anusha',22,50000,201)
Employee.insert_member(siri,'siri',23,55000,206)
ABI.insert_member('ABI',24,10,122)
