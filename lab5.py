#simulator of simple calculator +,-,/,//,*,**
def calc(a,b,op):
    if(op == '+'):
        return a+b
    elif(op == '-'):
        return a-b
    elif(op == '*'):
        return a*b
    elif(op == '/'):
        return a/b
    elif(op == '**'):
        return a**b
    elif(op == '//'):
        return a//b

a,b =[int(x) for x in input().split()]
op = input()
print(calc(a,b,op))
