import random
num=random.randrange(0,9,2)
while True:
  a=int(input('enter a number:- '))
  if a == num:
    print('congeats!you successfully gussed the number',num)
    break
  elif a < num:
    print('enter a greater number')
  elif a >num:
    print('enter a lesser number')