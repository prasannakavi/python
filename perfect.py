num=int(input('enter a number'))
out=0
temp=True
for i in range(1,a):
    if num%i==0:
        a+=i
if not temp:
    print('perfect number')
else:
    print('not a perfect number')