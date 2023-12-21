marks=eval(input('enter a marks'))
if marks<100 and marks>=90:
    print('A+ grade')
elif  marks<90 and marks>80:
    print('A grade')
elif  marks<80 and marks>70:
    print('B+ grade')
elif marks<70 and marks>60:
    print('B grade')
elif marks<60 and marks>50:
    print('c grade')
elif marks<50 and marks>35:
    print('pass')
else:
    print('better luck next time')