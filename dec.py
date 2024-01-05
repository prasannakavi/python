def add():
    a=int(input('enter a:- '))
    b=int(input('enter b:- '))
    print(a+b)
def cal(fun):
    def inner():
        print('operation started')
        fun()
        print('operation done')
    return inner
add=cal(add)
add()