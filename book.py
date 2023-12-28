print('welcome to book my show')
name=input('enter your name')
seat=eval(input('select number of seats:- '))
print('enter  1 to diamond')
print('enter 2 to gold')
print('enter 3 to silver')
seat=(int(input('enter the type of seat you want ')))
if(seat==1):
    print('it is a diamond')
    cost=200

elif(seat==2):
    print('it is a gold')
    cost=150
elif(seat==3):
    print('it is a silver is 100')
    cost=100
else:
    print('invalid seat')
    print('welcome to book my show',name)
    print('you booked the seats',seat)
print('you have selected the seat',seat,'and the amount is', seat*cost)
