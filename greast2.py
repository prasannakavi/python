num1=eval(input('enter a number'))
num2=eval(input('enter a number'))
num3=eval(input('enter a number'))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,' is  second greatest')
    else:
        print(num3,' is second greatest')
else:
        print('enter a valid number')
