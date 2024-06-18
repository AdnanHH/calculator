def add(a,b):
    sum=a+b
    print("The sum is",sum)
def sub(a,b):
    diff=a-b
    print("The difference is",diff)
def mul(a,b):
    mul=a*b
    print("The product is ",mul)
def div(a,b):
    div=a/b
    print("The quotient is",div)
flag=0
while(flag==0):
    a=int(input("Enter the first number to be calculated"))
    b=int(input("Enter the second number to be calculated"))
    i=int(input("""Enter the option to be selected:
                    1.Add the two numbers
                    2.Subtract the two numbers
                    3.Multiply the two numbers
                    4.Divide the two numbers
                    5.Exit"""))
    match(i):
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
        case 5:
            break
            flag=1
